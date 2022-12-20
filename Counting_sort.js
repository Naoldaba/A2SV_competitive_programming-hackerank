function countingSort(arr) {
    // Write your code here
    let list=[]
    let counter=0
    for(let j=0;j<100;j++){
        counter=0
        for(let i=0;i<arr.length;i++){
             if(j==arr[i]){
               counter++
            }
        }
        list.push(counter)  
    }
    return list
}
