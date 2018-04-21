
numPages = 10
pageNum = 2

# build xpath:
thisInfo = '['+str(pageNum)+'/'+str(numPages)+']'        
pageInfoXPATH = ( '//p[@class="page_info" and '+
                  'contains(text(),"'+
                  thisInfo+ '")]' )

example = '//p[@class="page_info"] and contains(text(),"[2/10]")]'

# straightforward
find(pageInfoEleXPATH).click()

# or use beautifulsoup
for ele in soup.find_all('p'):
    if ele.has_attr('class') and ele.get('class') == 'page_info' and '[2/20]' in ele.text:
        # got it
        pass

# or pass in a function
def match_func(node):
    if node.name == 'p'and node.has_attr('class') and node.get('class') == 'page_info' and '[2/20]' in node.text:
        return True
    else:
        return False
    
for ele in soup.find_all(match_func):
    pass

# you can also use lambda if you value unreadability
