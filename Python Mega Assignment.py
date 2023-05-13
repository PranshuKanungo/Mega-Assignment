## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Q2. Why is Python called a dynamically typed language?

Q3. List some pros and cons of Python programming language?

Q4. In what all domains can we use Python?

Q5. What are variable and how can we declare them?

Q6. How can we take an input from the user in Python?

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Q8. What is type casting?

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Q10. What are keywords?

Q11. Can we use keywords as a variable? Support your answer with reason.

Q12. What is indentation? What's the use of indentaion in Python?

Q13. How can we throw some output in Python?

Q14. What are operators in Python?

Q15. What is difference between / and // operators?

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Q18. What are boolean operator?

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```

Q20. What are conditional statements in Python?

Q21. What is use of 'if', 'elif' and 'else' keywords?

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Q26. What is a string? How can we declare string in Python?

Ans. String is the group or collection of characters and alphabates.
The string declaration can be done by simply writing any variable equals to any word or sentence inside single
or double quotes. and by default it will be a string in python because string is a in-built function in python.

Q27. How can we access the string using its index?


Ans. To access any single character in string using it's index we can simply write the string name with it's
index in square brackets and it's index starts with [0].

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

Code: print(string[9: ])

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

Code: string = "Big Data iNeuron"
         print((string[-1:-8:-1]))

Q30. Resverse the string given in the above question.

Code: print(string[ : :-1])

Q31. How can you delete entire string at once?

Code: Using the del() command :- del(string)

Q32. What is escape sequence?

Ans: An escape sequence is a sequence of characters that, 
when used inside a character or string, does not represent itself but is converted into another character 
or series of characters. Ex: /n

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```

First we can assign this to any variable and then we can call it in our print function. 
For ex: str = "iNeuron's Big Data Course"
            print(str)

Q34. What is a list in Python?

Ans. List in python is the collection of different types of datatypes like string, integer, 
float etc. which are stored inside the square brackets and each one separated by a comma 
and kept inside the single or double quote.

Q35. How can you create a list in Python?

Ans: A list in python can be created by assigning any variable to square brackets. For example:- list = []

Q36. How can we access the elements in a list?

Ans: To access the elements in a list we can use the variable name/list name and then can access the
individual element from it by writing the index number in square brackets.
For example:- list = [1,2,3,4]
print(list[1]) 
output-2

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 

Code: print(lst[4][2])

Q38. Take a list as an input from the user and find the length of the list.

lst = int(input("Enter the list"))
print(len(lst))

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]

code:
lst = ["Welcome", "to", "Data", "course"]
lst.insert(2, "Big")
print(lst)

Q40. What is a tuple? How is it different from list?

Ans: Tuple is an immutable object and it doesn't support the update function or any change; they have fixed values.
While List can be changed and the size of the list is not fixed like a tuple.

Q41. How can you create a tuple in Python?

Ans. To create a tuple in python we just need to assign a variable with the parenthesis bracket.
For Ex: t1 = ()

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

Ans: t1 = () //creating the tuple 
Now to add our name in the tuple either we need to convert the tupple into the list or we should have added the
name while creating the tupple itself and therefore we won't be able to add the name. 


Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
Ans. No we can not use the append command in tupple it's immutable and will not change 
it's fix size and hence gets failed.

Q44. Take a tuple as an input and print the count of elements in it.

Ans. tup = tuple(input("Enter your number for tuple by , separator").split(','))
            print(len(tup))

Q45. What are sets in Python?

Ans: Sets are the collection of unique values, which are written inside a square brackets.

Q46. How can you create a set?

Ans: We can create the set by assigning it to a variable with the keyword set().

 Q47. Create a set and add "iNeuron" in your set.

Ans: set_1 = set()
        set_1.add("iNeuron")
            print(set_1)

Q48. Try to add multiple values using add() function.

Ans:
set_1 = {1,2,3,4}
set_2 = [5,6,7,8,9]
for items in set_2:
    set_1.add(items)
print(set_1)

Q49. How is update() different from add()?

Ans: We use add() to add single value to a set and update() to add sequence values to a 
set and therefore to add more than one value in a set using add() we use the for loop.

Q50. What is clear() in sets?

Ans: It removes all the elements in the sets.

Q51. What is frozen set?

Ans. Frozen set is an immutable form of python normal set, whose value and elements are fixed and you can 
not add() any value in it unlike other normal sets.

Q52. How is frozen set different from set?

Ans. The main difference between frozen set and the normal set is that frozen set can not be modified like a 
normal set, it's immutable while we can add and update in any normal set().

Q53. What is union() in sets? Explain via code.

Ans: The union() of sets gives us the value of both the sets in a single union set. It works like an OR 
function; it returns the unique values of both the sets combined together. The representation of the union() is "|"
set_1 = {1,2,3,4,5}
set_2 = {6,7,8,9,9,10}
print("the union of sets is", set_1 | set_2)

Q54. What is intersection() in sets? Explain via code.

