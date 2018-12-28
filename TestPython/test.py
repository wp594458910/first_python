list = ["shiruiqi", "chenwenmeng", "zhengqian", "luoyujin"]
print(list)

print(list[1])
list[1] = "wangpeng"
print(list)

list.insert(0, "aaa")
list.insert(2, "bbb")
list.append("ccc")
print(list)

print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop())
print(list)

del list[0]
print(list)

del list[0]
print(list)