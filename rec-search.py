def rec_search(numb, n):
  if numb in n:
    return True

num_list = list(range(1000))
try:
  entry = int(input("Enter an integer: "))
except:
  pass

flag = rec_search(entry, num_list)
if flag:
  print("found")
else:
  print("Not Found")