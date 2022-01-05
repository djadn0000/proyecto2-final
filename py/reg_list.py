import json

# insert the  link in blacklist 
def InsertToList(link):
    f= open("js/dicc.json", "r")
    c = f.read()
    f.close()
    js =json.loads(c)
    js["lista"].append(link)
    s = json.dumps(js, indent=4)
    w =open("js/dicc.json" , "w")
    w.write(s)
    
# delete the 
def DeleteToList(link):
    f= open("js/dicc.json", "r")
    c = f.read()
    f.close()
    js =json.loads(c)
    js["lista"].remove(link)
    s = json.dumps(js, indent=4)
    w =open("js/dicc.json" , "w")
    w.write(s)

def FoundTheLink(link):
    s= False
    f= open("json/dicc.json", "r")
    c = f.read()
    f.close()
    js = json.loads(c)
    l = js["lista"]
    for x in l:
        if x == link:
            s = True    
    return s

def NameToWebblock(link):
    if FoundTheLink(link) :
        f= open("json/dicc.json", "r")
        c = f.read()
        f.close()
        js =json.loads(c)
        js["Name"] = link
        s = json.dumps(js, indent=4)
        w =open("json/dicc.json" , "w")
        w.write(s)

def BlockedPage(link):   
   if FoundTheLink(link) :
       s = "https//:www.proyectoadrianitt.ddns.net/js/block.html"
       return s
   return link

'''if __name__ =="__main__":
  NameToWebblock("www.youporn.com")
  f= open("json/dicc.json", "r")
  c = f.read()
  js= json.loads(c)
  #print(FoundTheLink("www.youporn.com"))
  adrian = js["lista"][0]
  print(adrian)
  print(js)  
  print("adrian")'''
