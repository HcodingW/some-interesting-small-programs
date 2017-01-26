# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:37:49 2017

@author: HW
"""

# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def nsepa(li, splist, k):
    # find the nearest one from k
    lip = []
    for e in splist:
        if li.find(e, k) != -1:
            lip.append(li.find(e, k))
    if lip == []:
        return -1
    else:
        return min(lip)

'''        
def split_string(source,splitlist):
    lout = []
    lpos = []
    startpos = nsepa(source, splitlist, 0)
    if startpos == -1:
        lout.append(source)
        return lout
    else:
        if startpos == 0:
            lpos.append(startpos)
        else:
            lout.append(source[:startpos])
            lpos.append(startpos)
        while startpos + 1 <= len(source) - 1 and nsepa(source, splitlist, startpos + 1) != -1:
            startpos = nsepa(source, splitlist, startpos + 1)
            lpos.append(startpos)
        m = len(lpos)
        for i in range(0, m - 1):
            if lpos[i] + 1 < lpos[i + 1]:
                lout.append(source[lpos[i] + 1 : lpos[i + 1]])
        if lpos[m - 1] < len(source) - 1:
            lout.append(source[lpos[m - 1] + 1 :])
    return lout
'''    


def split_string(source,splitlist):
    sourc = splitlist[0] + source + splitlist[0]   ## add the separator at the front and in the end
    lout = []
    lpos = []
    pos = nsepa(sourc, splitlist, 0)
    lpos.append(pos)
    while pos + 1 <= len(sourc) - 1 and nsepa(sourc, splitlist, pos + 1) != -1:
        pos = nsepa(sourc, splitlist, pos + 1)
        lpos.append(pos)
    m = len(lpos)
    for i in range(0, m - 1):
        if lpos[i] + 1 < lpos[i + 1]:
            lout.append(sourc[lpos[i] + 1 : lpos[i + 1]])
    return lout

'''
def split_string(source,splitlist):           ##standard answer
    output = []
    atsplit = True  #initialize at a split point
    for char in source:  #iterate through string by each letter
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #add character to last word
                output[-1] = output[-1] + char
    return output
'''

#print (nsepa("This is a test-of the,string separation-code!", " ,!-", 18))  
#print(split_string(",,,This is a test-of the,string separation-code!!!", " ,!-"))  

#out = split_string("This is a test-of the,string separation-code!"," ,!-")
#print (out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
