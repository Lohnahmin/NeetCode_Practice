def top_k_frequent(nums, k):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    pairs = []
    for value, freq in counts.items():
        pairs.append((value, freq))

    pairs.sort(key=lambda x: x[1], reverse=True)

    result = []
    for i in range(k):
        result.append(pairs[i][0])

    return result

def main():
    print(top_k_frequent([1, 2, 2, 3, 3, 3], 2))
    print(top_k_frequent([7, 7], 1))

if __name__ == "__main__":
    main()
