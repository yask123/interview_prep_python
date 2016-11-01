processes = [[], [0], [0], [1, 2], [3]]


def topological_sort(processes):
	perm_marks = set()
	temp_marks = set()
	results = []

	for i in range(len(processes)):
		if i not in perm_marks:
			visit_all_dfs(i, processes, perm_marks, temp_marks, results)

	return results


def visit_all_dfs(current_process, processes, perm_marks, temp_marks, results):
	if current_process in temp_marks:
		raise Exception("Cycle in the graph")

	if current_process not in perm_marks:
		temp_marks.add(current_process)
		for each in processes[current_process]:
			visit_all_dfs(each, processes, perm_marks, temp_marks, results)

		temp_marks.remove(current_process)
		perm_marks.add(current_process)
		results.append(current_process)


print topological_sort(processes)
