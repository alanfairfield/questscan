#/usr/bin/python3
if __name__ == '__main__':
    print("enter the value for x")
    x = int(input())

    print("enter the value for y")
    y = int(input())

    print("enter the value for z")
    z = int(input())
    
    print("enter the value for n")
    n = int(input())
    
    result = [
        [i, j, k]
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1) 
        if i + j + k != n
        ]
    
    print(result)