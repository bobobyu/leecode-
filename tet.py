with open('e.txt','w+') as f:
    f.write(' '*100)

with open('e.txt','a+') as f:
    f.writelines('123')