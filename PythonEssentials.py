
# coding: utf-8

# ## Python Essentials
# 
# * Feb 18, 2017
# * Carlos P. & Juan C.
# * Lecture available [here!](https://lectures.quantecon.org/py/python_essentials.html)

# In[1]:

import os
print(os.getcwd())


# In[2]:

countries = ('Japan', 'Korea', 'China')
cities = ('Tokyo', 'Seoul', 'Beijing')
for country, city in zip(countries, cities):
    print('The capital of {0} is {1}'.format(country, city))


# In[8]:

letter_list = ['a', 'b', 'c']
test = enumerate(letter_list)
for item in test:
    print(item)


# In[9]:

x = 'yes' if None else 'no'
print(x)


# In[18]:

a = [1, 2, 3, 4]
list(map(lambda x: x**2, a))


# In[19]:

from scipy.integrate import quad
get_ipython().magic('pinfo quad')


# ### Exercises

# In[31]:

## 1, part 1
x_vals = [2, 4, 6, 8, 10]
y_vals = [1, 3, 5, 7, 9]

inner_prod = sum([x*y for x, y in zip(x_vals,y_vals)])
print(inner_prod)


# In[41]:

## 1, part 2
howManyEvens = sum([item % 2 == 0 for item in range(100)]) # one lineeee!
print(howManyEvens)


# In[48]:

## 1, part 3
pairs = ((2, 5), (4, 2), (9, 8), (12, 10), (5, 9))
hmec = sum([x%2 == y%2 == 0 for x, y in pairs])
print(hmec)


# In[119]:

## 2

def p(x, coeff):
    """
    Args:
    x: polynomial base
    coeff: must be a list of coefficients
    
    Outputs the resulting value of the polynomial
    """
    try:
        return sum([c*(x**power) for power, c in enumerate(coeff)])
    except:
        if type(coeff) != list:
            print("coeff argument must be a list")
        else: print("x argument must be numeric")

p(1, coeff=[2,4])


# In[99]:

## 3
import string

text = "   hola Como estamOs HOY?!!!!   "

def checkUpperLetters(text):
    text = text.replace(" ", "")
    for punc in string.punctuation:
        text = text.replace(punc, "")
    print(text)
    return sum([orig == upp for orig, upp in zip(list(text), list(text.upper()))])

checkUpperLetters(text)


# In[117]:

## 4
A = (1,2)
B = (3,2,1,0)

def compareSeq(seq_a, seq_b):
    """
    Args:
    seq_a & seq_b can be a list, a tuple or a string
    Function returns True if every element in seq_a is also an element in seq_b
    """
    seq_a = list(seq_a)
    seq_b = list(seq_b)
    new_a = [a for a in seq_a if a in seq_b]
    return new_a == seq_a

compareSeq(A,B)


# In[118]:

get_ipython().magic('pinfo compareSeq')


# In[ ]:

## 5

