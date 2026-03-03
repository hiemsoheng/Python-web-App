empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "NYC"}
dict_constructor = dict(name="Bob", age=25)
from_tuples = dict([("a", 1), ("b", 2)])
# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



person = {"name": "Alice", "age": 30, "city": "NYC"}
print(person["name"])  # Alice
print(person.get("age"))  # 30
print(person.get("city", "Unknown"))  # Unknown

country = person.get("country")
if country == None:
    country = "Country not found"
print(country)
#print(person["country"])  # This code will get error due to cannot find the key in dictionary



user = {}

user.update({"name": "Charlie","age": 28,"city": "LA"})
user["name"] = "Visal"
user.setdefault("country", "USA")  # This will add 'country' key with value 'USA' if it doesn't exist
user.setdefault("country", "Canada")  # This will not change the value of 'country' since it already exists
print(user)  # {'name': 'Visal', 'age': 28, 'city': 'LA', 'country': 'USA'}


# removeuser = user.pop("age")  # This will remove the 'age' key from the dictionary
# print(removeuser)  # 28
# print(user)  # {'name': 'Visal', 'city': 'LA', 'country': 'USA'}

# user.popitem()  # This will remove the last inserted key-value pair from the dictionary
# print(user)  # {'name': 'Visal', 'city': 'LA'}


#Looping througy keys
for key in user:
    print(f'Key id {key} Value is {user[key]}')


#Looping through items can get both key, value form item inside dictionary
print("---------------------------------")
for key,val in user.items():
    print(f'Key id {key} Value is {val}')


#Looping thruogh dict using only values
print("---------------------------------")
for val in user.values():
    print(f'Value is {val}')


text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


clean_text = text.replace(" ", "")
print(clean_text)  # helloworld


before_join = text.split()
print(before_join)  # ['hello', 'world']

clean_text1 = "".join(text.split(" "))
print(clean_text1)  # helloworld
print("".join(before_join))  # hello\nworld


def marge_dicts(dict1, dict2):
    marge = dict1.copy()  # Create a copy of the first dictionary
    for key, value in dict2.items():
        if key in marge:
            marge[key] += value  # If the key exists, add the values
        else:
            marge[key] = value  # If the key doesn't exist, add it to the merged dictionary
    return marge
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 3, "c": 4, "d": 5}
print(marge_dicts(d1, d2))  