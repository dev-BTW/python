def isPalindrome(sentence):
    sentence = sentence.casefold()
    string = ""

    for i in sentence:
        if i.isalnum():
            string+=i

    return (string[::-1]==string)


print(isPalindrome("Was it a car, or a cat, I saw?"))
print(isPalindrome("Do geese see God?"))
print(isPalindrome("Desnes not far, rafton sensed"))