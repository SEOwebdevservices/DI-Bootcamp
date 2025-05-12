#lists

#A list is a sequences of elements
#syntax
#some_list = list() # to convert other sequences in a list
#other_list = []  #best way to create an empty list
#@accessing by IndexErrorprint(some_list[1])

#my_list = []
#methods for lists
#some_lists, append("A")
#print(some_list)

#my_list.extend(["b","c", "d",])
#print(my_list)

#create An empty 

#char_list = []
#char_list.extend(["Penny", "Sheldon", "Lenard", "Walowitz"])
#print(char_list)

#range(list(range(1,7)))
#print(list(range(1,7)))

#nums_list(list(range(1,7)))
#print(list(range(1,7)))

#print(nums_list[2:6])

#copied_list = nums_list[:]
#print(copied_list)
#copied_list = nums_list.copy()

#other methods
#insert(where, what)
#remove(what) removes the 1st occurence of the element
#del nums_list[3] will delete the item in the rth position on the list
#nums_list.pop() by default deletes the ???
#fruits["banana", "orange", "lime","apple"]
#sorted()
#sorted_fruit = sorted(fruits))
#print(sorted_fruits)
#print(fruits)

#sort()
#fruits.sort()
#print(fruits)

#index(element) and it returns the index of this element
#how to find something in a list and replace it
list1 = [5, 10, 15, 20, 25, 50, 20]
if list1.index(20):
    index_found = list1.index(20)
    list1.insert(index_found, 200)
    list1.remove(20)  
    print(list1)  
else:
    print("element not found")

