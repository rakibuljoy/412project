import ast
from graphviz import Digraph as dgph
from IPython.display import Image
from pprint import pprint

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def difference(a,b):
    return abs(a-b)

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

usedVariable = 10

for i in range(11):
    unusedVariable =11
    print(multiplication(i,usedVariable))
for i in range(11):
    Variable =6
    print(difference(i,usedVariable))
