'''
Created on 6 oct. 2017

@author: Alf
'''
from Parser import Parser

p = Parser("")

def main():
    print ("Run first test a url from joomla's page")
    test ('https://www.joomla.org')
    print ("Run second test is other type of web (not joomla)")
    test('http://www.elmundo.es')
        
def test(testURL):        
    if p.doParse(testURL) == True:
        print ("This page was created by JOOMLA")        
    else:
        print ("It wasn't created by J! Try an other page for my test please...")
        
        
    
if __name__ == '__main__':
    print ("example")
    main()