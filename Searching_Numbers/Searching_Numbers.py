# Napisać program, w którym funkcja wprowadza do listy (przekazanej jako
# argument)
# liczby z zakresu od 2000 do 3200 włącznie, które są podzielne przez 7
# i nie są wielokrotnością 5.
# Wartością zwracaną przez funkcje jest ilość liczb spełniających w.w.
# warunek. Wartość zwróconą przez funkcję wypisać na ekran.

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print("All of numbers meeting the condtion are: ",",".join(l))
print("Number of all arguments meeting the condition is: ", len(l))
input("Press any key to finnish...")



