# tuples: immutable, there is no notion of an empty tuple
my_tuple = ("TLV,")
print(type(my_tuple))

#conver some other sequence into a tuple:
my_tuple = tuple(range(11))
print(my_tuple)

passwords = ("abc", "cde", "123", "abd")
print(passwords.count("abc"))
#accessing by index
print(passwords[1])

#workaround on how to change tuples:
temp_list = list(my_tuple)
temp_list.extend(["A", "b", "c"])
my_tuple = tuple(temp_list)
print(my_tuple)

#Sets : not ordered: not possible to access index
#dont allow duplicated elements

set = set()
countries = {"Israel", "USA", "Brazil"}
names = {"Shimon", "Hana", "Israel"}
print(countries[1]) # typeerror "set" object is not subscriptable

#for loops
for <variable_name> in <sequence_name>
