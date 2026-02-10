# write a python program to remove duplicate character form the string

# s='programming'
# res=' '
# for i in s:
#     if i not in res:
#         res+=i
# print(res)        
        
        
        
# write a python program to print lorgest sub string in the original string

        
# v="i love you subasri"
# n_v=v.split()
# lorgest=n_v[0]
# for i in n_v:
#     if len(i)>len(lorgest):
#         lorgest=i
# print(lorgest)

# write a python program to count no.of consonant and vowels present in string

# s='education$#$%'
# v_c=0
# c_c=0
# for i in s:
#     if 'a'<=i and i<='z' or 'A'<=i and i<='Z' :
#         if i in 'aeiouAEIOU':
#             v_c+=1
#         else:
#             c_c+=1
# print(v_c)
# print(c_c)            



# write  the python to check the given two string are anagram are not
  
a=input("enter the str:")
b=input("enter the str:")
if sorted(a)==sorted(b):
    print('anagrem')
else:
    print("not anagrem")