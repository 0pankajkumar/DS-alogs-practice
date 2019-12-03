# 20, 29, 34, 73, 14

def insertionSort(box):
	for i in range(len(box)):
		if i-1 >= 0:
			j = i
			while box[j] < box[j-1]:
				if j-1 >= 0:
					temp = box[j]
					box[j] = box[j-1]
					box[j-1] = temp
					j -= 1
				else:
					break
		else:
			print("corner")
		print(box)


arr = [29, 64, 73, 34, 20, -9, 23]
insertionSort(arr)
# print(arr)