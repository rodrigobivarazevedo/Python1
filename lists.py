#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#When we say that lists are ordered, it means that the items have a defined order,
#  and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list
#The list is changeable, meaning that we can change, add, and remove items in a list after 
# it has been created.
#List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
# A list with strings, integers and boolean values


students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print(student)


#Notice that for each student in the students list,
#  it will print the student as intended. You might wonder why we did not use the _ designation 
# as discussed prior. We choose not to do this because student is explicitly used in our code

#We can utilize len as a way of checking the length of the list called students.
#Imagine that you don’t simply want to print the name of the student, 
# but also their position in the list. To accomplish this, you can edit your code as follows:

students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

#Notice how executing this code results in not only getting the position of each student 
# plus one using i + 1, but also prints the name of each student. 
# len allow you to dynamically see how long the list of the students is regardless how much it grows.

