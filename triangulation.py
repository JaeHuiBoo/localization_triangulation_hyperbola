from sympy import *
import math
from matplotlib import pyplot as plt

#input: r, m, n, t1, t2, t3 (it will be received from the sensors)
#location of three sensors :(x1, y1), (x2, y2), (x3, y3)
# ==> (m-r, n+r/sqrt(3)), (m+r, n+r/sqrt(3)), (m, n-2*r/sqrt(3)) 
#2r: the distance between two sensors
#(m,n): the center of the triangle(made with sensors)
#t1, t2, t3: TDOA between sensors  
#v: the velocity of sound (343m/s)

init_printing()

r = float(input('Enter r: '))
m = float(input('Enter m: '))
n = float(input('Enter n: '))
t0 = float(input('Enter t0: '))
t1 = float(input('Enter t1: '))
t2 = float(input('Enter t2: '))
v = 343 # m/s

# sensor points
pointMid_x = m
pointMid_y = n
point0_x = m-r
point0_y = n+r/math.sqrt(3)
pointMid0_x = m
pointMid0_y = n+r/math.sqrt(3)
point1_x = m+r
point1_y = n+r/math.sqrt(3)
pointMid1_x = m+r/float(2)
pointMid1_y = n-r/(2*math.sqrt(3))
point2_x = m
point2_y = n-2*r/math.sqrt(3)
pointMid2_x = m-r/float(2)
pointMid2_y = n-r/(2*math.sqrt(3))

# hyperbola between x0, x1
# [parallel movement] axis x +m, axis y +n+r/np.sqrt(3)
# f(x,y) -> f(x-m-r,y-n-r/math.sqrt(3))
x0 = Symbol('x')
y0 = Symbol('y')
eq_0 = Eq((4*(x0-m)**2/float((v*t0)**2)-4*(y0-n-r/math.sqrt(3))**2/float(4*r**2-(v*t0)**2)),1)

# hyperbola between x1, x2
# [rotate movement] +60 degree (from origin, counterclockwise)
# [parallel movement] axis x -m-r/float(2), axis y -n+r/(2*math.sqrt(3))
# g(x,y) -> g((x-m-r/float(2))/float(2)+math.sqrt(3)*(y-n+r/(2*math.sqrt(3)))/float(2),-(x-m-r/float(2))*math.sqrt(3)/float(2)+(y-n+r/(2*math.sqrt(3)))/float(2))
x1 = Symbol('x')
y1 = Symbol('y')
eq_1 = Eq((4*((x1-m-r/float(2))/float(2)+math.sqrt(3)*(y1-n+r/(2*math.sqrt(3)))/float(2))**2/float((v*t1)**2)-4*(-(x1-m-r/float(2))*math.sqrt(3)/float(2)+(y1-n+r/(2*math.sqrt(3)))/float(2))**2/float(4*r**2-(v*t1)**2)),1)

# hyperbola between x2, x0
# [rotate movement] +120 degree (from origin, counterclockwise)
# [parallel moevement] axis x -m+r/float(2), axis y -n+r/(2*math.sqrt(3))
# h(x,y) -> h(x/float(2)-math.sqrt(3)*y/float(2)-m+r/float(2),math(3)*x/float(2)+y/float(2)-m-r/float(2))
x2 = Symbol('x')
y2 = Symbol('y')
eq_2 = Eq((4*((x2-m+r/float(2))/float(2)-math.sqrt(3)*(y2-n+r/(2*math.sqrt(3)))/float(2))**2/float((v*t2)**2)-4*(math.sqrt(3)*(x2-m+r/float(2))/float(2)+(y2-n+r/(2*math.sqrt(3)))/float(2))**2/float(4*r**2-(v*t2)**2)),1)

#for 2 hyperbola for test
result = solve([eq_0,eq_1])

#for 3 hyperbola intersection
#result = solve([eq_0,eq_1,eq_2])

print(len(result))
print(result)

val = []

for r in result:
    a = r[Symbol('x')]
    b = r[Symbol('y')]
    a = str(a)
    b = str(b)
    a = a[0:a.index(' ')]
    b = b[0:b.index(' ')]
    val.append(float(a))
    val.append(float(b))

print(len(val))
print(val)

x = Symbol('x')
y = Symbol('y')

plot_implicit(Or(eq_0,eq_1,eq_2),(x,-10,10),(y,-10,10),line_color='green',markers=[{'args':[point0_x,point0_y],'color':"black",'marker':"o",'ms':3},
{'args':[point1_x,point1_y],'color':"black",'marker':"o",'ms':3},
{'args':[point2_x,point2_y],'color':"black",'marker':"o",'ms':3},
{'args':[pointMid_x,pointMid_y],'color':"blue",'marker':"o",'ms':2},
{'args':[pointMid0_x,pointMid0_y],'color':"black",'marker':"o",'ms':2},
{'args':[pointMid1_x,pointMid1_y],'color':"black",'marker':"o",'ms':2},
{'args':[pointMid2_x,pointMid2_y],'color':"black",'marker':"o",'ms':2},
{'args':[val[0],val[1]],'color':"red",'marker':"o",'ms':2},
{'args':[val[2],val[3]],'color':"red",'marker':"o",'ms':2},
{'args':[val[4],val[5]],'color':"red",'marker':"o",'ms':2},
{'args':[val[6],val[7]],'color':"red",'marker':"o",'ms':2}
])