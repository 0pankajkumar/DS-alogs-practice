# Bubble sort
# Largest items bubbles out at the last with each iteration


def bubbleSort(box):
	for e in range(len(box)):
		for i in range(len(box)):
			if i+1 < len(box):
				if box[i] > box[i+1]:
					temp = box[i]
					box[i] = box[i+1]
					box[i+1] = temp



arr = [29, 64, 73, 34, 20, -9, 23]
bubbleSort(arr)
print(arr)