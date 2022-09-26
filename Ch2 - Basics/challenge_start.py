
def is_palindrome(testStr):
    return True if testStr.lower() == testStr.lower()[::-1] else False

def prompt_input():

    while True:
        word = input("Enter string to test for palindrome or 'exit':")
        newWord = "";
        if word.lower() == 'exit':
            break
        else:
            for c in word:
                if c.isalnum():
                    newWord += c
            print(is_palindrome(newWord))


if __name__ == '__main__':
    prompt_input()

for i in range(6, 16):
    print(i)