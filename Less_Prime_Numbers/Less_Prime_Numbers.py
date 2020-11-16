n = (int(input("Enter n: ")))

print("Prime numbers less than",n,"are:")

for x in range(n):
      if x > 1:
       for y in range(2,x):
           if (x % y) == 0:
               break
       else:
           print(x)

input("Press any key to finish...")
