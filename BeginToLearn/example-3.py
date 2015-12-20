# coding=utf-8
#/usr/bin/python


class UpperString(object):
    def __init__(self):
        self._value = ''

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value.upper()


class MyClass (object):
    attribute = UpperString()

instance_of = MyClass()

print instance_of.attribute

instance_of.attribute = 'Hello Value'
print instance_of.attribute



