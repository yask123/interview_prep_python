def read_file(file_path):
	output_string = []
	with open(file_path, 'r') as out_file:
		for each_line in out_file:
			output_string.append(each_line)
	return output_string


output_string = read_file('test.csv')


def conver_to_dict(string, file_dict={}):
	for each_line in output_string[1:]:
		name, age = each_line.split(",")
		name = name[1:-1]
		age = int(age[2:-2])
		file_dict[name] = age


my_dic = {}
