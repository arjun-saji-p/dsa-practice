count = {}

for ch in s1:
    count[ch] = count.get(ch, 0) + 1

for ch in s2:
    count[ch] = count.get(ch, 0) - 1

if all(value == 0 for value in count.values()):
    print("Anagram")
else:
    print("Not Anagram")
