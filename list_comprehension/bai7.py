hesogoc = lambda x1,y1 ,x2,y2 : (y2-y1) / (x2 -x1)
tungdogoc = lambda x,y,a : y - a*x

a = hesogoc(1,2,3,4)
b = tungdogoc(1,2,a)
print(a)
print(b)