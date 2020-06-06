#%%
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums)/2)]
#%%
Solution().majorityElement([1,2,3,3])
# %%
divmod(1,10)
# %%
class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        n = N
        s = 0
        while N:
            N, tmp = divmod(N, 10)
            s += tmp ** k
        return s == n
# %%
Solution().isArmstrong(153)

# %%
for i in range(1000):
    if Solution().isArmstrong(i) == True:
        print(i)

# %%
def amst(num):  
    s = 0
    k = len(str(num))
    N = num
    for i in range(len(str(num))):
        num1 = num % 10
        s += num1 ** k
        num2 = num // 10
        num = num2
    if s == N:
        print(N)
    else:
        print(N,' is not a amst number')

# %%
amst(1634)
# %%
import os
dir_name = '煎蛋IMG'
get_path = os.getcwd()
path_dir = get_path + "\\" + dir_name

# %%
not os.path.isdir(path_dir)

# %%
if not os.path.isdir(path_dir):
            print(f"创建煎{dir_name}文件夹成功")
            os.mkdir(path_dir)
        else:
            print(f"{dir_name}G文件夹已存在创建失败")