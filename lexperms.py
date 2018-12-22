from itertools import permutations

string = [3,1,2,4]

string = sorted(string)
print(list((permutations(string, r=None))))
