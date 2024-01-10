#python's all set methods 
a = {"suraj","sagar",}
b = {"suraj","sagar",}
fruits = {"apple", "banana", "cherry"}
itCompanies = {"google", "microsoft", "apple"}

a.add("dattu")
print(a)

a.clear()
print(a)

x = b.copy()
print(x)

z = a.difference(b)
print(z)

b.difference_update(a)
print(b)

fruits.discard("apple")
print(fruits)

mm =fruits.intersection(itCompanies)
print(mm)

fruits.intersection_update(itCompanies)
print(fruits)

isDisjoint = fruits.isdisjoint(itCompanies)
print(isDisjoint)

isSub = fruits.issubset(itCompanies)
print(isSub)

isSuperSet = fruits.issuperset(itCompanies)
print(isSuperSet)

itCompanies.pop()
print(itCompanies)

cd=b.symmetric_difference(itCompanies)
print(cd)

b.symmetric_difference_update(itCompanies)
print(b)

print(b.union(itCompanies))

print(b.update(itCompanies))