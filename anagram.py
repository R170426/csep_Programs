a=str(input("Enter the input str1:"))
b=str(input("Enter the input str2:"))
str2_dict={}
str1_dict={}
for i in a:
    print(i)
    r=l.count(i)
    print(r)
    if i not in str1_dict:
        str1_dict[i]=r
for j in b:
    s=m.count(j)
    if j not in str2_dict:
        str2_dict[j]=s
print(str1_dict)
print(str2_dict)
if str1_dict.items()==str2_dict.items():
    print("It is an anagram")
else:
    print("not anagram")
