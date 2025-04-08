for i in range(5):
    print("Palindrome" if (s:=input("Enter a string: "))==s[::-1] else "Not a palindrome")
