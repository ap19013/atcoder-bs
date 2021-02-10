s = input()
token = s.split()
b = int(token[0])
c = int(token[1])

sx=b*c
if sx%2==0:
    print('Even')
else:
    print('Odd')