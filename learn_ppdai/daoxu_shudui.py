# -*- coding:utf-8 -*-
class Solution:
    def merge_sort(self, collection):
        length = len(collection)
        left_count = 0
        right_count = 0
        count = 0
        if length > 1:
            midpoint = length // 2
            left_half, left_count = self.merge_sort(collection[:midpoint])
            right_half, right_count = self.merge_sort(collection[midpoint:])
            i = 0
            j = 0
            k = 0

            left_length = len(left_half)
            right_length = len(right_half)
            while i < left_length and j < right_length:
                if left_half[i] < right_half[j]:
                    collection[k] = left_half[i]
                    i += 1
                else:
                    collection[k] = right_half[j]
                    j += 1
                    count += len(left_half[i:])
                k += 1

            while i < left_length:
                collection[k] = left_half[i]
                i += 1
                k += 1
            while j < right_length:
                collection[k] = right_half[j]
                j += 1
                k += 1

        return collection, (left_count + right_count + count) % 1000000007

    def InversePairs(self, data):
        # write code here
        _, count = self.merge_sort(data)
        return count


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    # data = [8,1,2,3,4,5,6,7,0]
    # result 2519
    data = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460,
            505, 360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474,
            162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697,
            478, 147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64,
            266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
    print(Solution().InversePairs(data))
