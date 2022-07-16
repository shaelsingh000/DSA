class Solution:
	def overlappedInterval(self, Interval):
            Intervals.sort()
            firstEle = Intervals[0][0]
            secondEle = Intervals[0][1]
            res = []
            for i in range(1, len(Intervals)):
                if Intervals[i][0] > secondEle:
                    res.append([firstEle, secondEle])
                    firstEle = Intervals[i][0]
                    secondEle = Intervals[i][1]
                else:
                    secondEle = max(secondEle, Intervals[i][1])
            res.append([firstEle, secondEle])
            return res
            


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
            n = int(input())
            a = list(map(int, input().strip().split()))
            Intervals = []
            j = 0
            for i in range(n):
                x = a[j]
                j += 1
                y = a[j]
                j += 1
                Intervals.append([x,y])
            obj = Solution()
            ans = obj.overlappedInterval(Intervals)
            for i in ans:
                for j in i:
                    print(j, end = " ")
            print()
# } Driver Code Ends