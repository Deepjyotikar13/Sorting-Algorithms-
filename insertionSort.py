def Insertion_sort(arr):
	if len(arr)<=1:
		return arr
	else:
		for ind in range(1,len(arr)):
			current=arr[ind]
			pre_ind=ind-1
			while pre_ind>=0 and current<arr[pre_ind]:
				arr[pre_ind+1]=arr[pre_ind]
				pre_ind-=1
				print(arr)
			arr[pre_ind+1]=current
		return arr
print(Insertion_sort([5,3,4,1]))