#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:10:57 2024

@author: erenozdilkural
"""

import numpy as np
import pandas as pd
import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum


v1 = np.arange(0,20)
v2 = np.arange(0,25)
n = 3000
r = 2000

#parameters

dd = pd.read_excel('Emergency-Aid-Data.xlsx', sheet_name='District Distance',  usecols="B:U")
md = pd.read_excel('Emergency-Aid-Data.xlsx', sheet_name='Distance - 25x20',  usecols="C:V", nrows = 26 )

dd_distance = dd.values.tolist()
md_distance = md.values.tolist()

del md_distance[0]

a = []

for i in v1:
    for j in v1:
        if dd_distance[i][j] <= r:
            a.append(1)
        else:
            a.append(0)
            
a = np.array(a)
a = a.reshape(20,20)


b = []

for k in v2:
    for j in v1:
        if md_distance[k][j] <= n:
            b.append(1)
        else:
            b.append(0)
            
b = np.array(b)
b = b.reshape(20,25)


model = gp.Model("ProjectQ1_2000")

#DV's

X = model.addVars(v1, v1, vtype=GRB.BINARY, name="X")

Y = model.addVars(v1, vtype=GRB.BINARY, name="Y")


#Objective

model.setObjective(quicksum(Y[i] for i in v1), GRB.MINIMIZE)

#Constraints

for j in v1:
    model.addConstr(quicksum(X[i,j] for i in v1) >= 1)
    
for i in v1:
    for j in v1:
        model.addConstr(X[i,j] <= a[i,j]*Y[i])
        
for i in v1:
    model.addConstr(quicksum(b[i,k] for k in v2) >= Y[i])
    
model.optimize()

if model.status == GRB.OPTIMAL:
    for v in model.getVars():
        print(f"{v.varName}: {v.x}")

if model.status == GRB.OPTIMAL:
    print(f"With the radius =2km, the optimal objective value is to open {model.objVal} different facilities.")
else:
    print("The model did not solve to optimality.")



    
