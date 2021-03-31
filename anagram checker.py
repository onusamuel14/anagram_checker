string1 = input("Input first word:")
string2 = input("Input second word:")
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)
if sorted_string1 == sorted_string2:
     print("The two words are anagrams")
else:
    print("The two words are not anagrams")
