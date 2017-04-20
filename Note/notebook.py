#!/usr/bin/python 
# -*- coding=utf-8 -*-

import datetime

# 为所有新的备注存储下一个可用的id
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a string in serachs and store tags for each note.'''
    
    def __init__(self, memo, tags=''):
        
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match (self, filter):
        
        return filter in self.memo or filter in self.tags



class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

