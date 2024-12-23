import re

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

def get_changes(prices):
    changes = [None]
    secret = initial_secret_num
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])
        secret = compute_next_secret(secret)
    return changes

with open("input/dec22.txt", "r") as file:
    v1 = 0
    n = 2000
    while line := file.readline():
        initial_secret_num = int(re.search(r'\d+', line.strip()).group())
        v1 += find_nth_secret_number(initial_secret_num, n)
    print(v1)

    prices = get_prices_for_secret_number(123, 10)
