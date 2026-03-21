"""
需求:
    问1, 2, 3, 4能组合成的四位数有几种情况, 按照5个一行输出.
要求:
    1. 要求同时包含1, 2, 3, 4这四个数字.
        1234, 1324均可
        1122, 1123不行
    2. 要求数字1和3不能挨着.
        1324, 3124不行
        1234, 3412可以
    3. 数字4不能开头.
    4. 5行以内搞定(包括5行)
"""

# 思路: 把数字 -> 字符串, 然后调用字符串的功能作判断, 即可.
# count = 0
# for s in [str(i) for i in range(1234, 4322)]:
#     if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4':
#         count += 1
#         print(s, end='\n' if count % 5 == 0 else '\t')

print([int(s) for s in [str(i) for i in range(1234, 4322)] if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4'])


# 需求: 已知列表: my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd'], 删除所有的bb元素, 尽可能多的用不同的解决方案.
# my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']
# new_list = [s for s in my_list if s != 'bb']
# print(new_list)

my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']
for s in my_list[:]:
    if s == 'bb':
        my_list.remove(s)
print(my_list)