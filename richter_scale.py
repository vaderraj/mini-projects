def richter_to_joule(r):
    return 10**(1.5*r + 4.8)

def richter_to_tnt(r):
    return  richter_to_joule(r)/4.184e9

r = float(input('Please enter a Richter scale value:'))
print('{:<}{:>4}'.format{'Richter scale value:', r})
