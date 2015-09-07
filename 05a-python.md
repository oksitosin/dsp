# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> •	Lists are a list of values. Each one of them is numbered, starting from zero. You can remove values from the list, and add new values. 

>>   Example: cats' names.
          
          cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', ‘Chester']

>> •	Tuples are just like lists, but you can't change their values. The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from zero. 

>>    Example: the names of the months of the year.
          
          months = (‘Jan’,'Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')

>> •  Dictionaries have keys and values. Each of the keys within a dictionary must be unique. If you make an assignment using an existing key as the index, the old value associated with that key is overwritten by the new value. Since tuples are immutable, they will work as keys in dictionaries. 


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> * sets — unordered collections of unique elements
>> * lists — ordered collections of elements

>> A set is a dictionary with no values. Set cannot contain duplicates. We can create sets from lists with eliminating the duplicates - same as combining two sets (always unique elements).

>> In lists, the elements are accessed by indexes. In sets, elements should be hashable to be found (same as in dictionary keys). 

>> Hash function is faster than indexing, so finding an element is faster in sets.


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> * Lambda is an anonymous function we can use with python. If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function.

>> Example 1:

          ex = [2, 18, 9, 22, 17, 24, 8, 12, 27]

          print filter(lambda x: x % 3 == 0, ex)  
          print map(lambda x: x * 2 + 10, ex)
          print reduce(lambda x, y: x + y, ex)
  
>> outputs for example 1:
  
          [18, 9, 24, 12, 27]
          [14, 46, 28, 54, 44, 58, 26, 34, 64]
          139

>> Example 2:

          a=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
          s=sorted(a,key=lambda i: i[1] )
          print s

>> output for example 2:
 
          [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> * List comprehension is a nice way to simplify code. According to the python documentation, "list comprehensions provide a concise way to create lists.”

>> If we wanted to create a list of squares for the numbers between 1 and 10, we could do the following:

          squares = []
          for x in range(10):
              squares.append(x**2)

>> This is an simple example, but using list comprehensions makes it simpler:

          squares = [x**2 for x in range(10)]


>> * Filter and map vs list comprehension:

          result1=[x for x in range(10) if x % 2 == 0]

          result2=list(filter((lambda x: x % 2 == 0), range(10)))

          result3 = []
          for x in range(10):
              if x % 2 == 0:
                  result3.append(x)
	
          print result1
          print result2
          print result3

>> The three codes above are the same to extract the even numbers in range 10. The output comes as:

          [0, 2, 4, 6, 8]
          [0, 2, 4, 6, 8]
          [0, 2, 4, 6, 8]
          
 >> The filter here is not much longer that the list comprehension. But we can combine an if and a map, in a single expression:

          square=[x ** 2 for x in range(10) if x % 2 == 0]
          print square

>> instead of:

          square2=[]
          for x in range(10):
              if x%2==0
                  square2.append(x**2)
          print square2

>> to have:
          
          [0, 4, 16, 36, 64]
          
>> as an output.          

>> * Set comprehension and dictionary comprehension:

      bag={(1,'red','pants'),(2,'blue','dress'),(3,'black','sweater'),(4,'white','dress'),(5,'black','dress')}
          
      sc={i[2] for i in bag }
      print sc

      dc={i[0]: i for i in bag}
      print dc
          
 >> Above example shows a tuple called bag. With set comprehension, we can get what unique pieces we have:
           
      set(['sweater', 'dress', 'pants'])
          
  >> We can use dictionary comprehension, with the same tuple as shown above which gives the following output:
 

      {1: (1, 'red', 'pants'), 2: (2, 'blue', 'dress'), 3: (3, 'black', 'sweater'), 4: (4, 'white', 'dress'), 5: (5, 'black', 'dress')}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





