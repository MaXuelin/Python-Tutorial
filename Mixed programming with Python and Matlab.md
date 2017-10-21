Python跟matlab的混合编程，也就是两者的相互调用。本教程所用的系统`Win7`.

一、在python中调用matlab文件
====

需要的python的库是mlab<br>
GitHub链接是：https://github.com/ewiger/mlab#windows <br>

安装mlab：<br>
要求：已经安装有pip 和setuptools ("easy_install.exe")，如果安装了anaconda一般都有这两个库。<br>

1、	打开cmd；<br>
2、	```easy_install.exe pywin32```，安装PyWin32模块<br>
3、	```pip install mlab```，安装mlab库<br>

测试mlab，成功画出图像说明测试通过：
```python
from mlab.releases import latest_release as matlab
matlab.plot([1,2,3],'-o')
```

假设.m脚本文件的名字为testScript.m，在python中调用的程序实例如下：
```python
from mlab.releases import latest_release as matlab
matlab.testScript
```

假设.m函数文件的名字为testFunction.m，假设输入变量为input，输出变量为output，实现matlab函数的运行和结果返回。在python中调用的程序实例如下：
```python
from mlab.releases import latest_release as matlab
output = matlab. testFunction(input)
```

常见问题解决：
```matlab
MatlabError: Attempt to execute SCRIPT test as a function:
```
这个错误的原因是，`test`在python中已经有定义，那么.m文件不能使用相同的名字。<br>


二、在matlab中调用python程序
====

Matlab一般自带了调用python的接口，想要查看matlab调用的python版本，在matlab命令行中输入：
```matlab
pyversion
```
输出为：
```matlab
       version: '2.7'<br>
    executable: 'D:\Program Files\Anaconda2\python.EXE'<br>
       library: 'D:\Program Files\Anaconda2\python27.dll'<br>
          home: 'D:\Program Files\Anaconda2'<br>
      isloaded: 1<br>
```

在matlab中调用python一般用如下的命令：
```matlab
py.module.function()
```
其中，`module`是你自己建立的py文件的名称，`function`是py文件中对应的函数名。举例如下（文件名 `mymod.py`）：<br>

```python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 00:48:57 2017

@author: Ma Xuelin
"""

# mymod.py
"""Python module demonstrates passing MATLAB types to Python functions"""
def search(a):
    """Return list of words containing 'son'"""
    a = a*2
    return a

def theend(words):
    """Append 'The End' to list of words"""
    words.append('The End')
    return words
    
def main():
    return search(5)
    
if __name__ == '__main__':
    main()
```
调用主函数：
```python
py.mymod.main()
```
调用search子函数，注意输入参数要匹配
```python
py.mymod.search(3) 
```


到此，python跟matlab的混合编程介绍完毕。
