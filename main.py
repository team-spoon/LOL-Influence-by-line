f = open('proNickname.txt', 'r')

print('[', end=' ')
while True:
    line = f.readline()
    if not line: break
    print("'"+line+"', ", end=' ')
print(']', end=' ')
f.close()