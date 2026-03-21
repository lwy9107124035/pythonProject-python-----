
import math

def dataset_loader(batch_size):
    with open("./05_生成器和正则表达式/data/jaychou_lyrics.txt", "r", encoding="utf-8") as src_f:
        lines = src_f.readlines()
        # lines = [line.strip() for line in src_f.readlines()]
        total_batch = math.ceil(len(lines) / batch_size)

        for idx in range(total_batch):
            yield lines[idx*batch_size: idx*batch_size + batch_size]


dl = dataset_loader(61)
print(next(dl))
print(next(dl))
print(next(dl))
print(next(dl))
print(next(dl))
print(next(dl))
print(next(dl))
  