Ans: The intersection() of sets gives us the common values of both the sets and not the values from both the 
sets like our union() function.The representation of the intersection of sets is through "&". 
set_1 = {1,2,3,4,5,6,7}
set_2 = {6,7,8,9,9,10}
print("the intersection of sets is", set_1 & set_2)

Q55. What is dictionary in Python?

Ans: Dictionary is the kind of data structure which has the elements in it in key-value pair form. 

Q56. How is dictionary different from all other data structures.

Ans. Dictionary stores the values in key:value format and not any single element like other data structures.

Q57. How can we delare a dictionary in Python?

Ans. To declare a dictionary in python we can simply use the curly brackets and put the 'key': 'Value'
pair in it separated with ':'

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
Ans. <class 'dict'>

Q59. How can we add an element in a dictionary?

Ans. To add an element in the dictionary we use the dictionary name along 
with the key ['key'] and assign it with the value.
for example: dict {'India' : 'MP', 'US': 'Washington'}
   To add an element:- dict['Africa']  = 'Xyz'

Q60. Create a dictionary and access all the values in that dictionary.

Ans. dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
    print(dict.values())

Q61. Create a nested dictionary and access all the element in the inner dictionary.
 Ans. nested_dict = {"a" : {"Harry": 1, "Carry":2, "Jerry" : 3}, "b" : "4"}
print(nested_dict['a'])

Q62. What is the use of get() function?

Ans. get() function returns the value of a specified key.
ex: dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
    print(dict.get('Harry'))

Q63. What is the use of items() function?

Ans. items() return the list of tuples of each key value pair. 
For ex: dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
print(dict.items())
output:- dict_items[('Harry',1),('Carry',2),('Cherry',3)]

Q64. What is the use of pop() function?

Ans. pop() removes the element with the specified key. 
    For ex: dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
            dict.pop('Harry')
            print(dict)
    
    output:- {'Carry' : 2, 'Cherry' : 3}

Q65. What is the use of popitems() function?

Ans. popitems() function removes the last added key-value pair from the dictionary. 
    For ex: dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
            dict.popitem()
            print(dict)
    output:- {'Harry' : 1, 'Carry' : 2}

Q66. What is the use of keys() function?

Ans. Keys() function returns the list of keys from the dictionary.
     for ex:  dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
            print(dict.keys())
output- dict_keys(['Harry', 'Carry', 'Cherry'])

Q67. What is the use of values() function?

Ans. values() function returns the list of values from the dictionary.
for ex:  dict = {'Harry' : 1, 'Carry' : 2, 'Cherry' : 3}
    print(dict.values())
output- dict_values([1, 2, 3])

Q68. What are loops in Python?

Ans. When we need to use the same code repeatedily for a specific condition to be satisfied then we use
    the loops in python so that we can skip writing the code for n number of times for the same condition.

Q69. How many type of loop are there in Python?

Ans. There are mainly three types of loops:
     While Loop 
     For loop  
     Nested loop

Q70. What is the difference between for and while loops?

Ans.For loop is used when number of iterations are known and while loop is used when the number of iterations
are unknown.
Syntax of while loop:-
condition = true //Initialization
while condition:
    statements

syntax for for loop:-
    for items in range():
        print()


Q71. What is the use of continue statement?

Ans. Continue statement helps in skipping the current execution in the loop and moves to the next value in the 
loop without jumping out of the loop.

Q72. What is the use of break statement?
 
Ans. If you want to jump out of the loop and not from the complete code then to simply jump out of the loop
we can use the break statement.

Q73. What is the use of pass statement?

Ans. The pass statement can be used when we don't have the code to in the if condition and we want it to skip
to the else statement therefore to maintain the flow of the code we use the pass statement.

Q74. What is the use of range() function?

Ans. range() function returns the series or sequence of numbers starting from zero to the number we assign it. 
ex: range(5) 
so it will give us numbers from 1 to 5:- 0,1,2,3,4

Q75. How can you loop over a dictionary?

Ans. We can use for loop for dictionary. 
ex: for x, y in dict.items():
        print(x,y)
    

### Coding problems
Q76. Write a Python program to find the factorial of a given number.

Code:- 

n = int(input("Enter a number"))
factorial = 1
def factorial(n):
    if n==0 :
        return 1
    else:
        return n * factorial(n-1) 
           
result = factorial(n)
print("the factorial of", n, "is", result)


Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

Code:
p= int(input("Enter the percentage"))
r= int(input("Enter the rate"))
t= int(input("Enter the time"))
def simple_interest(p,r,t):
    print("This is our principle", p)
    print("This is our rate", r)
    print("This is our time",t)
    
    si= (p*r*t)/100
    print("the simple interest is", si)
simple_interest(p,r,t)


Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

Code:
P = int(input("Enter the principle"))
R = int(input("Enter the rate"))
t = int(input("Enter the time"))
A= P*(pow((1+ R/100),t))
CI= A - P
print("The compound interest is", CI)

