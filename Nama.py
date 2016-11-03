import re
import math
f = open('API_SI.POV.GINI_DS2_en_csv_v2.csv', 'r')
#f = open('koferry.txt', 'r')

i = 0;
output=""
for line in f:
    i+=1
    variable = re.sub('(^["a-zA-z\s"]+,)','',line)
    searchObj = re.search('(^["a-zA-z\s"]+,)', variable)

    if searchObj:
       output+= re.sub('[",]','',searchObj.group())
    
    
    variable = re.sub('(^["a-zA-z\s"]+,)','',variable)
    variable = re.sub('(^["a-zA-z\s()]+),(["A-Z\.]+),','',variable)
    


    jumlahData =0
    min =10000000.000
    max =0.0
    rata2 =0.0
    for (obj) in re.findall('([\d.]+)', variable):
        
        
        if obj is not "." and not "":
            cek = int(float(obj));
            cek = str(cek)
        
        if cek.isdigit():
            if obj is not "." and not "":
                datafloat = float(obj)
                jumlahData+=1
                if datafloat < min:
                    min = datafloat
                if datafloat > max:
                    max = datafloat
                
                rata2 += float(obj)
        
    if jumlahData >0:
        rata2 /= jumlahData
        output+= ' '+str(jumlahData) +" " +str(rata2)+" "+str(max)+" "+str(min)
    else:
        output+= ' '+str(jumlahData)
    
    
    output+="\n"
    
    
print output
    
print i
