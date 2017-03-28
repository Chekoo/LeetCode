#coding=utf-8
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].*/


class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i, num in enumerate(nums):
            if num not in check:
                check[target-num] = i
            else:
                return [check[num], i]

# enumerate可以用来遍历一个列表，即遍历索引又遍历元素。

