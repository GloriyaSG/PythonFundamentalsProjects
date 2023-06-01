text = input()
forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
text_without_vowels = [print(f"{x}", end="") for x in text if x.lower() not in forbidden_vowels]