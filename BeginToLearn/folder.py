# coding=utf-8
#/usr/bin/python

class Folder (list):

    def __init__(self, name):
        self.name = name

    def dir(self):
        print 'I am the %s folder.' % self.name
        for element in self:
            print element


the = Folder('secret')
print the

the.append('pics')
the.append('videos')
the.dir()



