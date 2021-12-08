from typing import Text


WelcomeText = 'Hello'

def addName(name:str):
    global WelcomeText
    WelcomeText += ' '+name
    return WelcomeText

allText = addName('Jan') + ', ' + addName('willem')

print(allText)