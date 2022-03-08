# @desc: This document contains the button class that will
# be used in main-menu and settings screens. The Button will be fully
# reusable, and customizable to fit different usecases.


class Button(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        print(self.title)



Button("start", "Start")