# ask the user for a sentence
sentence = input("Enter a sentence: ")

# dictionary to store vowel counts
vowel_counts = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

# covert the sentence to lowecase to count vowels correctly
sentence = sentence.lower()

# loop through each character and count vowels
for char in sentence:
    if char in vowel_counts:
        vowel_counts[char] += 1

# print the vowel counts
print("\nVowel Counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")