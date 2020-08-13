# Given a string, sort it in decreasing order based on the frequency of characters.


class Solution:
    def frequencySort(self, s: str):
        letters = Counter(s)
        frequencies = []
        final = ""
        for letter in letters:
            frequencies.append([letters[letter], letter])
        frequencies = reversed(sorted(frequencies))
        for frequency in frequencies:
            final += frequency[1] * frequency[0]
        return final


print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))
print("The strings above should be \"eert\", \"cccaaa\", and \"bbAa\".")
