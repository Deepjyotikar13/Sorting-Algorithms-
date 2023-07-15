def bubble_sort(arr):
  last_index=len(arr)
  for total in range(len(arr)):
        for ind in range(0,last_index-1):
        	if arr[ind]>arr[ind+1]:
        		arr[ind],arr[ind+1]=arr[ind+1],arr[ind]
        last_index-=1
  return arr
print(bubble_sort([10,2,45,0,100,0,67,800]))