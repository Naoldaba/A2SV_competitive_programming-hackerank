if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        take_input=input().split(" ")
        if take_input[0]=="append":
            arr.append(int(take_input[1]))
        elif take_input[0]=="insert":
            arr.insert(int(take_input[1]),int(take_input[2]))
        elif take_input[0]=="remove":
            arr.remove(int(take_input[1]))
        elif take_input[0]=="print":
            print(arr)
        elif take_input[0]=="sort":
            arr.sort()
        elif take_input[0]=="pop":
            arr.pop()
        elif take_input[0]=="reverse":
            arr.reverse()
