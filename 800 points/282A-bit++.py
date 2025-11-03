#282A Bit ++
'''
The first line contains a single integer n (1 ≤ n ≤ 150) — the number of statements in the programme.

Next n lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable x (denoted as letter «X»). Thus, there are no empty statements. The operation and the variable can be written in any order.
'''
n = int(input())
count = 0
for i in range(0,n):
  input_x = input()
  count_plus = input_x.count("+")
  count_minus = input_x.count("-")
  if count_plus == 2:
    count = count + 1
  elif count_minus == 2:
    count = count -1
print(count)
        
   
