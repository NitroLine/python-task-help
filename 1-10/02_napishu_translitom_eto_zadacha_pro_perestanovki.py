def make_permutations(collection: list):
    length = len(collection)
    if length <= 1:
        yield collection
        return
    indices_permutation = []
    start_indices = [0]
    while len(start_indices) > 0:
        if len(indices_permutation) == length:
            yield [collection[index] for index in indices_permutation]
            start_indices.pop()
            indices_permutation.pop()
            continue

        for index in filter(lambda index_tmp:
                            index_tmp not in indices_permutation,
                            range(start_indices[-1], length)):
            start_indices[-1] = index + 1
            indices_permutation.append(index)
            start_indices.append(0)
            break
        else:
            start_indices.pop()
            indices_permutation.pop()


if __name__ == "__main__":
    for permutation in make_permutations([5]):
        print(permutation)

    print()

    for i, permutation in enumerate(make_permutations([5, 6, 7, 4])):
        print(f'{i}: {permutation}')
