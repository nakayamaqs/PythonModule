#
# Pulls all of the contents from each of the URLs in the 'urls' list,
# and returns what appears to be the favorite word, where the
# metric for what favorite means is outlined above
#

def getFavoriteWord(urls):
    import urllib.request
    import re
    import operator
    from operator import itemgetter

    responseText = urllib.request.urlopen(urls)
    dic_result = {}

    for line in responseText:
    	words = str(line.replace(b"\r", b"").replace(b"\n", b"")).split() #convert byte to string, replace \r\n.
    	# print(words)
    	for i,f in enumerate(words):
    		# f = f.replace("\r", "") #remove \r\n
    		# f = f.replace("\n", "")
    		f = f.replace("\"", "")
    		# print(f)
    		f = re.sub("[',;.?!())]", '', f) # replace char like ...
    		# Check if word is lowercase
    		if(f.islower()):
    			# check if word is in dictionary yet or not
    			if(f in dic_result):
    				dic_result[f] = dic_result[f] + 1
    			else:
    				dic_result[f] = 1

    # for w in sorted(set(dic_result)):
    #     print(w + ": " + str(dic_result[w]))

    for w in sorted(dic_result, key=dic_result.get, reverse=True):
         print(w + ": "+  str(dic_result[w]))

    # htmlSource = responseText.read()
    # print(dic_result)
    responseText.close()
    # print(htmlSource)

getFavoriteWord("http://www.gutenberg.org/files/5200/5200.txt")
