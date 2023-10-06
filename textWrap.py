def wrap(string, max_width):
    new_str=""
    for i in range(0,len(string),max_width):
        if i+max_width<=len(string):
            new_str+=string[i:i+max_width]+"\n"
        else:
            new_str+=string[i:]
    return new_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
