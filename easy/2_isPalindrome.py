"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x <= 9:
            return True
        str_x = str(x)
        str_len = len(str_x)
        num = 0
        if str_len % 2 == 0:
            num = int(str_len/2)
            if str_x[:num] == str_x[num:][::-1]:
                return True
            else:
                return False
        else:
            num = int(str_len/2)
            num2 = int(str_len/2+1)
            if str_x[:num] == str_x[num2:][::-1]:
                return True
            else:
                return False

    def isPalindrome2(self, x):
        """
        其实有最简单的写法
        """
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False

    def run(self):
        x = int(input('Input a num:'))
        print(self.isPalindrome(x))


if __name__ == '__main__':
    while 1:
        Solution().run()

