a = 5
b = 5
print(a == b)
print(a is b)
print(id(a) , id(b))

func = []

for i in range(1,5):
    # func.append(lambda: i)
    func.append(lambda x=i: x)

for f in func:
    print(f())



l = [1, 2, 3, 4, 1, 4, 5, 0, 2, 0, 0]
m = 8
n = [1, 2, 4, 0, 5]
o = 4
# o/p = [1,1,1,2,2, 2,3,4,4,4, 5,5]
# order of n

l[:] = sorted(i for i in l+n if i != 0)
print(l)



