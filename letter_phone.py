phone_pad = {1: ['a', 'b', 'c'], 2: ['d', 'e', 'f']}


def phone_comb(phone_pad, current_index, result, key_pressed):
	if current_index < 0:
		print result
		return
	for each_key in phone_pad[key_pressed[current_index]]:
		phone_comb(phone_pad, current_index - 1, result + each_key, key_pressed)


key_pressed = [1, 2]

phone_comb(phone_pad, len(key_pressed) - 1, '', key_pressed)
