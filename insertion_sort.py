def insertionSort1(n, arr):
    # Write your code here
    q=n-1
    li=[]
    li.extend(arr)
    x=arr[n-1]
    for j in range(n-2,-1,-1):
        arr.clear()
        arr.extend(li)
        arr.pop()
        if x<arr[j]:
            arr.insert(j+1,arr[j])
        elif x>arr[j]:
            arr.insert(j+1,x)
            for m in arr:
                print(m, end=" ")
            print()
            break
        for m in arr:
            print(m,end=" ")
        print()
    arr.clear()
    arr.extend(li)
    arr.pop()
    if x < arr[0]:
        arr.insert(0, x)
        for m in arr:
            print(m,end=" ")
