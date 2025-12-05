def top_k_frequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    items = list(counts.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]

    result = []
    for i in range(k):
        result.append(items[i][0])

    return result

def main():
    print(top_k_frequent([1,2,2,3,3,3], 2))
    print(top_k_frequent([7,7], 1))

if __name__ == "__main__":
    main()
