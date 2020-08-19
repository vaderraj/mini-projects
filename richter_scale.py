def richter_to_joule(r):
    return 10**(1.5*r + 4.8)

def richter_to_tnt(r):
    return  richter_to_joule(r)/4.184e9

arr = []
arr.append(['Richter', 'Joules', 'TNT'])
for i in (1, 5, 9.1, 9.2, 9.5):
    arr.append([str(i), str(richter_to_joule(i)), str(richter_to_tnt(i))])
col_width = max(len(word) for row in arr for word in row) + 2
for row in arr:
    print(''.join(word.ljust(col_width) for word in row))
r = float(input('Please enter a Richter scale value:'))
print('Richter scale value: ' + str(r))
print('Equivalence in joules: ' + str(richter_to_joule(r)))
print('Equivalence in tons of TNT: ' + str(richter_to_tnt(r)))
