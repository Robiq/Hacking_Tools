#usr/bin/python

import sys
import requests as req
import re

# Find payload in result 
def findData(pattern, data):
    match=re.search(pattern, data)
    if match:
        print match.group()

# TODO
# Change encoding and representation of payload
def getPayloads(payload):
    # url encoded
    # double url encoded
    # hex
    return [payload]

def request(reqType, url, payload, data, format):
    if reqType=='get':
        # return html, not object
        return req.get(url, params=payload).text

    elif reqType=='post':
        formatT=''
        if format==0:
            formatT='text/plain'
        if format==1:
            formatT='application/json'
        if format==2:
            formatT='application/xml'
        if format==3:
            formatT='text/xml'
        # TODO
        # return html, not obj
        headers = {"content-type":formatT}
        return req.post(url, params=payload, data=data, headers=headers).text

if __name__=='__main__':
    # TODO take regex as input?
    # plan is to automate xss
    # find input fields/parameterized urls with burp
    # run script to find exploits
    
    reqType=''
    url=''
    payload=''
    dataformat=0
    data=''
    if len(sys.argv)<3:
        print 'usage: [url] [payload] ([data] [format])'
        print 'format: 0=txt, 1=json, 2=xml'
        quit()
    elif len(sys.argv)>3:
        reqType='post'
        data=sys.argv[3]
    else:
        url='http://'+sys.argv[1]
        payload=sys.argv[2]
        reqType='get'
        
    print reqType
    print url
    print payload
    
    # Make regex
    regex=re.compile(re.escape(payload), re.M|re.I)
    
    # TODO
    # convert payload to different encoding 
    payloads=getPayloads(payload)
    
    useable=[]
    for p in payloads:
        # TODO change resp to html content 
        resp=request(reqType, url, payload, data, format)
        #print resp
        
        # TODO
        # do regex to extract data from response (eg. payload)
        # store if regex found
        injection = findData(regex, resp)
        if injection:
            # things to store:
            # url, payload, result
            useable.push({'url':url, 'payload':p, 'result':resp})
            
    # TODO
    # go through usable results
    linkList=[1]
    linkList[0]="<li>"
    for x in range(len(useable)):
        html=generateHTML(useable[x])
        filename=url+'_'+x+'.html'
        f=file(filename,'w')
        f.write(html)
        f.close()
        # TODO build HTML with results
        # format: link 1,2,3...
        # link contains url, payload as txt and result as HTML 
        linkList.append("<a href="+filename+">"+x+"</a>")
   
    linkList.append("</li>")
    
    # TODO write to file!
    a=""
    for i in linkList:
    	a+=i
    print a
