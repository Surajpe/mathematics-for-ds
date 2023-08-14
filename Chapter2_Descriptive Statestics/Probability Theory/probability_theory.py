# -*- coding: utf-8 -*-
"""Probability Theory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/almabetterschool/700a07f889f51959fc3b9f3e92a925ff/probability-theory.ipynb

# Set Theory Examples
"""

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8, 10}
C = {1, 3, 5, 7, 9}

A.intersection(B)

A.union(B)

B.union(C)

B.intersection(C)

A.intersection(B).intersection(C)

"""# Counting Examples"""

def factorial(n):
  f = 1
  for i in range(1, n+1):
    f = f * i
  return f

def P(n, r):
  return int(factorial(n)/factorial(n-r))

def C(n, r):
  return int(factorial(n)/(factorial(r) * factorial(n-r)))

C(2, 1)

P(10, 2)

from itertools import permutations
from itertools import combinations

# Get all the permutations
seq = permutations(['a','b','c'])

for p in list(seq):
   print(p)

P(3,3)

#Getting all permutations of a particular length.
seq = permutations(['a','b', 'c'], 2)

for p in list(seq):
   print(p)

P(3,2)

# Get all the combinations
combi = combinations(['a','b','c', 'd', 'e'], 3)

for c in list(combi):
   print(c)

C(5,3)

"""Students of Cohort Aravali are going to complete a Capstone Project next week. They will be divided in teams of 3. In how many ways can we do this? There are a total of 24 students in the cohort."""

aravali = {'Akshay', 'Chinmaya', 'Debashish',
            'DILAVAR', 'DIVY', 'HRUSHIKESH',
            'Isha', 'Kartikey', 'Vaideswar',
            'Pranav', 'Mihir', 'Monika',
            'SATYA', 'YAGNIK', 'Raj',
            'RAJESH', 'Rohan', 'Shashank',
            'Soumya', 'Sudhanshu', 'Suraj',
            'Sweety', 'Vanshika', 'Nishant'}

C(24, 3)

seq = combinations(aravali, 3)

for p in list(seq):
   print(p)

"""In any team, we don't want more than 1 student from the top 8 students."""

top_8 = {'Chinmaya', 'Debashish', 'HRUSHIKESH', 'Isha',
         'YAGNIK', 'Raj', 'Rohan', 'Sudhanshu'}

remaining = students - top_8

remaining

C(16, 2)

seq = combinations(remaining, 2)

for p in list(seq):
   print(p)

"""# Probability Basics Examples"""

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8, 10}
C = {1, 3, 5, 7, 9}

P_A = len(A)/len(U)

P_A

A.intersection(B)

P_A_int_B = len(A.intersection(B))/len(U)

P_A_int_B

S = {1, 2, 3, 4, 5, 6}

A = {1, 3, 5}

B = {4, 5, 6}

A.union(B)

A.intersection(B)

#P(A U B) = P(A) + P(B) - P(A int B)

#Area 1: 1, 3

#Area 2: 5

#Area 3: 4, 6

#P(A) = Area 1 + Area 2
#P(B) = Area 2 + Area 3
#P(A int B) = Area 2
#P(A U B) = Area 1 + Area 2 + Area 3

"""# Bayes' Theorem Example

The punctuality of trains has been investigated by considering a number of train
journeys. In the sample, 60% of trains had a destination of Manchester, 20%
Birmingham and 20% Edinburgh. The probabilities of a train arriving late in
Manchester, Edinburgh or Birmingham are 30%, 20% and 25% respectively.

If a late train is picked at random from the group under consideration, what is the
probability that it terminated in Manchester?

M = event that the train has the destination Manchester
B = event that the train has the destination Birmingham
E = event that the train has the destination Edinburgh
L = event that the train arrived late

P(M) = 0.6
P(B) = 0.2
P(E) = 0.2

P(L|M) = 0.3
P(L|B) = 0.25
P(L|E) = 0.2

P(M|L) = ?

P(M|L) = [P(L|M)*P(M)]/([P(L|M)*P(M)] + [P(L|B)*P(B)] + [P(L|E)*P(E)])

P(M|L) = (0.3*0.6) / (0.3*0.6 + 0.25*0.2 + 0.2*0.2) =
"""

# P(B|L)





