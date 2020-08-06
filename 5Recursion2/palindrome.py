def isPalindrome(w):
    if len(w) == 0 or len(w) == 1:
        return True
    elif w[0] == w[len(w) - 1]:
        return isPalindrome(w[1:len(w) - 1])
    else:
        return False

palindrome = input()
print(isPalindrome(palindrome))