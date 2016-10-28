from collections import OrderedDict

freq_dict = {'hey':5, 'go':23}

print sorted(freq_dict.items(), key=lambda t: t[1], reverse=True)
