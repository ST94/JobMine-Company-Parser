from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    recording = False
    companyNameArray = []

    def handle_starttag(self, tag, attrs):
        #print ("Encountered a start tag:", tag)
        if tag == 'div':
            #print ('td')
            for attr,attr_value in attrs:
                #print (attr, attr_value)
                if 'UW_CO_EMPLYR_NAME' in attr_value:
                    self.recording = True
                if 'UW_CO_PARENT_NAME' in attr_value:
                    self.recording = True

    #def handle_endtag(self, tag):
        #print ("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.recording:
            #print (data)
            self.companyNameArray.append(data)
            self.recording = False



# instantiate the parser and fed it some HTML

with open('data/data.html', 'r') as my_file:
    parser = MyHTMLParser()
    parser.feed(my_file.read())
    print (parser.companyNameArray)


