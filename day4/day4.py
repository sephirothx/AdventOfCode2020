import re

inp = open('input.txt').read().strip()
passports = inp.split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

sol1 = 0
sol2 = 0
for p in passports:
    count = 0
    for f in fields:
        if f not in p:
            break
    else:
        sol1 += 1
        p_fields = p.split()
        valid = True
        for f in p_fields:
            n, v = f.split(':')
            if n == 'byr' and not (re.match(r'^\d{4}$', v) and 1920 <= int(v) <= 2002) or \
            n == 'iyr' and not (re.match(r'^\d{4}$', v) and 2010 <= int(v) <= 2020) or \
            n == 'eyr' and not (re.match(r'^\d{4}$', v) and 2020 <= int(v) <= 2030) or \
            n == 'hgt' and not ((re.match(r'^\d+cm$', v) and 150 <= int(v[:-2]) <= 193) or
                                (re.match(r'^\d+in$', v) and 59 <= int(v[:-2]) <= 76)) or \
            n == 'hcl' and not (re.match(r'^#[0-9a-f]{6}$', v)) or \
            n == 'ecl' and v not in ecl or \
            n == 'pid' and not (re.match(r'^\d{9}$', v)):
                valid = False
        if valid:
            sol2 += 1

print(sol1)
print(sol2)
