from z3 import *
x = Int('x')
y = Int('y')

if(x>0):
	y=x
else:
	y=-x

s = Solver()
s.add(Not(Implies(Or(And(x>0, y==x), And(x<=0, y==-x)), y >= 0)))
print(s.check())

