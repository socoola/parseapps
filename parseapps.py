# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    find_div = False
    attrs_div = {}
    def attrs_to_dict(self, attrs):
        attrs_dict = {}
        for attr in attrs:
            attrs_dict[attr[0]] = attr[1]
        return attrs_dict

    def handle_starttag(self, tag, attrs):
        if(tag == 'div'):
            #print "Encountered the beginning of a %s tag" % tag
            #if(attrs['class'] == 'name col2'):
            attrs_dict = self.attrs_to_dict(attrs)
            if(attrs_dict.has_key('class') and (attrs_dict['class'] == 'name col2')):
                self.find_div = True
                self.attrs_div = attrs_dict
        elif((self.find_div) and (tag == 'a')):
            attrs_a = self.attrs_to_dict(attrs)
            print self.attrs_div['title'], attrs_a['href']
            f=open(self.attrs_div['title'].decode('utf-8'), 'w+')
            f.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="https://itunesconnect.apple.com/" />
<title>%s</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">%s</td></tr>
</thead><tbody>
<tr>
	<td>open</td>
	<td>%s</td>
	<td></td>
</tr>
<tr>
	<td>waitForVisible</td>
	<td>link=价格与销售范围</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>link=价格与销售范围</td>
	<td></td>
</tr>
<tr>
	<td>waitForVisible</td>
	<td>//div[@id='pageWrapper']/div[5]/div[5]/div/div[3]/div[2]/div/div[4]/div/div/table/tbody/tr[2]/td/div/div</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>//div[@id='pageWrapper']/div[5]/div[5]/div/div[3]/div[2]/div/div[4]/div/div/table/tbody/tr[2]/td/div/div</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>//div[@id='tierSelectionID']/div/table/tbody/tr[5]/td/span</td>
	<td></td>
</tr>
<tr>
	<td>click</td>
	<td>css=button.ng-animate</td>
	<td></td>
</tr>

</tbody></table>
</body>
</html>
''' %(self.attrs_div['title'], self.attrs_div['title'], attrs_a['href']))


    def handle_endtag(self, tag):
        #if(tag == 'div'):
        #    print "Encountered the end of a %s tag" % tag
        if((tag == 'div') and self.find_div):
            self.find_div = False
            self.attrs_div = {}


p = MyHTMLParser()
f = open("data.txt")
try:
    for line in f:
        p.feed(line)
finally:
    f.close()





