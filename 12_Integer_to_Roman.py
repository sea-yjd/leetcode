## 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
      ## solution1:
        # dictionary = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
        #             50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000:'M'}
        # num_split = []
        # num_new = {}
        # roman_new = {}
        # romannum = []
        # if num in dictionary:
        #     return dictionary[num]
        # else:
        #     while(num):
        #         p = num % 10
        #         num_split.append(p)
        #         num = int(num / 10)
        #     for i in range(len(num_split)):
        #         num_new[i] = int(num_split[i] * math.pow(10,i))
        #     for i in range(len(num_new)):
        #         roman_new[i] = []
        #         if num_new[i] in dictionary:
        #             roman_new[i] = dictionary[num_new[i]]
        #         elif num_new[i] == 0:
        #             roman_new[i] = []
        #         else:
        #         ##找区间
        #             left = 0
        #             j = 0
        #             while(num_new[i]):
        #                 if j == len(dictionary):
        #                     list(dictionary.keys())[j-1]
        #                 elif (list(dictionary.keys())[j] <= num_new[i] and list(dictionary.keys())[j] >= left):
        #                     left = list(dictionary.keys())[j]
        #                     j += 1
        #                     continue
        #                 roman_new[i].append(dictionary[left])
        #                 num_new[i] = num_new[i] - left
        #                 j = 0
        #                 left = 1
        #     j = len(roman_new)-1
        #     while(j >= 0):
        #         romannum += roman_new[j]
        #         j -= 1
        # return ''.join(romannum)
  ## solution2：
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC','L','XL','X','IX', 'V', 'IV', 'I']
        result = ''
        for i in range(0,len(values)):
            while num >= values[i]:
                num -= values[i]
                result += numbers[i]
        return result
S = Solution()
y = S.intToRoman(1997)
print(y)
