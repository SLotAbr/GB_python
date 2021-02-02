n = int(input('Please, enter the number of seconds:\n'))
hh, mm, ss = n // 3600, (n // 60) % 60, n % 60
print('{:>02}:{:>02}:{:>02}'.format(hh, mm, ss))
