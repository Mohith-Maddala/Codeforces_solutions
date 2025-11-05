n = input()
list_n = []
for i in n:
    list_n.append(i)
result = list_n[0].upper()
replace_lower = n.replace(list_n[0],result)
print(replace_lower)
