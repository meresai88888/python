n=int(input('enter n value')
for i in range(1,(n+1),1)
       for j in range(n-i)
              print("  ",end=' ')
      for j in range(n-1)
              print(j,end=' ')
      for j in range((i-1),0,-1):
              print(j,end=" ")
      print(' ')
