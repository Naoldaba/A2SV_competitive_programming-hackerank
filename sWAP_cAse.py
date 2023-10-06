def swap_case(s):
    new_str=""
    for i in s:
        if i.isupper():
            new_str+=i.lower()
        else:
            new_str+=i.upper()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
