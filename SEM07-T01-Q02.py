d1 = int(input())
m1 = int(input())
a1 = int(input())
d2 = int(input())
m2 = int(input())
a2 = int(input())
data1 = (d1+m1+a1)
data2 = (d2+m2+a2)
if (data1) > (data2):
    print('%d/%d/%d' %(d1,m1,a1))
elif data1 == data2:
    print('%d/%d/%d' % (d1, m1, a1))
else:
    print('%d/%d/%d' %(d2,m2,a2))
