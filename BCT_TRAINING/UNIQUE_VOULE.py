sentence = input("sentence: ").lower()
vowels = set()

for char in sentence:
    if char in 'aeiou':
        vowels.add(char)

print("Unique vowels:", vowels)
