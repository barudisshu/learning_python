
# A variable is a name that refers to a value.
# 变量就是一个名字指向值得引用

message = 'And now for something completely different'
n = 17
pi = 3.1415926

# 命名规范：可以包含字母和数字，但不能以数字开头。可以使用大写字母开头，但不推荐
# 占位符`_`可以出现在名。
# 关键字不能作为变量名

# 一个表达式(expression)由值、变量、操作符组成。值本身可以被看作一个表达式，单独一个变量可是一个合法的表达式。

# 一个语句(statement)是一段代码单元。通常，语句不包含值。

miles = 26.2
print(miles * 1.61)

# 变量的声明部分不执行输出

# 操作的执行顺序
# python遵循数学规约。按照PEMDAS原则
# - Parentheses                    括号
# - Exponentiation                 乘方
# - Multiplication and Division    乘除
# - Operators                      同等级则从左到右

# 字符串也适用操作符，但仅限于`+`和`*`。不过意义不同
first = 'throat'
second = 'warbler'
print(first + second)  # concat
print('Spam' * 3)      # SpamSpamSpam

# 注解以`#`开头
