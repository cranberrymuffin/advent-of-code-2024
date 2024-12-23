import re
import operator

def mix(secret, value):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def compute_next_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret//32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret 

def find_nth_secret_number(initial_secret_num, n):
    secret = initial_secret_num
    for i in range(n):
        secret = compute_next_secret(secret)
    return secret

def get_prices_for_secret_number(initial_secret_num, n):
    prices = []
    secret = initial_secret_num
    for i in range(n):
        prices.append(secret % 10)
        secret = compute_next_secret(secret)
    return prices

def get_sequence_map(changes, prices):
    sequences = {}
    for i in range(0, len(changes) - 4):
        if (changes[i], changes[i+1], changes[i+2], changes[i+3]) not in sequences:
            sequences[(changes[i], changes[i+1], changes[i+2], changes[i+3])] = prices[i+3]
    return sequences

def get_changes(prices):
    changes = [None]
    secret = initial_secret_num
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])
        secret = compute_next_secret(secret)
    return changes

def combine_dicts(a, b, op=operator.add):
    return dict(a.items() + b.items() +
        [(k, op(a[k], b[k])) for k in set(b) & set(a)])


def find_price_for_sequence(sequence, price_maps):
    price = 0
    for price_map in price_maps:
        if sequence in price_map:
            price += price_map[sequence]
    return price

with open("input/dec22.txt", "r") as file:
    v1 = 0
    n = 2000
    secret_nums = []
    while line := file.readline():
        initial_secret_num = int(re.search(r'\d+', line.strip()).group())
        secret_nums.append(initial_secret_num)
        v1 += find_nth_secret_number(initial_secret_num, n)
    print(v1)

    all_sequences = set()
    price_maps = [] 

    for secret_num in secret_nums:
        prices = get_prices_for_secret_number(secret_num, 2000)
        sequences = get_sequence_map(get_changes(prices), prices)
        price_maps.append(sequences)
        all_sequences = all_sequences.union(set(sequences.keys()))

    v2 = 0

    for sequence in all_sequences:
        price = find_price_for_sequence(sequence, price_maps)
        if price > v2:
            v2 = price

    print(v2)

    