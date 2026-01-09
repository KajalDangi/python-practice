def anagram_checker(s1,s2):
    if len(s1) == len(s2):
        s1.sort(), s2.sort()
        if s1 == s2:
            return "Yes it is anagram checker"
        else:
            return "No it is not a anagram checker"

a=list(input("Enter the first String: "))
b=list(input("Enter the Second String: "))
print(anagram_checker(a,b))


