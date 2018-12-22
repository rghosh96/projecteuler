#builds every number in range 1000
first = [str(x) for x in range(1000)]
one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
twenty = 'twenty'
thirty = 'thirty'
fourty = 'fourty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
hundred = 'hundred'
an = 'and'
q = []
temp = ''
def gen(x, n):
    global q
    global temp
    if x[n] == '0':
        if x[0] == '0':
            pass
        else:
            if x[n - 1] == '1':
                temp += ten
            elif x[n - 1] == '2':
                temp += twenty
import num2word
ls = []
for i in range(1, 1001):
    ls.append(num2word.to_card(i))
total = 0
for i in ls:
    total += len(i)
    
