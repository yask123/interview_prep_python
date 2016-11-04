from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

a = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

print a

d['aaa'] = 1

print a
