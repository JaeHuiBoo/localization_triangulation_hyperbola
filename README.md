# localization_triangulation_hyperbola

using acoustic sensors to detect the origin of the sound.
It is called triangulation. Using TDOA to draw 3 hyperbola and intersection of 3 hyperbola represents the origin of the sound.

input: r, m, n, t1, t2, t3 (it will be received from the sensors)
location of three sensors :(x1, y1), (x2, y2), (x3, y3)
 ==> (m-r, n+r/sqrt(3)), (m+r, n+r/sqrt(3)), (m, n-2*r/sqrt(3)) 
2r: the distance between two sensors
(m,n): the center of the triangle(made with sensors)
t1, t2, t3: TDOA between sensors  
v: the velocity of sound (343m/s)
