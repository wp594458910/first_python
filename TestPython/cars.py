cars = ["bmw", "audi", "toyota", "subaru"]
# 永久性排序
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# 临时排序
cars1 = ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars1))
print(cars1)

# 倒着打印
cars1.reverse()
print(cars1)

length = len(cars1)
print(length)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'bmw' in cars:
    print(True)
else:
    print(False)

