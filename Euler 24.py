#lexicographical permutations
string = '0123456789'
a = []
count = ''
temp = []
temp1 = []

count = ''
for i in string:
    temp.append(i)
def p():
    global temp
    global temp1
    for i in temp:
        for k in string:
            if k not in i:
                temp1.append(i + k)
    temp = temp1
    temp1 = []





        
    
