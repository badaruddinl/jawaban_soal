#Deret: 1 1 2 3 5 8 13 21 34 55 89
#Index: 0 1 2 3 4 5 6 7 8 9 10
all_index = 10
def fibonnaci(all_index):
    first = 0
    second = 1
    print(first + second)
    for x in range(all_index):
      now = first+second
      print(now)
      first = second
      second = now