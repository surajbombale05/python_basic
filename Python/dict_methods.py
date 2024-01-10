player={
    "rohit":45,
    "dhoni":7,
     "virat":18
}
print(player)
x=player.copy()
print(x)

a = ("vk","msd","hitman")
b = 100
thisdict = dict.fromkeys(a, b)
print(thisdict)

getdata = player.get("rohit")
print(getdata)

item = player.items()
print(item)

key = player.keys()
print(key)

player.pop("rohit")
print(player)

player.popitem()
print(player)

c =player.setdefault("dhoni",33)
print(c)

player.update({"virat":188})
print(player)

value= player.values()
print(value)