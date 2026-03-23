


import re

s = '开心你就大声笑，哈哈，呵呵，嘿嘿，嘻嘻，桀桀桀，啦啦啦'

result = re.compile('哈|呵|嘿|嘻|桀').sub('♥', s)

print(result)
print('-' * 23)

result = re.sub('哈|呵|嘿|嘻|桀', '♥@', s)
print(result)