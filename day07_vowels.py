word=input("Enter a word: ")
vowels=0
for char in word:
    if char in "aeiouAEIOU":
        vowels += 1
print("Number of vowels:", vowels)