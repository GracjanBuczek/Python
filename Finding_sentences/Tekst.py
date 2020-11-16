#Napisać program, który
#1. Będzie dzielił tekst na zdania.
#2. Odszuka i wypisze najdłuższe zdanie
#3. Policzy w nim słowa.

text=input("Enter your text: ")
r_text=text.replace("?",".").replace("!",".")
sentence = r_text.split(".") 

longest_sentence = max(sentence, key=len)
print(longest_sentence)

words=longest_sentence.split()
print("The longest sentece in text consist of",len(words),"words.")
