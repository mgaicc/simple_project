#functions practice
def check_is_palidrome(word):
    word = word.replace(" ", "").lower()
    if word[::-1] == word:
        return True
    else:
        return False
words = input('Write a word to check if palidrome or not, if palidrome return true, else return false: ')
print(check_is_palidrome(words))