def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1

    for c in t:
        if c not in counts:
            return False
        counts[c] -= 1
        if counts[c] < 0:
            return False

    return True

def main():
    print(valid_anagram("racecar", "carrace"))
    print(valid_anagram("jar", "jam"))

if __name__ == "__main__":
    main()
