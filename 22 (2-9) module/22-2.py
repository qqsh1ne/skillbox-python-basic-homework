zen = open('zen.txt', 'r')
s = zen.read().splitlines()
zen.close()
print('\n'.join(s[::-1]))
