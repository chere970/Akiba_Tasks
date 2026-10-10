import re

word=input("Enter a word: ")
cleaned_word=re.sub(r'[^A-Za-z0-9]','',word).lower()
inversed_word=cleaned_word[::-1]

if cleaned_word==inversed_word:
    print(f"{word} is palindrom")
else: print(f"{word} is not palindrom")


