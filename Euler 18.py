#finds largest possible sum of triangle path
string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
count = 0
count1 = 0
count2 = 1
count3 = 1
list_ = [[]] * 15
string = string.split()
s = []
for i in string:
    if i[0] == '0':
        s.append(i.strip('0'))
    else:
        s.append(i)
for i in range(15):
    list_[count] = s[count1:count2]
    count += 1
    count3 += 1
    count1 = count2
    count2 = count1 + count3
list_ = list_[::-1]
g = []
for i in list_[0]:
    g.append(eval(i))
list_[0] = g
del g
temp = list_[0]
temp1 = []
for i in list_:
    count = 0
    temp1 = []
    if i == list_[0]:
        pass
    else:
        for k in i:
            y = eval(k)
            q = y + temp[count]
            w = y + temp[count + 1]
            print(y)
            print(q)
            print(w)
            if q > w:
                temp1.append(q)
            else:
                temp1.append(w)
            count += 1
            print(count)
        temp = temp1
            
            
            
            

    
    

