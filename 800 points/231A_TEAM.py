#231A.TEAM

'''
Here they 3 friends are going to the code contest and they decided they sohuld submit the solution if and only if 2 friends got the same answers 
'''
n = int(input)
count = 0
for i in range(0,n):
  input_score = intput()
  count_yes = input_score.count(1)
  if count_yes == 2:
    count = count +1
print(count)
