#1/2+ 2/3+ 3/4 +n/(n+1) | n>0
x=int(input())
sum=0.0
for i in range(1,x+1):
    sum += float(float(i)/(i+1))
print(sum)
