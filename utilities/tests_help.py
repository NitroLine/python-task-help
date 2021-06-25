def make_tests(func, tests):
    success_count = 0
    for test in tests:
        result = func(test[0])
        status = result == test[1]
        success_count += int(status)
        print(f'arg: {test[0]}; '
              f'expected: {test[1]}; '
              f'was: {result}; '
              f'status: {status}')
    print(f"Tests count: {len(tests)}; Passed: {success_count}")