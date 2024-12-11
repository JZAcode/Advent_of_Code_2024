from first import right_list, left_list
total = 0
for e in left_list:
  repetitions = 0
  for i in right_list:
    if e == i:
      repetitions += 1
  total += e*repetitions
print(total)
