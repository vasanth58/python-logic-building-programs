'''print('*')'''

'''print('*')
print('*')'''

# rows=int(input('enter here:'))
# columns=int(input('enter here:'))
# for row in range(rows):
#     for column in range(columns):
#         print("*",end=' ')
#     print()




# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print( )           
# o/p
# * * * * * * 
# *         * 
# *         *
# *         *
# *         *
# * * * * * * 




# a=int(input( ))
# for i in range(a):
#     for j in range(a):
#         if i>=j:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
            
#     print( )
    

# output
# *       
# * *
# * * *
# * * * *




# a=int(input())
# for i in range(a):
#     for j in range (a):
    
#         if i<=j:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ') 
    #  print( )           
        
#         output
#         6
# * * * * * * 
#   * * * * *
#     * * * *
#       * * *  
#         * *
#           *





# a=int(input())
# for i in range(a):
#     for j in range (a):
    
#         if i+j>=a-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ') 
#     print( )   
    
#  output 
#     4
#       *
#     * * 
#   * * *
# * * * *





# a=int(input())
# for i in range(a):
#     for j in range (a):
    
#         if i+j<=a-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ') 
#     print( )   
    
#     output
#     4
# * * * * 
# * * *
# * *
# *





# output:
# here:5
# * * * * * 
# *       *
# *   *   *
# *       *
# * * * * *
# a=int(input('here:'))
# for i in range (a):
#     for j in range(a):
#         if i==0 or j==0 or j==a-1 or i==a-1 or (i==a//2 and j==a//2):
#                 print("*",end=' ')
#         else:
#             print(' ',end=' ') 
#     print( )   
    
    
    
    
    
# a=int(input())
# for row in range(a):
#     for column in range (a):
#         if row==a//2 or column==a//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')            
#     print( )        

# 5
#     *     
#     *
# * * * * *
#     *
#     *




# 
# output
#  5
# * * * * * 
# * *     *
# *   *   *
# *     * *
# * * * * *



# soet the list  value for assending order 


# l=[2,4,3,1,66,5,4,8,7,99,7]
# l.sort()
# print(l)

# output
# [1, 2, 3, 4, 4, 5, 7, 7, 8, 66, 99]

# l=[3,1,6]
# i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[j]<l[i]:
#             l[j],l[i]=l[i],l[j]
# print(l)            
# output:[1, 2, 3, 4, 4, 5, 7, 7, 8, 66, 99]


# find the missing number in list
# l = [1,2,3,4,6,7]
# n =l[-1]
# e= n*(n+1)//2
# a = sum(l)
# print(e- a)

# i=int(input())
# if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
# elif i % 3 == 0:
#         print("Fizz")
# elif i % 5 == 0:
#         print("Buzz")
# else:
#         print('not 3 and 5')
    
# s = "madam"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# x=[1,2,[3,4]]
# x.insert(1,25)
# print(x)

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print( )               



# l=[10,20,30,40]
# new_list=[]
# for i in l:
#     sum=0
#     for j in l :
#         if i!=j:
#             sum=sum+j
#     new_list.append(sum)
# print(new_list)       
    
    
    
    
# n=abs(int(input()))
# r=''
# while n!=0:

#     rem=n%2
#     r=str(rem)+r
#     n=n//2
# print(r)    

p=1
n=p%10
print(n)