#coding:gbk
from random import shuffle
num=range(1,14)
se=['����','����','÷��','��Ƭ']
wang=['����','С��']
pai=[]
for i in se:
    for m in num:
        k = i+str(m)
        pai.append(k)
for w in wang:
    pai.append(w)
shuffle(pai)
a=','.join(pai[:17])
b=','.join(pai[17:34])
c=','.join(pai[34:51])
s=','.join(pai[51:])
print 'a����: '+a
print 'b����: '+b
print 'c����: '+c
print '����: '+c
