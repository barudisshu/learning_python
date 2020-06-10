import math

# 在程序上下文中，函数是一系列被命名的执行计算的语句。函数的定义需要定义名称和语句。然后“调用”。

type(42)

int('32')

# int('Hello')  错误

int(3.9999999)
int(-2.3)

# 浮点
float(32)
float('3.14159')

# 字符串
str(32)
str(3.14159)

# 数学函数

signal_power = 3
noise_power = 2

ratio = signal_power / noise_power
describels = 19 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)

math.sqrt(2) / 2.0

# 函数可以组合
x = math.sin(degrees / 360 * 2 * math.pi)

x = math.exp(math.log(x + 1))


# 添加一个函数

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


print_lyrics()


# 函数内可以调用其它函数
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# 函数内部的变量和参数是本地的

def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)


line1 = 'Bing tiddle '
line2 = 'tiddle bang.'

cat_twice(line1, line2)

# Fruitful Functions and Void Functions
# PY中认为有返回值的是fruitful function ，没有返回值的是 void function

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
