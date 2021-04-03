# html parser
from html.parser import HTMLParser

# variable result
result = []

class htmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
    	# check all attributes in tags and then store to array
        for attr in attrs:
        	x = attr[0].split('-')

        	if len(x) < 2:
        		continue

        	result.append(x[1])

parser = htmlParser()
# input html string
parser.feed('<div><div piintu-rootbear="ko" title="Oh My">Hello <i sc-org>World</i></div></div>')
# print result
print(result)