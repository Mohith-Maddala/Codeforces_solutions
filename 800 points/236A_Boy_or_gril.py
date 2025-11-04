n = input()
check_list = []
unique_list = []
for i in n:
  mohith = i
  check_list.append(mohith)
for j in n:
  unique_element = j
  if unique_element not in unique_list:
    unique_list.append(unique_element)
  else:
    pass
  
if unique_list == check_list:
    print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
