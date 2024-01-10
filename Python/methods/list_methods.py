#list methods 

a = [1,2,3,"suraj"]
b = [44,65, 6, "Sagar"]
print(a)
print(b)
a.append("swami")
a.clear()
c = b.copy()
print(b.count(44))
print(c)

p = [11,22,33]
q = [44,55,66]

p.extend(q)
print(p)
print(p.index(22))
p.insert(2,77)
print(p)
p.pop()
print(p)
p.remove(11)
print(p)
p.reverse()
print(p)
p.sort()
print(p)