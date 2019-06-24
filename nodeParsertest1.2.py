import pandas as pd
import xml.etree.ElementTree as ET
import re

####DEFINE NODE####
def getvalueofnode(node):
    """return node text or None"""
    return node.text if node is not None else None
    ###Will get the value as a text in the end to insert the data into the dataframe
    ###if there is no data it returns None

###DEFINING ROOT ELEMENT###
dfcols = ['Date', 'Product', 'Buyer', 'Price'] ###nameing the columns of the dataframe (header of the table)
#df_xml = pd.DataFrame(columns=dfcols) ###sets DataFrame to use the header as columns

###takes the test roll and parses it with ElementTree
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml')
###defines root as the root - Element from Test roll.xml
root = tree.getroot()

####GET DATA####
###iteration over body in root
for body in root:
    ###itertion over divs in body
    for div in body:
        date = div.find('.//date')
        rows = div.findall('.//row')
        for row in rows:
            cells = row.findall('.//cell')
            date2 = getvalueofnode(date)
            #print(cells)
            product = getvalueofnode(cells[0])
            buyer = getvalueofnode(cells[1])
            price = getvalueofnode(cells[-1])
            #print(date2)
            #print(getvalueofnode(product))
            #print(getvalueofnode(buyer))
            #print(getvalueofnode(price))
            lines = (date2 + ';' + str(product) + ';' + str(buyer) + ';' + str(price))
            f = open('ResultTEST.txt', 'a', encoding = 'utf-8')
            f.write(str(lines))
            f.write('\n')
            f.close()
            print(done)
            if row == rows:
                break


f = open('ResultTEST.txt', 'r', encoding='mbcs')
word = ['(.*paard.*)|(.*veul.*)|(.*merrij.*)|(.*hengste.*)']
for line in f:
    for i in word:
        if re.search(i, line):
            print(line)
            horses = line
            horsesFile = open('horses.csv', 'a', encoding='utf-8')
            horsesFile.write(horses)
            horsesFile.close()
            horsesFileTxt = open('horses.txt', 'a', encoding='utf-8')
            horsesFileTxt.write(horses)
            horsesFileTxt.close()
