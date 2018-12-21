
import time
# 1．使用全局函数来装饰类方法
# ２．使用类方法来装饰类方法
# ３．使用类内置方法来装饰实例方法

# def a_(fun):


# class A(object):
#     def __init__(self):
#         self.a_ = 100

#     @a_ #使用全局函数装饰
#     def func(self, num):

#     def b_(fun):

#     @b_ #使用类内方法装饰
#     def func1(self, num):

# c = A()
# c_ = c.func(100)
# print(c_)   #200
# c_1 = c.func1(102)
# print(c_1)  #202

#--------------------------

# def a_(fun):
#     def inner(*args,**kwargs):
#         c = fun(*args,**kwargs)
#         return c
#     return inner

# class A(object):
#     def __init__(self):
#         self.a = 100

#     @a_#使用全局函数装饰
#     def func(self, num):
#         return num + 100

# c = A()
# c_ = c.func(100)
# print(c_) #  200

# #------------------------

# class A(object):
#     def __init__(self):
#         self.a = 100

#     def b_(fun):
#         ******

#     @b_#使用类内方法装饰
#     def func1(self, num):
#         ******
# c_1 = c .func1(102)
# print(c_1) # 202

# #-------------------------
# class B(object):
#     def __init__(self):
#         ******

#     def __***__()
#         ******

# @B#使用类来装饰
# def cc(num,num1):
#     return num+num1
# d = cc (11,22) # 33
# print(d)

#-------------------------
class A(object):
    def __init__(self,func):
        self.a = 100
        self.func = func
    def __call__(self, *args, **kwargs):
        print(time.time())
        c = self.func(self,*args,**kwargs)
        print(c,'这是c')
        print(time.time())
        return c

class B:
    def __init__(self):
        self.a = 200

    @A
    def func(self,num):
        return num+self.a

b = B()
c = b.func(100)
print(c)