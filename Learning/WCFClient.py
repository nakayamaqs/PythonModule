# Connect to WCF services with Python.

import urllib.parse
import urllib.request

# Not working with parameters below.
def connectWebMethod(url, values):
    # url = 'https://resource.mirror.microstrategy.com/SSO/mstruser.svc/GetPerson'
    # values = {'applicationKey' : 'Michael Foord',
    #           'token' : 'Northampton'
    #          }

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8',
        'Content-Length': len(data)
        }

    req = urllib.request.Request(url, data,headers)

    try:
        response = urllib.request.urlopen(req)
        print(response)
        the_page = response.read()
        print(the_page)
    except urllib.error.URLError as e:
        print('Error: '+e.reason)
        print(e.read())


url = 'https://resource.mirror.microstrategy.com/SSO/mstruser.svc/GetPerson'
values = {'applicationKey' : 'Michael Foord',
              'token' : 'Northampton'
         }
# connectWebMethod(url, values)

url2 = 'https://chn-zhzhang2.corp.microstrategy.com/resourceCenterService/ResourceCenterInformation.asmx/HelloWorld'
values2 = {'userList' : [ {'UserName' : 'Northampton'},
                          {'UserName' : 'Zhe'} ]
          }
# connectWebMethod(url2, values2)

# consume web service in SOAP format.
#
def InvokeWebservice():
    texturl='https://chn-zhzhang2.corp.microstrategy.com/resourceCenterService/ResourceCenterInformation.asmx?op=HelloWorld'
    # postcontent='<?xml version="1.0" encoding="utf-8"?>'
    # postcontent+='<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
    # postcontent+='<soap:Body>'
    # postcontent+='<SendShortMessage xmlns="http://tempuri.org/">'
    # postcontent+='<phonenum>'+phone+'</phonenum>'#参数
    # postcontent+='<message>'+msg+'</message>'#参数
    # postcontent+='</SendShortMessage>'
    # postcontent+='</soap:Body>'
    # postcontent+='</soap:Envelope>'
    postcontent = """<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <HelloWorld xmlns="http://Microstrategy.ResourceCenterService.com/">
          <UserName>
            <string>"ZZ"</string>
            <string>"323"</string>
          </UserName>
        </HelloWorld>
      </soap12:Body>
    </soap12:Envelope>"""
    req=urllib.request.Request(texturl, data=postcontent.encode('utf-8'), headers={'Content-Type': 'text/xml'})
    response = urllib.request.urlopen(req)
    print(str(response) + " code " + str(response.code))
    the_page = response.read()
    print(str(the_page))

def CallRESTfull():
    # Defaults
    dbName = 'uniprotkb'
    entryId = 'wap_rat'
    format = None

    # Construct URL
    baseUrl = 'http://www.ebi.ac.uk/Tools/dbfetch/dbfetch'
    url = baseUrl + '/' + dbName + '/' + entryId
    if format != None:
        url += '/' + format

    # Get the entry
    fh = urllib.request.urlopen(url)
    result = fh.read()
    fh.close()

    # Print the entry
    print(result)

# InvokeWebservice()
CallRESTfull()
