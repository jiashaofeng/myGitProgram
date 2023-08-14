# # -*- coding: UTF-8 -*-
# # def commonChars(A):
# # # “”"
# # # 该函数主要识别list中各元素相同的字符
# # # :param A: 给定的list
# # # :return: common_chars:相同字符的列表
# # # “”"
# #     lenth_li = len(A)
# #     lenth_li0 = len(A[0])
# #     common_li = []
# # ##方式一：通过遍历list中第一个元素每一个字符的方式
# # # 遍历第一个列表元素得每一个元素
# #     for x in range(0,lenth_li0):
# #         element = A[0][x]
# #         i = 1
# # # #将列表中每一元素与列表中没有元素进行比对
# #     for y in range(1,lenth_li):
# # # #具体比对列表中每一个元素中每一个字符
# #         for y1 in range(0,len(A[y])):
# #             if element == A[y][y1]:
# #                 i += 1
# #             if i == lenth_li:
# #                 common_li.append(A[y][y1])
# #                 A[y] = A[y][:y1] + A[y][y1 + 1:]
# #                 break
# #             else:
# #                 continue
# #     return common_li
# #
# # A=['hello','hehe']
# # print(commonChars(A))
# A=['hello','hi']
# def commonChars(A):
#     lenth_li = len(A)
#     lenth_li0 = len(A[0])
#     common_li = []
#     for x in range(0, lenth_li0):
#         i = 1
#     for y in range(1,lenth_li):
#         print(A[y])
#         print(A[y].find(A[0][x]))
#         result_find = A[y].find(A[0][x])
#         print(result_find)
#         # if result_find == -1:
#         #     break
#         else:
#             i += 1
#             A[y] = A[y].replace(A[0][x], '', 1)
#             if i == lenth_li:
#                 common_li.append(A[0][x])
#     return common_li
#
#
#
# print(commonChars(A))

import re

while True:
    try:
        string = input()
        lists = re.findall('\d+', string)
        lens = max([int(len(x)) for x in lists])
        for i in lists:
            if len(i) == lens:
                print(i, end='')
        print(','+str(lens))
    except:
        break

