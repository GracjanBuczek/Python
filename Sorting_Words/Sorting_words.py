#Napisać program wczytujący z klawiatury listę wyrazów 
# a następnie wyświetlający je posortowane alfabetycznie.

lista=sorted(input("").split(), key=str.lower)
print (lista)
input("Press any key to finish")
