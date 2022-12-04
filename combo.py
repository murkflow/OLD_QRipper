import re
def bruter(n):
    for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        #print(re.sub("[^0-1]","",str(list(map(int,list(s))))))
        combo=re.sub("[^0-1]","",str(list(map(int,list(s)))))
        with open('combolist.txt', 'a') as c:
            c.write(combo+'\n') 
bruter(65) # shorten to 3 for testing
print("Looks like it worked.")
