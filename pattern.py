'''
"""
*****
*****
*****
*****
*****
"""

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="")
        
    print("")
'''


'''
"""
*    
**   
***  
**** 
*****
"""
for i in range(1, 6):
    
    for j in range(1, 6):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")

    print("")
'''



'''
"""
     *
    **
   ***
  ****
 *****
"""

for i in range(1, 6):
    j = 5
    while j >= i:
        print(" ", end="")
        j -= 1

    for k in range(1, i+1):
        print("*", end="")
    print("")

'''




'''
"""
    *
   ***
  *****
 *******
*********
"""

for i in range(1, 6):

    j = 5
    while j > 1:
        print(" ",end="")
        j -= 1
'''





        
