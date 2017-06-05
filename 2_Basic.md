# Python3 基础语法

# 1. 编码

默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：

    # -*- coding: cp-1252 -*-

# 2. 标识符

- 第一个字符必须是字母表中字母或下划线'_'。
- 标识符的其他的部分有字母、数字和下划线组成。
- 标识符对大小写敏感。

在Python 3中，非-ASCII 标识符也是允许的了。

# 3. python保留字

保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 4. 注释

Python中单行注释以 # 开头，实例如下：

```python3
#!/usr/bin/python3

# 第一个注释
print ("Hello, Python!") # 第二个注释
```

执行以上代码，输出结果为：

    Hello, Python!

多行注释可以用多个 # 号：

```python3
#!/usr/bin/python3

# 第一个注释
# 第二个注释

print ("Hello, Python!") 
```

执行以上代码，输出结果为：

    Hello, Python!

# 5. 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

```python3
if True:
	print ("True")
else:
	print ("False")
```

以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：

```python3
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
```

以上程序由于缩进不一致，执行后会出现类似以下错误：

```python3
 File "test.py", line 6
    print ("False")    # 缩进不一致，会导致运行错误
                                      ^
IndentationError: unindent does not match any outer indentation level
```

# 6. 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：

    total = item_one + \
            item_two + \
            item_three

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：

    total = ['item_one', 'item_two', 'item_three',
            'item_four', 'item_five']

# 7. 数据类型

python中数有四种类型：整数、长整数、浮点数和复数。

- 整数， 如 1
- 长整数 是比较大的整数
- 浮点数 如 1.23、3E-2
- 复数 如 1 + 2j、 1.1 + 2.2j

# 8. 字符串

- python中单引号和双引号使用完全相同。
- 使用三引号('''或""")可以指定一个多行字符串。
- 转义符 '\'
- 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
- python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
- 字符串是不可变的。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。

```python3
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
```

# 9. 空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。

# 10. 等待用户输入

执行下面的程序在按回车键后就会等待用户输入：

```python3
#!/usr/bin/python3

input("\n\n按下 enter 键后退出。")
```

以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下键时，程序将退出。

# 11. 同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

```python3
#!/usr/bin/python3

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

执行以上代码，输入结果为：

    $ python3 test.py
    runoob
    7

# 12. 多个语句构成代码组

缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

如下实例：

```python3
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```

# 13. Print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

```python3
#!/usr/bin/python3

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
```

以上实例执行结果为：

    a
    b
    ---------
    a b

# 14. import 与 from...import

在 python 用 `import` 或者 `from...import` 来导入相应的模块。
将整个模块(somemodule)导入，格式为： `import somemodule`
从某个模块中导入某个函数,格式为： `from somemodule import somefunction`
从某个模块中导入多个函数,格式为： `from somemodule import firstfunc, secondfunc, thirdfunc`
将某个模块中的全部函数导入，格式为： `from somemodule import *`

```python3
# 导入 sys 模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
```

# 15. 命令行参数

很多程序可以执行一些操作来查看一些基本信，Python可以使用-h参数查看各参数帮助信息：

    $ python -h
    usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
    Options and arguments (and corresponding environment variables):
    -c cmd : program passed in as string (terminates option list)
    -d     : debug output from parser (also PYTHONDEBUG=x)
    -E     : ignore environment variables (such as PYTHONPATH)
    -h     : print this help message and exit
    
    [ etc. ]

我们在使用脚本形式执行 Python 时，可以接收命令行输入的参数，具体使用可以参照[Python 3 命令行参数](http://www.runoob.com/python3/python3-command-line-arguments.html)。