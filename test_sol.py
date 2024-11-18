# Question-1 : Find Peak Element

lis=list(map(int,input("Enter list : ").split()))
peak_ind=-1
i=0
j=len(lis)-1
while i!=j:
    if i==0 and lis[i]>lis[i+1]:
        peak_ind=i;
        break
    elif  j==len(lis)-1 and lis[j]>lis[j-1]:
        peak_ind=j;
        break
    elif (lis[i]>lis[i-1] and lis[i]> lis[i+1]):
        peak_ind=i;
        break;
    elif (lis[j]>lis[j-1] and lis[j]> lis[j+1]):
        peak_ind=j
    i=i+1
    j=j-1
print(peak_ind)

# ======================================================================================================================
# Question-2 : Find the Encrypted String
st=list(input("Enter String : "))
k=int(input("Enter K :"))
st3=''
i=0
while i<len(st):
    st3=st3+st[(i+3)%(len(st))]
    i=i+1
print(st3)


# =======================================================================
# Question-4 : Sort Colors
lis=list(map(int,input("Enter list : ").split()))
lis1,lis2,lis3=[],[],[]
for i in lis:
    if i==0:
        lis1.append(i)
    elif i==1:
        lis2.append(i)
    else:
        lis3.append(i)
lis1=lis1+lis2+lis3
print(lis1)
