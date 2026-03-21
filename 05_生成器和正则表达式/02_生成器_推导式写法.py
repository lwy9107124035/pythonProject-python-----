
import sys

my_generator = (i for i in range(1,11))
print(type(my_generator))
print('-' * 23)

my_gt2 = (i for i in range(1,11) if i % 2 == 0)
print(type(my_gt2))
print('-' * 23)

print(next(my_gt2))
print(next(my_gt2))
print('=' * 23)
for i in my_gt2:
    print(i)

my_list = [i for i in range(1000_0000)]
my_gt3 = (i for i in range(1000_0000))
print(type(my_list), type(my_gt3))


print(f"my_list的内存占用: {sys.getsizeof(my_list)}")
print(f"my_gt3的内存占用: {sys.getsizeof(my_gt3)}")