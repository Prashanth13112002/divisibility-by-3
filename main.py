class solution:
    def divisible_by3(self,arr):
        s=0
        for i in arr:
            s+=i
        if(s%3==0):
            return 1
        else:
            return 0
a1=solution()
a=list(map(int,input().split()))
print(a1.divisible_by3(a))