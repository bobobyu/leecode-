import _pickle as pickle

with open('test.txt', 'w+') as f:
    f.write(' '*100)
with open('test.txt', 'a+') as f:
    f.seek(0,0)
    f.write('123')
with open('test.txt', 'a+') as f:
    f.seek(5, 0)
    f.write('4')
with open('test.txt', 'r+') as f:
    print(f.read())
