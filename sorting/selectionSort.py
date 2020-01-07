# In short
# Select the minimum & sort
# i.e, select minimum & replace with the current element
# Algorithm complexity O(n^2) worst time, 


def selectionSort(box):
	for i in range(len(box)):
		mini = i
		for j in range(i+1, len(box)):
			if box[j] < box[mini]:
				mini = j
		temp = box[i]
		box[i] = box[mini]
		box[mini] = temp




arr = [29, 64, 73, 34, 20, -9, 23]
selectionSort(arr)
print(arr)