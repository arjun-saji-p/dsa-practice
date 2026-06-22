text = "aabbcdde"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break
