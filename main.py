# Exercise 1

# Using the given list, print out a filtered version of the list with only the numbers that are less than ten 10
alist = [1,11,14,5,8,9]
filtred_list=[]
for num in alist:
   if num<10:
     filtred_list.append(num)
print(filtred_list)




# Exercise 2


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
merged_list= l_1 + l_2
print(merged_list)

# Exercise 3

# Square every number from 1 to 15
for i in range(1,16):
  square=i**2
  
  print(square,end=" ")
print("\n")


# Exercise 4
names_list = ['  amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
filtred_list = [x.strip().title() for x in names_list if x.strip().title().startswith('A')]

print(filtred_list)
        
    

# Exercise 5
# Print all Prime numbers from 1 to 100

for i in range(2,101):
    
    for j in range(2,i):
        if i%j==0:
            break
    else :
        print(i,end=" ")