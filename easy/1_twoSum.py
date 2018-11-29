"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        第一次提交，提示超时 T_T
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                count = nums[i] + nums[j]
                if count == target:
                    return [i, j]

    def two_sum2(self, nums, target):
        """
        第二次提交, 1368ms
        """
        for i in range(len(nums)):
            flag = target - nums[i]
            if flag in nums:
                sec = nums.index(flag, 0, len(nums))
                if i == sec:
                    continue
                return [i, sec]

    def two_sum3(self, nums, target):
        """
        第三次提交，希望有好点的结果，哈哈哈哈 48ms

        """
        dic = dict(zip(nums, range(len(nums))))

        for i in range(len(nums)):
            flag = target - nums[i]
            if flag in dic and i != dic[flag]:
                return [i, dic[flag]]

    def run(self):
        nums = [2, 7, 11, 15]
        target = 9
        num = self.two_sum3(nums, target)
        print(num)


if __name__ == '__main__':
    Solution().run()
