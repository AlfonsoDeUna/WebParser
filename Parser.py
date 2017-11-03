'''
Created on 3 nov. 2017

@author: Alf
'''

from lxml import html
import requests

class Parser(object):
    '''
    
    '''
def factory (type):
    if type == "Joomla": return JoomlaParser()
    if type == "Wordpress": return WordPressParser()
    assert 0, "Error Parser Creation: " + type 
    factory = staticmethod (factory)
       
    class WordPressParser(Parser):
        pass

    
    class JoomlaParser (Parser):
    
    
        def doParse(self, url_page): 
            
            page = requests.get(url_page)
            tree_page = html.fromstring(page.content)
            metaInf = tree_page.xpath('/html/head/meta[@name="generator"]/@content')
            path = "".join(metaInf)
            
            if path.find("Joomla") is not -1:
                return True
            else:    
                return False