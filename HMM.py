
val1 = (1/3)
val2 = (1/2)
val3 = (val1*val2)

print("Alpha Array")
Alpha = [
     [(1), round(val3,3), round(pow(val3,2),4), round(pow(val3,3),4), round(pow(val3,4),5)],
     [round(val1,2), 
      round(((Alpha[1][0]*val2*val2) + (val3) + (Alpha[0][1]*val1)),3), 
      round(((Alpha[1][1]*val2*val2) + (Alpha[0][1] * val3) + (Alpha[0][2]*val1)),3),
      round(((Alpha[1][2]*val2*val2) + (Alpha[0][2] * val3) + (Alpha[0][3]*val1)),3),
      round(((Alpha[1][3]*val2*val2) + (Alpha[0][3] * val3) + (Alpha[0][4]*val1)),4),      
      ],
     [0, 
      round(Alpha[1][0] * pow(val2,2),3),
      round(Alpha[1][1] * pow(val2,2),3),
      round(Alpha[1][2] * pow(val2,2),3),
      round(Alpha[1][3] * pow(val2,2),5)
      ]
]
for x in Alpha:
  print(*x, sep=' ')
print("\nAlpha final value =", Alpha[2][4])
# print((Alpha[1][3]*val2*val2))
# print(Alpha[0][3] * val3)
# print((Alpha[0][4]*val1))

print("Beta Array")
Beta = [
        [round(((Beta[0][1] * val3) + (Beta[1][1] * val3) + (Beta[1][0] * val1)) ,4),
         round(((Beta[0][2] * val3) + (Beta[1][2] * val3) + (Beta[1][1] * val1)) ,4),
         round(((Beta[0][3] * val3) + (Beta[1][3] * val3) + (Beta[1][2] * val1)) ,4),
         round(((Beta[0][4] * val3) + (Beta[1][4] * val3) + (Beta[1][3] * val1)) ,4),
         0
         ],
        [round(Beta[1][1] * val2 * val2,4),
         round(Beta[1][2] * val2 * val2,4),
         round(Beta[1][3] * val2 * val2,4),
         round(val2*val2,3),
         0
         ],
        [0,0,0,0,1]
]
for x in Beta:
  print(*x, sep=' ')
print("\nBeta final value =", Beta[0][0])
# print(Beta[0][1] * val3)
# print(Beta[1][1] * val3)
# print(Beta[1][0] * val1)

print("Posterior Probablities")
horizontal1 = [
               round((Alpha[0][0]*Beta[0][1]*val3) / Beta[0][0],3), 
               round((Alpha[0][1]*Beta[0][2]*val3) / Beta[0][0],3),
               round((Alpha[0][2]*Beta[0][3]*val3) / Beta[0][0],3),
               round((Alpha[0][3]*Beta[0][4]*val3) / Beta[0][0],3)
               ]
print("Row 0 = ", horizontal1)

horizontal2 = [
               round((Alpha[1][0]*Beta[1][1]*val2*val2) / Beta[0][0],3),
               round((Alpha[1][1]*Beta[1][2]*val2*val2) / Beta[0][0],3),
               round((Alpha[1][2]*Beta[1][3]*val2*val2) / Beta[0][0],3),
               round((Alpha[1][3]*Beta[1][4]*val2*val2) / Beta[0][0],3)
               ]
print("Row 1 = ",horizontal2)

vertical = [
            round((Alpha[0][0]*Beta[1][0]*val1) / Beta[0][0],3),
            round((Alpha[0][1]*Beta[1][1]*val1) / Beta[0][0],3),
            round((Alpha[0][2]*Beta[1][2]*val1) / Beta[0][0],3),
            round((Alpha[0][3]*Beta[1][3]*val1) / Beta[0][0],3)
            ]
print("Columns = ",vertical)

diagonal = [
            round((Alpha[0][0]*Beta[1][1]*val3) / Beta[0][0],3),
            round((Alpha[0][1]*Beta[1][2]*val3) / Beta[0][0],3),
            round((Alpha[0][2]*Beta[1][3]*val3) / Beta[0][0],3),
            round((Alpha[0][3]*Beta[1][4]*val3) / Beta[0][0],3)
            ]
print("Diagonals = ",diagonal)

print("Compute Counts")
a1 = round(sum(horizontal1),3)
a2 = round(sum(diagonal),3)
a3 = round(sum(vertical),3)
a4 = round(sum(horizontal2),3)
a5 = 1
a1a = round(horizontal1[0] + horizontal1[2] + horizontal1[3], 3)
a1b = round(horizontal1[1], 3)
a2a = round(diagonal[0] + diagonal[2] + diagonal[3], 3)
a2b = round(diagonal[1], 3)
a4a = round(horizontal2[0] + horizontal2[2] + horizontal2[3], 3)
a4b = round(horizontal2[1], 3)
a5a = 1
a5b = 0
print("C(a1) =",a1, "\nC(a2)=",a2, "\nC(a3)=",a3, "\nC(a4)=",a4, "\nC(a5)=",a5, "\nC(a1,a)=",a1a, "\nC(a1,b)=",a1b, "\nC(a2,a)=",a2a, "\nC(a2,b)=",a2b, "\nC(a4,a)=",a4a, "\nC(a4,b)=",a4b, "\nC(a5,a)=",a5a, "\nC(a5,b)=",a5b)

print("Normalizing")
total_a123 = a1+a2+a3
total_a45 = a4+a5
total_a1ab = a1a+a1b
total_a2ab = a2a+a2b
total_a4ab = a4a+a4b
total_a5ab = a5a+a5b
a1 = round(a1 / (total_a123), 2)
a2 = round(a2 / (total_a123), 2)
a3 = round(a3 / (total_a123), 2)
a4 = round(a4 / (total_a45), 2)
a5 = round(a5 / (total_a45), 2)

a1a = round(a1a / (total_a1ab), 2)
a1b = round(a1b / (total_a1ab), 2)
a2a = round(a2a / (total_a2ab), 2)
a2b = round(a2b / (total_a2ab), 2)
a4a = round(a4a / (total_a4ab), 2)
a4b = round(a4b / (total_a4ab), 2)
a5a = round(a5a / (total_a5ab), 2)
a5b = round(a5b / (total_a5ab), 2)
print("a1 =",a1, "\na2=",a2, "\na3=",a3, "\na4=",a4, "\na5=",a5)
print("a1[a,b] = ", [a1a,a1b])
print("a2[a,b] = ", [a2a,a2b])
print("a4[a,b] = ", [a4a,a4b])
print("a5[a,b] = ", [a5a,a5b])