import numpy as np
L=int(input("specify the length of the beam:"))   #length of the beam in meters
W=float(input("specify intensity of the uniformly distributed load:"))  #intensity of load in kN/m


#QUESTION 1a
x= [0,12]
Moment_at_ends = []
Shearforce_at_ends=[]
for i in x:
    M=(W*(-6*i**2 + 6*L*i - L**2))/12    #bending moment equation
    Moment_at_ends.append(M)
    V=W*((L/2) - i) #shear force equation
    Shearforce_at_ends.append(V)
print(f"The bending moments at the ends are {Moment_at_ends}kNm")
print(f"The shear forces at the ends are {Shearforce_at_ends}kN")


#QUESTION 1b
'MO =x**2 -12*x + 24'     #expression for bending moment = 0
point_of_contraflexure1 = 6 - np.sqrt(12)
point_of_contraflexure2 = 6 + np.sqrt(12)
print(f"The first point of the contraflexure is {point_of_contraflexure1}m")
print(f"The second point of the contraflexure is {point_of_contraflexure2}m")

#QUESTION 1c
'VO = L/2 - x'  #expression for shear force = 0
distance_of_shear_force_is_zero = L/2
print(f"The distance at which the shaer force is zero is {distance_of_shear_force_is_zero}m")

#QUEstion 1d and 1e
BendingAtPoint = []
ShearForceAtPoint = []
b = np.arange(0,12.01,0.01)     #span of beam in steps of 10mm
for i in b:
    BM = (W*(-6*i**2 + 6*L*i - L**2))/12   #bending moment of each point of the span in steps of 10mm
    SF = W*((L/2)-i)        #shear force of each point of the span in steps of 10mm
    BendingAtPoint.append(BM)
    ShearForceAtPoint.append(SF)
print(f"The bending moments at each point of 10mm are {BendingAtPoint}kNm")
print(f"The shear forces at each point of 10mm are {ShearForceAtPoint}KNm")

#QUESTION 1f
BM = (W*(-6*b**2 + 6*L*b - L**2))/12      #bending moment of each point of the span in steps of 10mm
SF = W*((L/2)-b)    #shear force of each point of the span in steps of 10mm
D = abs(BM)       #absolute values for bending moment at each point in the beam at steps of 10mm
d = min(D)       #the mininum absolute bending moment at each point in the beam at steps of 10mm
X1 = 6 - np.sqrt(12-(1/30*d))   #first point where the absolute value of the bending moment is minimum
X2 = 6 + np.sqrt(12-(1/30*d))   #second point where the absolute value of the bending moment is minimum 
print(f"first point along L where bending moment is minimum is minimum is {X1}")
print(f"second point along L where bending moment is minimum is minimum is {X2}")

#QUESTION 1g
#relative error = ((X - point of contraflexure)/X)*100%
relative_error1 = ((point_of_contraflexure1 - X1)/point_of_contraflexure1)*100
relative_error2 = ((X2 - point_of_contraflexure2)/X2)*100
print(f"First relative error ={relative_error1}%")
print(f"Second relative error = {relative_error2}%")

#QUESTION 1h
#maximum bending moment occurs at a point where the shear force = 0
#maxinum bending moment occurs at the supports

print(f"Point where bending moment is maxinum is {b[600]}m")    #point where the bending moment is maximum
print(f"First point where bending moment is mininum is {b[0]}m")   #first point where the bending moment is minimum
print(f"Second point where the bending moment is minimum is {b[1200]}m")  #second point where the bending moment is minimum




#GITHUB LINK: https://github.com/RoseKufia