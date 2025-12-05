def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

def main():
    print(contains_duplicate([1, 2, 3, 3]))  # True
    print(contains_duplicate([1, 2, 3, 4]))  # False

if __name__ == "__main__":
    main()
