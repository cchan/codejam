import sys
from collections import defaultdict

T, N = map(int, input().split(' '))

for asdf in range(T):
    history = list()
    
    print('AAAAA')
    prev = 'AAAAA'
    sys.stdout.flush()
    resultants = defaultdict(set)
    
    for _ in range(45):
      word = input()
      
      if word == "-1":
          raise "OopsException"
      
      resultants[prev].add(word)
      if len(resultants[prev]) == 1:
          print(prev)
          prev = prev
      else:
          print(word)
          prev = word
      sys.stdout.flush()
    
    word = input() # ignore
    
    biggest_or_smallest = list(resultants[prev])[0]
    for _ in range(4):
      print(biggest_or_smallest)
      sys.stdout.flush()
      resultants[biggest_or_smallest].add(input())
    
    print(biggest_or_smallest) # ignore
    
    if len(resultants[biggest_or_smallest]) == 1:
      biggest = biggest_or_smallest
      smallest = list(resultants[biggest_or_smallest])[0]
    else:
      biggest = prev
      smallest = biggest_or_smallest
    # actually it could also be 2ndbiggest, biggest
    
    other = 'AAAAA'
    if smallest == other or biggest == other:
      other = 'BBBBB'
    if smallest == other or biggest == other:
      other = 'CCCCC'
    
    for _ in range(50):
      word = input()
      if word == "-1":
          raise "OopsException"
      if word == biggest:
        print(smallest)
        #with open('asdf.txt', 'a') as f:
        #  f.write(smallest + ' ')
      elif word == smallest:
        print(other)
        #with open('asdf.txt', 'a') as f:
        #  f.write(other + ' ')
      else:
        print(biggest)
        #with open('asdf.txt', 'a') as f:
        #  f.write(biggest + ' ')
      sys.stdout.flush()
    #with open('asdf.txt', 'a') as f:
    #  f.write('\n')
