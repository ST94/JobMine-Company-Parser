from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print ("Encountered a start tag:", tag)
        if tag == 'td':
            print ('td')
            for attr,attr_value in attrs:
                print (attr, attr_value)
                if attr == 'col':
                    print ('col')
                    if attr_value =='2':
                        print (self)

    #def handle_endtag(self, tag):
        #print ("Encountered an end tag :", tag)

    #def handle_data(self, data):
        #print ("Encountered some data  :", data)

# instantiate the parser and fed it some HTML

with open('data/data.html', 'r') as my_file:
    parser = MyHTMLParser()
    parser.feed(my_file.read())