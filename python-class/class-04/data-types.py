list1 = [1, 2,6, 1]
print(list1[1])
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)


tuple1 = (5, 58, 1, 2, 3, 4)
print(sorted(tuple1))
print(sorted(tuple1, reverse=True))
print(tuple1[1])

dict1 = {"name": "test", "age": 10, 'district': 'dhaka', 'city': None, "country": "US"}
print(dict1['name'])
print(dict1['district'])
print(dict1.get('age'))
print(dict1.values())
print(dict1.values())
print(dict1)
print(len(dict1))

dict1.setdefault("city", "London")
dict1.update({"country": "UK"})
print(dict1)