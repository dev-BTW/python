def isPalindrome(string):
    string = string.casefold()
    return string[::-1] ==string


while(True):
    word = str(input("Enter a word: "))
    if isPalindrome(word):
        print("{0} is a Palindrome".format(word))
    else:
        print("{0} is not a Palindrome".format(word))