''' *** SORTING A LIST*** '''

li = [9, 1, 8, 2, 5, 7, 3, 6, 4]

#Method: Use the sorted function and save the answer as a new variable:
sorted_list = sorted(li)
        # Sorted list is now equal to [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Storing the sorted list in reverse
sorted_list = sorted(li, reverse=True)
   #sorted list is now equal to [9, 8, 7, 6, 5, 4, 3, 2, 1]

''' ***SORTING A TUPLE (IS DONE THE SAME WAY)*** '''
tup = (9, 1, 8, 2, 5, 7, 3, 6, 4)

sorted_tuple = sorted(tup)
    # sorted_tuple is now equal to [1, 2, 3, 4, 5, 6, 7, 8, 9]

''' *** SORTING A DICTIONARY *** '''
dictionary = {'name': 'Preben', 'job': 'web-development', 'age': '36', 'language': 'Python'}
sorted_dictionary = sorted(dictionary)  # <--- the sorted function sorts the dictionary keys 
                                        # sorted_dictionary = ['age', 'job', 'language', 'name']


''' ***SORTING CLASS INSTANCES '''
class Employee(): 
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # <--- this specifies how we want this class represented when we print it out to the screen. 
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# Sorting method one: Create function
def e_sort(emp):   #<--- In this case the emp paramenter will be the Employee class instance
    return emp.name

sorted_employees = sorted(employees, key=e_sort)
        # sorted_employees = [(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]

sorted_employees = sorted(employees, key=e_sort, reverse=True)
        # sorted_employees = [(Sarah,29,$80000), (John,43,$90000), (Carl,37,$70000)]

# sorting method two: use attrgetter
from operator import attrgetter     # <--- 'attribute-getter'

sorted_employees = sorted(employees, key=attrgetter('salary'))
        # sorted_employees = [(Carl,37,$70000), (Sarah,29,$80000), (John,43,$90000)]