Q79. Write a Python program to check if a number is prime or not.

Code:
n = int(input("Enter the number"))
for i in range(2,n):
    if n%i != 0:
        print('The number is prime')
        break
    else:
        print("The number is not prime")
        break

Q80. Write a Python program to check Armstrong Number.

Code: 
n = int(input("Enter your number"))
sum = 0
temp = n
while temp > 0:
     digit = temp % 10
     sum += digit ** 3
     temp //= 10 
if n == sum :
     print(n,"It is an Armstrong number")
else:
     print(n, "It is not an armstromg number") 



Q81. Write a Python program to find the n-th Fibonacci Number.

Code:
n= int(input("enter the number"))
def fibonacci(n):
        if n == 0 or n<0:
            return 0
        elif n==1:
             return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
result = fibonacci(n)
print("The nth fibonacci of", n, "is", result)

Q82. Write a Python program to interchange the first and last element in a list.

Code: 
list=[1,2,3,4,8,7,5,6]
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print(list)

Q83. Write a Python program to swap two elements in a list.

Code:
list=[1,2,3,4,8,7,5,6]
temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)

Q84. Write a Python program to find N largest element from a list.

Code1: 
list = [1,2,3,4,5,8,7,6]
max=0
for items in list:
    if items>max:
        max = items 
    else:
        pass
print(max)

Code2:
list = [1,2,3,4,5,8,7,6]
n=1
for items in list:
    if n == len(list):
        break 
    elif list[n-1]>list[n]:
        temp = list[n-1]
        list[n-1] = list[n]
        list[n] = temp 
        n = n+1 
    else:
        n= n+1
        continue
print(n)


Q85. Write a Python program to find cumulative sum of a list.

Code:
list = [1,2,3,4,5,6,7,8]
j = 0
new_list=[]
for i in range(0,len(list)):
    j = j + list[i]
    new_list.append(j)
print(new_list)

Q86. Write a Python program to check if a string is palindrome or not.

Code:
word = input("Enter your word")
def ispalindrone(word):
     return word == word[::-1]

if ispalindrone(word):
     print("Yes it's a palindrone")
else:
     print("Not a palindrone")


Q87. Write a Python program to remove i'th element from a string.

Code:
string = input("Enter your string")
i = int(input("Enter the value of i"))
new_string = string[ : i] + string[i+1: ]
print(new_string)

Q88. Write a Python program to check if a substring is present in a given string.

Code:
string = input("Enter the string")
substring = input("Enter your substring")
 if substring.lower() in string.lower(): 
     print("The substring is present in string")
 else:
     print("substring is not present in string")

Q89. Write a Python program to find words which are greater than given length k.

Code:
s= "hello nice to meet you guys"
k=2
print( [word for word in s.split() if len(word) > k])

Q90. Write a Python program to extract unquie dictionary values.

Code: 
test_dict = {'abc': [5, 6, 7, 8],
             'xyz': [10, 11, 7, 5]}
res = {ele for val in test_dict.values() for ele in val }
print(res)

Q91. Write a Python program to merge two dictionary.
 
Code:
dict_1 = {'1' : "Harrry", '2':"Jerry"}
dict_2 = {'3' : "Carry", '4': "Ferry"}
def merge(dict1,dict2):
    res = {**dict_1, **dict_2}
    return res
dict_3 = merge(dict_1, dict_2)
print(dict_3)

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```
Code:
list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
print(dict(list))

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```
Code:
list = [9, 5, 6]
new_list=[(items, items**3) for items in list]
print(new_list)


Q94. Write a Python program to get all combinations of 2 tuples.

Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

Code:
import itertools
test_tuple1= (7,2)
test_tuple2= (7,8)
res = [(a,b) for a in test_tuple1 for b in test_tuple2]+ [(a,b) for a in test_tuple2 for b in test_tuple2]
print("The combination of 2 tuples are", (res))


Q95. Write a Python program to sort a list of tuples by second item.

Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Code:
tup = [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
def Sorted_tuple(tup):
    lst = len(tup)
    for i in range (0,lst):
        for j in range(0, lst-i-1):
          if (tup[j][1] > tup[j+1][1]):
              temp = tup[j]
              tup[j] = tup[j+1]
              tup[j+1]= temp 
    return tup
print(Sorted_tuple(tup))


Q96. Write a python program to print below pattern.

* 
* * 
* * * 
* * * * 
* * * * * 

Code: 

n =5 
for i in range(n):
    for j in range(i+1):
        print("*", end = ' ')
    print()
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
Code:

n=5 
for i in range(n):
    for j in range(i, n):
        print("*", end = ' ')
    print()

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```
Code:

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end = '')
    for j in range(i+1):
        print("*", end = ' ')
    print()



Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```
Code:

n=5 
for i in range(n):
    for j in range(i+1):
        print(j+1, end = ' ')
    print()

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```
Code:

n=5
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k), end = ' ')
    k= k + 1
    print()