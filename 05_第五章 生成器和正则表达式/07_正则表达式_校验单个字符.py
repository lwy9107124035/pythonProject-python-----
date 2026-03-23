

import re

# result = re.match('.it', 'ait')
# result = re.match('.it', '你it')
# result = re.match('.it', '你好it')

# result = re.match('\.it', 'ait')
# result = re.match('\.it', '.it')

result = re.match('[ahg]it', 'ait')
result = re.match('[ahg]it', 'hit')
result = re.match('[ahg]it', 'git')
result = re.match('[ahg]it', 'bit')
result = re.match('[ahg]it', 'a it')
result = re.match('[^ahg]it', 'rit')
result = re.match('[^ahg]it', 'ritdgaga')
result = re.search('[^ahg]it', 'fewgeritdgaga')

result = re.match('[a-z]it', '-it')




if result:  # 匹配成功
    print(result.group())  # 匹配到的内容
    print(result.span())  # 匹配到的内容的索引位置
else:  # 匹配失败
    print('匹配失败')