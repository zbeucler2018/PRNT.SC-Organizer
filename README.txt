#Use tensorflow to classify the imgs
#https://towardsdatascience.com/easy-image-classification-with-tensorflow-2-0-f734fee52d13
#


################################

from lxml import html
import requests

page = requests.get('https://prnt.sc/ab1234')
tree = html.fromstring(page.content)

data = tree.xpath('/html/body/div/div')

print(data)
print(type(data))

################################



create a dictionary (key | value) (number | value)

loop through all possible urls
  find the img url
  add the url as a value and number as key

finish dictionary

"No Screenshot" img declared

NoSC dict declared
validSC dict declared

loop through all imgs in dict
  if img == "No Screenshot"
    add to NoSC
  else
    add to validSC




