#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:28:10 2018

@author: kmkgmx
"""

import numpy as np
#Generate random Socres
a = np.random.normal(loc = 60,scale = 60,size = 60)
student = []
i = 0

#print(a)

for i in a:
    if (i <= 100) & (i >=0) :
        student.append(int(i))

print(student)

#QuickSorts Students' scores

def Partition(A,p,r):
    x = A[r]
    i = p - 1
    j = p
    while j <= r-1:
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
        j = j + 1
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1


def QuickSort(A,p,r):
    if p<r:
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

QuickSort(student,0,len(student)-1)

print(student)