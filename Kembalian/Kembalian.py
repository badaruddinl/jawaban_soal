def checking1k(input1):
  if input1 % 1000 != 0:
    return 0
  return 1

def checking100k(input2):
  if input2 % 100000 != 0:
    return 0
  return 1
def checkingSecondGreaterOne(input1,input2):
  if input2 < input1 :
    return 0
  return 1

def problemSolution(input1,input2):
  check = checking1k(input1)
  if check == 0:
    print("Tidak Valid")
    return 0
  check = checking100k(input2)
  if check == 0 :
    print("Tidak Valid")
    return 0
  check = checkingSecondGreaterOne(input1,input2)
  if check == 0 :
    print("Tidak Valid")
    return 0
  kembalian = input2-input1
  arr = []
  while (kembalian-100000 >= 0):
    kembalian = kembalian-100000
    if kembalian < 0:
      kembalian = kembalian + 100000
      break
    arr.append(100000)
    if kembalian == 0 :
      break
  while (kembalian-50000 >= 0):
    kembalian = kembalian-50000
    if kembalian < 0:
      kembalian = kembalian + 50000
      break
    arr.append(50000)
          
    if kembalian == 0  or kembalian < 0:
      break
  while (kembalian-20000 >= 0):
    kembalian = kembalian-20000
    if kembalian < 0:
      kembalian = kembalian + 20000
      break
    arr.append(20000)
    if kembalian == 0  or kembalian < 0:
      break
  while (kembalian-5000 >= 0):
    kembalian = kembalian-5000
    if kembalian < 0:
      kembalian = kembalian + 5000
      break
    arr.append(5000)
    if kembalian == 0  or kembalian < 0:
      break
  while (kembalian-1000 >= 0):
    kembalian = kembalian-1000
    if kembalian < 0:
      kembalian = kembalian + 1000
      break
    arr.append(1000)
    if kembalian == 0  or kembalian < 0:
      break
  print(arr)

problemSolution(input1, input2)