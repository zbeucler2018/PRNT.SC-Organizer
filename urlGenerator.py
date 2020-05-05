# urlGenerator makes random urls
import random, string


def prepend(listObj, strAdded): 
    strAdded += '{0}'
    listObj = [strAdded.format(i) for i in listObj] 
    return(listObj)

def urlGen():
  randURLs = []
  #create 10 urls
  for _ in range(10):
    # get 2 random letters in a string
    letters = ""
    for _ in range(2):
      letters = letters + random.choice(string.ascii_lowercase)
    # get 4 random numbers in a string
    numbers = ""
    for _ in range(4):
      numbers = numbers + random.choice(string.digits)
    # add the 2 strings togther
    val = letters + numbers 
    # check if val is in randURLs or not
    while val not in randURLs:
      randURLs.append(val)

  # Add "https://prnt.sc/" to the front of the randURLs elements
  baseURL = 'https://prnt.sc/'
  
  #add baseURL to the front of all randURL strings
  randURLs = prepend(randURLs, baseURL)

  print()
  print("##### Generator #####")
  print(randURLs)
  print("################################################")
  print()

  
  # return randURL
  return(randURLs)