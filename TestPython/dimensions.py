dimensions = (200, 50)
print(dimensions)
print(dimensions[0])

for dimension in dimensions:
    print(dimension)

# 元祖不能修改，可以重新复制
dimensions = (400, 200)

for dimension in dimensions:
    print(dimension)