'''
Python 3.8.10
给你一个数num，判断是不是素数 
'''

#输入：需要检查的数
#返回：
# false : 非素数
# true  : 素数
def pd(n):
    if n<2:
        return None
    

    for x in range(2,n):
        if n%x==0: 
            return False

    return True


#num=5
for num in range(100):
    print(num,":",pd(num))
