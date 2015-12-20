# coding=utf-8
#/usr/bin/python

class Mama(object):

    def say(self):
        print 'do your homework'


class Sister(Mama):

    def say(self):
        Mama.say(self)
        print ' and clearn your bedroom'


anita = Sister()
anita.say()