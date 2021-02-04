import re
import os
import shutil
 
drc = 'C:/Users/user/Desktop/DIR2'

 
replacements = [
    ('\d{​​1,3}​​​​​​​​​.\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​.\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​.\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​', 'ip.ip.ip.ip'),
    ('\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​-\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​-\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​-\d{​​​​​​​​​​​​​​​​​​​​​​​1,3}​​​​​​​​​​​​​​​​​​​​​​​', 'ip-ip-ip-ip'),
    ('[zZ][00][0-9]\w{​​​​​​​​​​​​​​​​​​​​​​​0,5}​​​​​​​​​​​​​​​​​​​​​​​','UserIDMaskedHere'),
    ('root', 'u_bootmyfoot'),
    ('admin', 'boot'),
    ('orion', 'biscuit'),
    ('oreo','boreod'),
    ('pam_unix','palmeo'),
    ('pam','bam'),
    ('sage','barge'),
    ('nanny','bunny'),
    ('nginx','gininbox'),
    ('postgre','rexpostserv'),
    ('siemens','OrgMaskinPlace'),
    ('falcon','dalton'),
    ('ssh','hss'),
    ('tomcat','catinwall'),
    ('poc','dummy'),
    ('prod','atty'),
    ('production','attyion'),
    ('AtlasServer','ASERV'),
    ('palmeo','malos'),
    ('palm_env','Dasvos'),
    ('([0-9A-F]{​​​​​​​​​​​​​​​​​​​​​​​2}​​​​​​​​​​​​​​​​​​​​​​​[:-]){​​​​​​​​​​​​​​​​​​​​​​​5}​​​​​​​​​​​​​​​​​​​​​​​([0-9A-F]{​​​​​​​​​​​​​​​​​​​​​​​2}​​​​​​​​​​​​​​​​​​​​​​​)','MyMAC12')
  ]
 
for dirpath, dirname, filename in os.walk(drc):#Getting a list of the full paths of files
    for fname in filename:
        #print("reading File" ,fname)
        path = os.path.join(dirpath, fname) #Joining dirpath and filenames
        #print("reading path" ,path)
        strg = open(path,encoding="utf8").read() #Opening the files for reading only
        #print(strg)
        for old, new in replacements:
            
            if re.search(old, strg):#If we find the pattern ....
                
                
                
                strg = re.sub(old,new,strg)
                
        print(path, strg)        
        print(strg)
        f = open(path, 'w',encoding="utf-8") #We open the files with the WRITE option
        f.write(strg) # We are writing the the changes to the files
        f.close() 
