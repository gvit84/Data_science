def palindrom():
    word = input('Enter word: ')
    if word[::-1] == word[0::]:
        print(f'This word is PALINDROM')
        return True
    else:
        print(f'This word is not PALINDROM')
        return False

print(palindrom())
