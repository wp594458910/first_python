bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# 访问一个列表最后一个元素，索引为-1
print(bicycles[-1])

bicycles.append("baoma")
print(bicycles)

bicycles[0] = "aaaa"
print(bicycles)

bicycles.insert(0, "bbbb")
print(bicycles)

del bicycles[0]
print(bicycles)

# pop() 可删除列表末尾的元素
# bicycles.pop()
# print(bicycles)

# 输出最后一个元素
last_data = bicycles.pop()
print(last_data)
print(bicycles)

# 弹出列表任何位置的元素
first_data = bicycles.pop(0)
print(first_data)
print(bicycles)

# 根据值删除元素
bicycles.remove("redline")
print(bicycles)

