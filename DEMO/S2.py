# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:35:11 2018

@author: EccE
"""

k=input().strip().upper()
k1=k[::-1]
if k==k1:
    print("YES")
else:
    print("NO")