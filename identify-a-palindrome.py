def check_palindrome(input):
    input = input.lower()
    cleanedInput = ''.join(character for character in input if character.isalnum())
    for i in range(len(cleanedInput)):
        if cleanedInput[i] != cleanedInput[len(cleanedInput) - (i + 1)]:
            return False
    return True

print(check_palindrome('Hello World'))
print(check_palindrome("Go hang a salami, I'm a lasagna hog,"))
