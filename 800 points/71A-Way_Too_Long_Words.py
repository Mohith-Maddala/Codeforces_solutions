#71A
#IN THE QUESTINO THEY WELL GIVE A STRING SO THAT I SHOULD CONVERT IT INTO NOTIATIONS 

'''
I GOT 2 IDEAS WHILE SOLVING FIRST USING LIST I WILL KEEP ALL MY RESULT AND GIVE THE LIST USING JOIN FUNCTION
AND THE 2ND ONE IS USING print and also the code should excute to abervation if and only if the string contains more than 10 charcters 
'''
#1st code 
number_of_lines = int(input())
for i in range(0,number_of_lines):
  word = input()
  first_letter = word[0]
  last_letter = word[-1]
  length_of_word = len(word)
  if length_of_word > 10:
    print(f"{first_letter}{length_of_word-2}{last_letter}")
  else:
    print(word)

#2nd code

number_of_lines = int(input())
for i in range(0,number_of_lines):
  word = input()
  empty_list = []
  first_letter = word[0]
  last_letter = word[-1]
  length_of_word = len(word)
  empty_list.append(first_letter)
  empty_list.append(last_letter)
  updated_length = length_of_word-2
  empty_list.append(updated_length)
  if length_of_word > 10:
    print("".join(empty_list)
  else:
    print(word)
