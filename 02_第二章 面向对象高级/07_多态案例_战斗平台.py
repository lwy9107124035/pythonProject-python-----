"""
案例: 演示Python的多态案例之 战斗平台.

需求:
    1. 构建对战平台(公共的函数) object_play(), 接收: 英雄机 和 敌机.
    2. 在不修改对战平台的情况下, 完成多次战斗.
    3. 规则:
        英雄机, 1代战斗机力60, 2代战斗力80
        敌机, 1代战斗力70

代码提示:
    英雄机1代 HeroFrighter
    英雄机2代 AdvHeroFrighter
    敌机      EnemyFrighter
"""

# 1. 定义英雄机1代, 战斗力 60
class HeroFrighter:
    def power(self):
        return 60

# 2. 定义英雄机2代, 战斗力 80
class AdvHeroFrighter(HeroFrighter):
    def power(self):
        return 80

# 3. 敌机1代
class EnemyFrighter:
    def power(self):
        return 70

# 4. 构建对战平台, 公共的函数, 接收不同的参数, 有不同的效果 -> 多态.
# def object_play(hero: HeroFrighter, enemy: EnemyFrighter):
def object_play(hero, enemy):
    # 参1: 英雄机, 参2: 敌机
    if hero.power() >= enemy.power():
        print('英雄机 战胜 敌机!')
    else:
        print('英雄机 惜败 敌机!')


# 5. 测试.
if __name__ == '__main__':
    # 思路1: 不使用多态, 完成对战.
    # 场景1: 英雄机1代 vs 敌机1代
    h1 = HeroFrighter()
    e1 = EnemyFrighter()
    if h1.power() >= e1.power():
        print('英雄机1代 战胜 敌机1代')
    else:
        print('英雄机1代 惜败 敌机1代')
    print('-' * 34)

    # 场景2: 英雄机2代 vs 敌机1代
    h2 = AdvHeroFrighter()
    e2 = EnemyFrighter()
    if h2.power() >= e2.power():
        print('英雄机2代 战胜 敌机1代')
    else:
        print('英雄机2代 惜败 敌机1代')

    # 思路2: 使用多态, 完成对战.
    h1 = HeroFrighter()
    h2 = AdvHeroFrighter()
    e1 = EnemyFrighter()
    # 场景1: 英雄机1代 vs 敌机1代
    object_play(h1, e1)
    print('-' * 34)
    # 场景2: 英雄机2代 vs 敌机1代
    object_play(h2, e1)

    # object_play(h1, h2)





























































