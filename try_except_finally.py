import sys
from urllib import request, parse

url = "https://www.google.com/search?"
query_string = { 'q':'list main methods of urllib request in python 3'}
qry = parse.urlencode(query_string)
print ("this is how urlencoded data looks like: "+qry)
qry = url + qry
print ("this is end query url with userdata"+qry)
#myheader = {}
myheader = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"}
try:
  #response1 = request.urlopen(url)
  req = request.Request(qry, headers=myheader)
  response_orig = request.urlopen(req)
#  response = response_orig.readlines()
except Exception:
  print ("Error occured during web-request")
  print (sys.exc_info()[0], sys.exc_info()[1])
 

finally:
#  output1 = response
  
  output2 = response_orig.read()

  print ("Request to "+url+"was successful")
  print ("\n")
#  print ("Data returned ")
#  for line in output1:
#    print (line)

  print ("\n")
 # print(response1.read())

  # Read the content of the response
  html_content = response_orig.read()

  # Specify the filename for the HTML file
  html_file = 'output.html'

  # Write the HTML content to a file
  try:
    with open(html_file, 'wb') as file:
        file.write(html_content)
  except Exception:
    print("Error writing to file {html_file}")
    print(sys.exc_info()[1])
  finally:
    pass
  print(f'HTML content has been saved to {html_file}')
  pass

