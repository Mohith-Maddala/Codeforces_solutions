n = input()
list_n = []
for i in n:
  list_n.append(i)
for j in range(0,len(n)):
    if "+" in list_n:
        remove_plus = list_n.remove("+")
    else:
        pass
list_n.sort()
result = "+".join(list_n)
print(result)

    
