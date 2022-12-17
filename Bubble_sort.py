def countSwaps(a):
    # Write your code here
    num_swaps=0
    sorted=False
    while sorted is False:
        sorted=True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                num_swaps+=1
                sorted=False
    print("Array is sorted in",num_swaps,"swaps.")
    print('First Element:',a[0])
    print('Last Element:',a[len(a)-1])
