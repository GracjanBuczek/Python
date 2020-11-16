# y=(2*C*D/H)^0,5 
import math
c=(float(input("Enter C: ")))
h=(float(input("Enter H: ")))
value = []
i=[x for x in input("Enter number: ").split(',')]
for d in i:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (",".join(value))
input ("Press any key to finnish")
