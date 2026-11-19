import copy
import re
from itertools import combinations


def compute(a, switches):
    a = str(a)
    if a.isdigit():
        return int(a)

    vals = a.split(' ')
    if len(vals) == 3:
        next_a = vals[0].strip()
        operator = vals[1].strip()
        next_b = vals[2].strip()
        if operator == 'AND':
            return int(compute(next_a, switches)) and int(compute(next_b, switches))
        if operator == 'OR':
            return int(compute(next_a, switches)) or int(compute(next_b, switches))
        if operator == 'XOR':
            return int(compute(next_a, switches)) ^ int(compute(next_b, switches))
    else:
        return compute(switches[vals[0]], switches)
    
def extract_number(switches, starts_with):
    my_list = []
    for key in switches:
        if key.startswith(starts_with):
            index = int(re.search(r'\d+', key).group())
            while(len(my_list) <= index):
                my_list.append(0)
            my_list[index] = switches[key]
    
    my_list.reverse()
    return my_list

def binary_to_decimal(number):
    return int(''.join(str(x) for x in number), 2)

def has_cycle(switches):
    visiting = set()
    visited = set()

    def visit(wire):
        if wire in visiting:
            return True
        if wire in visited:
            return False

        value = switches[wire]
        if not isinstance(value, str) or value.isdigit():
            visited.add(wire)
            return False

        parts = value.split()
        dependencies = (parts[0], parts[2]) if len(parts) == 3 else (value,)
        visiting.add(wire)
        for dependency in dependencies:
            if dependency in switches and visit(dependency):
                return True
        visiting.remove(wire)
        visited.add(wire)
        return False

    return any(visit(wire) for wire in switches)

def disjoint_combinations(pairs, count):
    selected = []
    used_wires = set()

    def generate(start):
        if len(selected) == count:
            yield tuple(selected)
            return

        needed = count - len(selected)
        for index in range(start, len(pairs) - needed + 1):
            first, second = pairs[index]
            if first in used_wires or second in used_wires:
                continue

            selected.append(pairs[index])
            used_wires.update((first, second))
            yield from generate(index + 1)
            selected.pop()
            used_wires.remove(first)
            used_wires.remove(second)

    yield from generate(0)

def find_suspicious_outputs(switches, mismatched_outputs):
    gates = {
        wire: value.split()
        for wire, value in switches.items()
        if isinstance(value, str) and len(value.split()) == 3
    }
    consumers = {}
    for _, (left, operator, right) in gates.items():
        consumers.setdefault(left, []).append(operator)
        consumers.setdefault(right, []).append(operator)

    cone = set()
    pending = list(mismatched_outputs)
    while pending:
        wire = pending.pop()
        if wire in cone or wire not in switches:
            continue
        cone.add(wire)
        gate = gates.get(wire)
        if gate:
            pending.extend((gate[0], gate[2]))

    z_outputs = [wire for wire in gates if wire.startswith('z')]
    highest_z = max(z_outputs, key=lambda wire: int(wire[1:]))
    suspicious = set()
    # These gate/consumer patterns are invariants of this ripple-carry adder.
    for wire, (left, operator, right) in gates.items():
        input_xy = left.startswith(('x', 'y')) and right.startswith(('x', 'y'))
        first_bit_and = {left, right} == {'x00', 'y00'}
        uses = consumers.get(wire, ())

        if wire.startswith('z') and wire != highest_z and operator != 'XOR':
            suspicious.add(wire)
        elif operator == 'XOR':
            if not wire.startswith('z') and not input_xy:
                suspicious.add(wire)
            elif input_xy and not first_bit_and and 'XOR' not in uses:
                suspicious.add(wire)
        elif operator == 'AND' and not first_bit_and and 'OR' not in uses:
            suspicious.add(wire)

    return suspicious & cone
    
with open("input/dec24.txt", "r") as file:
    switches = {}

    while line := file.readline():
        line = line.strip()
        if ':' in line:
            data = line.split(":")
            value = data[1].strip()
            switches[data[0].strip()] = int(value) if len(value) == 1 else value 
        elif '->' in line:
            data = line.split("->")
            value = data[0].strip()
            switches[data[1].strip()] = int(value) if len(value) == 1 else value 
    
    origional_formulas = copy.deepcopy(switches)

    def compute_z(switches): 
        for key in switches:
            a = switches[key]
            if isinstance(a, str) and ('AND' in a or 'OR' in a or 'XOR' in a):
                origional_formulas[key] = a
                switches[key] = compute(switches[key], switches)
        z = extract_number(switches, 'z')
        z = binary_to_decimal(z)
        return z
    
    def swap(switches, swaps):
        swapped_switches = copy.deepcopy(switches)
        for first, second in swaps:
            swapped_switches[first], swapped_switches[second] = (
                swapped_switches[second],
                swapped_switches[first],
            )
        return swapped_switches
    
    z = compute_z(origional_formulas)

    x = extract_number(switches, 'x')
    y = extract_number(switches, 'y')

    true_sum = binary_to_decimal(x) + binary_to_decimal(y)
    mismatched_outputs = {
        f"z{bit:02d}"
        for bit in range(max(true_sum.bit_length(), z.bit_length()))
        if ((true_sum >> bit) & 1) != ((z >> bit) & 1)
    }
    suspicious_outputs = find_suspicious_outputs(switches, mismatched_outputs)
    print("Mismatching bits:", sorted(int(wire[1:]) for wire in mismatched_outputs))
    print("Candidate wires:", sorted(suspicious_outputs))

    possible_pairs = list(combinations(sorted(suspicious_outputs), 2))
    x_wires = sorted((wire for wire in switches if wire.startswith('x')), key=lambda wire: int(wire[1:]))
    y_wires = sorted((wire for wire in switches if wire.startswith('y')), key=lambda wire: int(wire[1:]))
    input_width = min(len(x_wires), len(y_wires))
    max_input = (1 << input_width) - 1
    test_vectors = {
        (binary_to_decimal(x), binary_to_decimal(y)),
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (max_input, 0),
        (0, max_input),
        (max_input, 1),
        (max_input, max_input),
    }
    for bit in range(input_width):
        value = 1 << bit
        test_vectors.update(
            (
                (value, 0),
                (0, value),
                (value, value),
                (value - 1, 1),
                (max_input ^ value, value),
            )
        )

    for swap_set in disjoint_combinations(possible_pairs, 4):
        swapped_formulas = swap(switches, swap_set)
        if has_cycle(swapped_formulas):
            continue

        for x_value, y_value in sorted(test_vectors):
            swapped_set = copy.deepcopy(swapped_formulas)
            for bit, wire in enumerate(x_wires):
                swapped_set[wire] = (x_value >> bit) & 1
            for bit, wire in enumerate(y_wires):
                swapped_set[wire] = (y_value >> bit) & 1
            if compute_z(swapped_set) != x_value + y_value:
                break
        else:
            print(swap_set)
            break
    else:
        print("No valid swap set found")
            
    
            