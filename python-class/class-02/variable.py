test = 'test string'
My_Name = 'Al Amin Ahamed'
my_name = 'fdsf'


def my_function():
    name = "Python"
    print(name)


my_function()

def outer_function():
    name = "Python"

    def inner_function():
        name = "PHP"
        print(name)

    inner_function()

outer_function()


integer_number = 10
float_number = 10.25
# str = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

lists = [1, 2, 3]
tuple_ = (1, 2, 3)
dic = {'data' : 'fasdfasf', 'key':'value'}

subjects = ['bangla', 'english', 'math']
books = ['englishfortody', 'mathforu', 'historyofbangla']
subjects.append('history')

t = ('teafd', 'fasdfas', subjects, dic)
print(t)

friend = {'name' : "Syaed", 'age': 40}
friends = [friend, friend ,friend]
print(friend['name'])
print(friends)

print(type(friends))
print(type(integer_number))
print(friends[0]['name'])

print(str(True))
print(int())
print(bool())
print(list())


