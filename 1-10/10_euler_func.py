from math import gcd


def calculate_euler_func(n: int) -> int:
    k = 0
    for i in range(1, n + 1):
        k += 1 if gcd(i, n) == 1 else 0
    return k


if __name__ == "__main__":
    tests = [(1, 1), (2, 1), (5, 4), (6, 2), (66, 20)]
    success_count = 0
    for test in tests:
        result = calculate_euler_func(test[0])
        status = result == test[1]
        success_count += int(status)
        print(f'arg: {test[0]}; '
              f'expected: {test[1]}; '
              f'was: {result}; '
              f'status: {status}')
    print(f"Tests count: {len(tests)}; Passed: {success_count}")

