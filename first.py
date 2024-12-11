with open('input.txt', "r") as file:
  input = file.readlines()
#input = input.split('   ')
left_list = []
right_list = []
total = 0
for couples in input:
  couples = couples.replace('\n', '')
  input = couples.split('   ')
  left_list.append(int(input[0]))
  left_list.sort()
  right_list.append(int(input[1]))
  right_list.sort()
for i in range(len(left_list)):
  total += abs(left_list[i] - right_list[i])
print(total)
