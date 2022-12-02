def main():
    n = int(input()) # number of soldiers
    
    a = [int(i) for i in input().split()] # heights of soldiers
    max_height = max(a)
    min_height = min(a)

    max_height_index = a.index(max_height)
    min_height_index = a[::-1].index(min_height)
    
    count = max_height_index
    count += min_height_index
    if max_height_index > (len(a) - min_height_index - 1):
        count -= 1
    
    print(count)

if __name__ == '__main__':
    main()
    