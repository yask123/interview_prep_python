'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).


Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
[3,8]
[1,5] [5,10]

start_time = 1
end_time = 8
'''


def merge_intervals(intervals, new_interval):
	end_time = None
	start_time = None
	result = []
	for each_interval in intervals:
		if end_time != None and end_time >= each_interval[0]:
			end_time = max(end_time, each_interval[1])

		elif start_time == None and each_interval[1] >= new_interval[0]:

			start_time = min(each_interval[0], new_interval[0])
			end_time = max(each_interval[1], new_interval[1])

		elif start_time != None and end_time != None:
			result.append([start_time, end_time])
			result.append(each_interval)
			start_time = None
			end_time = None
		else:
			result.append(each_interval)

	if start_time != None:
		result.append([start_time, end_time])
	return result


intervals = [[1, 4], [8, 10]]
new_interval = [3, 9]

print merge_intervals(intervals, new_interval)
