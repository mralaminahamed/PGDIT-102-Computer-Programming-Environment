lists = ['physics', 'chemistry', 1997, 2000]
lists[0] = 'Biology'
del lists[0]
print(lists)

lists.insert(1, 1455)
value = lists.pop(0)
length = len(lists)
print(length)

print(value)
print(lists)
lists.clear()
print(lists)

voter = {'name': 'tewst', }
if voter['name'] == 'test':
    print(voter)



# • list[2] = 2001;
# • print (list[2])
# • print (list[2])
# • list[2:4] = [2001 2004];