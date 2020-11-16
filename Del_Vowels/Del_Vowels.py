list_ = input("Enter sentence:")
vowel = ["a", "e", "i", "o", "u", "y"]

for i in list_:
    if i in vowel:
        list_ = list_.replace(i, " ")
 
print(list_)
input("Press any key to finish...")
