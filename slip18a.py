#Write a Python program to compute element-wise sum of given tuples.
 #Original tuples: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
 #Element-wise sum of the said tuples: (6, 9, 8, 6) .

t=list(map(int,input('enter the 1st tuple:').split()))
t1=list(map(int,input('enter the 2nd tuple:').split()))
t2=list(map(int,input('enter the 3rd tuple:').split()))

t3=[]
for i in range(len(t)):
    t3.append(t[i]+t1[i]+t2[i])
print('Element-wise sum of the said tuples:',t3)
