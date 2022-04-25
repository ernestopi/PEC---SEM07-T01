def maior(n1,n2,n3,n4,n5):
    max = n1
    if n2 > max and max > n3 and n3 > n4 and n4 > n5:
        max = n2
    else:
        if n3 > max and max > n2 and n2 > n4 and n4 > n5:
            max = n3
        else:
            if n4 > max and max > n2 and n2 > n5:
                max = n4
            else:
                if n5 > max and max > n2 and n2 > n3 and n3 > n4:
                    max = n5
                else:
                    max = 1
    return max

def menor(n1,n2,n3,n4,n5):
    min = n1
    if n2 < max and max < n3 and n3 < n4 and n4 < n5:
        min = n2
    else:
        if n3 < max and max < n2 and n2 < n4 and n4 < n5:
            min = n3
        else:
            if n4 < max and max < n2 and n2 < n5:
                min = n4
            else:
                if n5 < max and max < n2 and n2 < n3 and n3 < n4:
                    min = n5
                else:
                    min = 1
    return min

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    print(max(n1,n2,n3,n4,n5))
    print(min(n1,n2,n3,n4,n5))

if __name__ == '__main__':
    main()