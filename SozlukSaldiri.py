from asyncore import write
from itertools import product
from timeit import repeat
kelimler="oguzhan osman lale"

dizi1=[]

for i in kelimler:
    if i == " ":
        continue              #1 sesli olamaz son o olmamaz
    dizi1.append(i)


sesliharfler=["a","e","ı","i","o","ö","u","ü"]
dizi2=[]

for j in dizi1:
    
    for l in dizi2:
        if j==l:
            break
    else:
        dizi2.append(j)


f = open("sifreliste2", "w")

print(dizi2)

kombi= product(dizi2,repeat =5)

for j in list(kombi):
    #print(j[0])
    for h in sesliharfler:
        if j[0]==h:
            break
        elif j[4]=="o":
            break
    else:
        f.write("".join(j)+"\n") 