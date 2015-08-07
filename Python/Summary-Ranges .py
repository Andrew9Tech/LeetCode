




class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) <= 0:  return []
        if len(nums) == 1:  return [str(nums[0])]
        start = temp = nums[0];
        count = 1; result = []
        for item in nums[1:]:
            if item == (temp + 1):
                count, temp= count + 1, item
                if (item == nums[-1]):
                    result.append(str(start) + '->' + str(item))
            elif (count > 1):
                result.append(str(start) + '->' + str(temp))
                temp = start = item; count = 1
                if (item == nums[-1]):
                    result.append( str(item))
            elif (count == 1):
                result.append(str(temp))
                start = temp = item
                count = 1
                if (item == nums[-1]):
                    result.append( str(item))
        return result
