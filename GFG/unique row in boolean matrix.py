#User function Template for python3

def uniqueRow(row, col, matrix):
    result = []
    for i in range(0, row*col, col):
        bool_value = matrix[i:i+col]
        if bool_value not in result:
            result.append(bool_value)
    return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = input().split()
        
        a = uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends