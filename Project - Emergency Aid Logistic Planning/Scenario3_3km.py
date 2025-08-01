#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:57:18 2024

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
r = 3000
M = 1000

#parameters

dd = pd.read_excel('Emergency-Aid-Data.xlsx', sheet_name='District Distance',  usecols="B:U")
md = pd.read_excel('Emergency-Aid-Data.xlsx', sheet_name='Distance - 25x20',  usecols="C:V", nrows = 26 )

dd_distance = dd.values.tolist()
md_distance = md.values.tolist()
p = [14242,	30003, 10302, 22978, 22380,	17390, 25261, 29124, 14366, 13744, 14827, 11720, 13718,	 43433,	27568, 28591, 37144, 8093, 30147, 11649]

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

Z = model.addVars(v1, vtype=GRB.BINARY, name="Z")

#Objective

model.setObjective(quicksum(dd_distance[i][j] * X[i, j] for i in v1 for j in v1), GRB.MINIMIZE)

#Constraints

model.addConstr(quicksum(Y[j] for j in v1) <= 4)

for j in v1:
    model.addConstr(quicksum(X[i,j] for i in v1) <= M * Z[j])
    
for j in v1:
    model.addConstr(quicksum(X[i,j] for i in v1) >= Z[j])
    
for i in v1:
    for j in v1:
        model.addConstr(X[i,j] <= a[i,j]*Y[i])
        
for i in v1:
    model.addConstr(quicksum(b[i,k] for k in v2) >= Y[i])

for j in v1:
    model.addConstr(quicksum(X[i,j] for i in v1) >= 1)
    
model.optimize()

if model.status == GRB.OPTIMAL:
    for v in model.getVars():
        print(f"{v.varName}: {v.x}")
  
if model.status == GRB.OPTIMAL:
    print(f"With the radius = 3km, the optimal objective value is the total distance of {model.objVal} meters.")
else:
    print("The model did not solve to optimality.")