nums = [1,2,3,4,5]
print(nums)        #[1, 2, 3, 4, 5]
print(nums[4])     # 5
print(nums[2:])    #[3, 4, 5]
print(nums[-1])    #5

names = ['Pallavi','Madhu','Aarushi']
print(names)        #['Pallavi', 'Madhu', 'Aarushi']

values = [9.5,'Pallavi',25]
print(values)       #[9.5, 'Pallavi', 25]

mil = [nums,names]
print(mil)      #[[1, 2, 3, 4, 5], ['Pallavi', 'Madhu', 'Aarushi']]

nums.append(45) #append will add the value at end of array
print(nums)     #[1, 2, 3, 4, 5, 45]

nums.insert(2,77) #insert will add the value in the middle of the array
print(nums)     #[1, 2, 77, 3, 4, 5, 45]

#to delete the value from list using index value needs to use pop
nums.pop(1)
print(nums)     #[1, 77, 3, 4, 5, 45]

nums.pop()      # removes the last element of the list
print(nums)     #[1, 77, 3, 4, 5]

del nums[2:]
print(nums)     #[1, 77]

nums.extend([10,12,13,14,15])
print(nums)     #[1, 77, 10, 12, 13, 14, 15]

num1 = [1,1]
print(num1)     #[1, 1]

var1 = 'Telusko'
print(var1[-3])  #s