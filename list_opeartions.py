courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# print(courses[0]), print(courses[3])              #index item
# print(courses[1])
# print(courses[0:3])                                #range

# courses.append('Art')                             #append
# print(courses)

# courses.insert(0,'Geography')                     # insert value at particular index
# courses.insert(3,'Geography1')
# print(courses)

# courses_2 = ['Marathi', 'Hindi', 'English']
# courses.insert(0,courses_2)                         # inserting another list in existing list at index
# print(courses)

# courses_2 = ['Marathi', 'Hindi', 'English']
# courses.extend(courses_2)                         # inserting another list in existing list at LAST
# print(courses)

# courses.remove('Math')                            #remove
# print(courses)

# popped = courses.pop()                              # used for remove last item in list
# print(popped)
# print(courses)

# courses.reverse()                   # reverse the list
# print(courses)

# courses.sort()                      # sorting the list
# print(courses)

# courses.sort(reverse=True)            # sorting reverse
# print(courses)

# nums = [1, 3,5,2 ,5,6]
# print(min(nums))                # minimum
# print(max(nums))                # maximum
# print(sum(nums))                # sum

# print('CompSci' in courses)
# print('marathi' in courses)

# for items in courses:           # print list using loop
#     print(items)
#
# for index, course in enumerate(courses):            # print list with no's
#     print(index,course)
#
# for index, course in enumerate(courses,start=1):   # print list with no's and start point
#     print(index, course)

# courses_str1 = ','.join(courses)
# print(courses_str1)
# courses_str2 = '-'.join(courses)
# print(courses_str2)

########## lists            ( list use square brackets )
# num1 = [1,2,3,4,3]
# num2 = num1
# print(num1)
# print(num2)
# num1[0] = 8
# print(num1)
# print(num2)

########## tupel            ( tupel used simple brackets )
# num1 = (1,2,3,4,3)
# num2 = num1
# print(num1)
# print(num2)
# num1[0] = 8
# print(num1)
# print(num2)


########## sets            ( tupel used curlu brackets )
# num1 = {1,2,3,4,3}
# num2 = num1
# print(num1)
# print(num2)
# num1[0] = 8
# print(num1)
# print(num2)