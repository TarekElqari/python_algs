#Un tuple est une liste qui ne peut plus être modifiée.
#Lorsque vous créez un tuple avec une seule valeur,
#n'oubliez pas d'y ajouter une virgule, sinon ce n'est pas un tuple.
#>>> mon_tuple = ("ok")
#>>> type(mon_tuple)
#<type 'str'>
#>>> mon_tuple = ("ok",)
#>>> type(mon_tuple)
#<type 'tuple'>


#use cases of tuples
#Returning multiple values from a function: Unlike some other programming languages,
#Python functions can return multiple values using tuples. For example:

def get_user_info():
    name = "John"
    age = 30
    city = "New York"
    return name, age, city

user_info = get_user_info()
print(user_info)  # Output: ('John', 30, 'New York')



#Storing coordinates: Tuples can be used to store coordinates
#in a Cartesian plane or geographical locations.


point = (3, 5)
#Iterating over sequences: Tuples can be used to iterate 
#over multiple sequences simultaneously using zip() function.

names = ('Alice', 'Bob', 'Charlie')
ages = (25, 30, 35)

for name, age in zip(names, ages):
    print(name, age)
#Dictionary keys: Tuples can be used as dictionary keys if they
#contain immutable elements like strings or numbers.
student_grades = {('Alice', 'Math'): 90, ('Bob', 'Math'): 85}


#Caching values in memoization: Tuples can be used as keys to cache 
#previously computed values in memoization techniques.


memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result
#Database records: Tuples can be used to represent rows from a database query result.
db_records = [('John', 25), ('Alice', 30), ('Bob', 35)]


#Unpacking: Tuples can be used to unpack sequences into individual variables.
coordinates = (3, 5)
x, y = coordinates
