import json

# Converting JSON format to Python Objects - Using Loads Method
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)

# Converting Python Objects to JSON format - Using Dumps Method
dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
a = json.dumps(dict)
print(a)

list = ["apple", "bananas"]
b = json.dumps(list)
print(b)

tuple = ("apple", "bananas")
c = json.dumps(tuple)
print(c)

string = "hello"
d = json.dumps(string)
print(d)

int = 42
e = json.dumps(int)
print(e)

float = 31.76
f = json.dumps(float)
print(f)



