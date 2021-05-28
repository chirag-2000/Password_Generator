import string
import random

plen=int(input("Enter password length :"))

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits  
s4=string.punctuation

s=[]

s.extend(list(s1)) #before appending type cast string to list 
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# print(s)
random.shuffle(s)
# print(s)
pasword="" #empty string

print(pasword.join(s[0:plen]))



