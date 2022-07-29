compass = ["north", "east", "south", "west"]
compassIn = input()
if compassIn == 'north':
  arah = 0
if compassIn == 'east':
  arah = 1
if compassIn == 'south':
  arah = 2
if compassIn == 'west':
  arah = 3
  
ke = input()
if ke == 'kanan':
  if arah+1 >= 4:
    print(compass[0])
  else:
    print(compass[arah+1])
if ke == 'kiri':
  print(compass[arah-1])