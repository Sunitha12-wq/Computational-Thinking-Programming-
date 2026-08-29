def combine(first, second):
    output = []
    a = b = 0

    while a < len(first) and b < len(second):
        if first[a] < second[b]:
            output.append(first[a])
            a += 1
        else:
            output.append(second[b])
            b += 1

    output.extend(first[a:])
    output.extend(second[b:])

    return output


def iterativeMergeSort(numbers):
    size = 1
    total = len(numbers)

    while size < total:
        for start in range(0, total, 2 * size):
            first = numbers[start:start + size]
            second = numbers[start + size:start + 2 * size]

            combined = combine(first, second)

            for index, value in enumerate(combined):
                numbers[start + index] = value

        size *= 2

    return numbers


myArray = [42, -8, 19, 4, 31.5, -15, 27, 9]
sortedArray = iterativeMergeSort(myArray)

print("Sorted array:", sortedArray)