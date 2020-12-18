from math import exp as E
import json

h1 = [0,0,0,0,0,0,0,0] 
h1out = [0,0,0,0,0,0,0,0] 
Bias = 0.01 #0.1

def back_propogate(ip,hweight,h1out,tv):
    for tvx in range(len(tv)):
        tv[tvx] = float(tv[tvx])
    
    f =open("weights\Error_weight")
    Error_weight = json.load(f)
    f.close()
    print("<><><><><>")
   
    for x in range(8): #@ output length = 0 to 8
        while((int(h1out[x]*10+Bias) != int(tv[x]*10))):
            Total_Error_steps = (h1out[x]-tv[x])*(E(-h1[x])/( (1+E(-h1[x])) * (1+E(-h1[x])) ))
            for y in range(128): #@ input length = 0 to 128
                Error_weight[0][x][y] = Total_Error_steps * ip[y]
                hweight[0][x][y] = hweight[0][x][y] - Error_weight[0][x][y]
            h1[x] = 0
            for y in range(128): #@ input length = 0 to 128
                h1[x]=h1[x] + (ip[y]* hweight[0][x][y])
            h1out[x] = (1/(1+(E(-h1[x])))) + Bias

    print("<><>OutNew___ >>>>\n", h1[0],":",h1[1],":",h1[2],":",h1[3],"  ",tv)
    print("=")
    print("<><>OutPut New ___+>>>>\n", h1out[0],":",h1out[1],":",h1out[2],":",h1out[3],"  ",tv)
    f = open("weights\hweight",'w')
    f.write(str(hweight))
    f.close()
    
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def run(ip,Corrected_out,ComingFrom):
    f =open("weights\hweight")
    hweight = json.load(f)
    f.close()
    for x in range(8): #@ output length = 0 to 8
        h1[x] = 0
        for y in range(128): #@ input length = 0 to 128
            h1[x]=h1[x]+(ip[y]*hweight[0][x][y])
        h1out[x] = (1/(1+(E(-h1[x])))) + Bias
        
    if ComingFrom == True:
        f = open("sup\Result","w")
        f.write(str(h1out))
        f.close()
#_______________________________________________________________
    
    if Corrected_out != "":
        back_propogate(ip,hweight,h1out,Corrected_out)
        
    
    
        












