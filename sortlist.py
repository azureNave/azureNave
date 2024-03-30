def merge(arr1,arr2):
    for i in range(0,len(arr1)-1):
        arr2.append(arr1[i])
    arr2.sort()
    

arr1 =[1,4,6,7]
arr2 =[2,5,3,8]
print(merge(arr1,arr2))