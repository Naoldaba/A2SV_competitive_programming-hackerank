  //Function to sort the array using selection sort algorithm.
  selectionSort(arr,n){
   //code here
   for(let i=0;i<arr.length;i++){
        for(let j=0;j<arr.length;j++){
            if(arr[i]<arr[j]){
                let temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            }
        }
    }
    return arr
  }
