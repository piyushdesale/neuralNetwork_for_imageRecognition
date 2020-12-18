import N as N
import importlib
from PIL import Image
import json
import glob

def GoingToN(imgS,tv,ComingFrom):
    img = Image.open(imgS)
    pix = img.load()
    size = width, height = img.size
    ip = []
    for xp in range(0,width,1):
        s = 0
        for yp in range(0,height,1): 
            (r,g,b) = pix[xp,yp] 
            rgbAVG = int((r+g+b)/3)
            if rgbAVG > 127:
                rgbAVG = 1
            else:
                rgbAVG = 0

            s=s+rgbAVG
        ip  = ip +[s/1000]

    for yp in range(0,height,1):
        s = 0
        for xp in range(0,width,1): 
            (r,g,b) = pix[xp,yp] 
            rgbAVG = int((r+g+b)/3)
            if rgbAVG > 127:
                rgbAVG = 1
            else:
                rgbAVG = 0

            s=s+rgbAVG
        ip  = ip +[s/1000]

    #----------------------------------------------------------
    N.run(ip,tv,ComingFrom)  # Goes to NN:..........
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   
def Test():
    imgS = "TestingImages_withImageNo\\" + input("Enter the Name of image to test >") + ".jpg"    
    Corrected_out = ""
    GoingToN(imgS,Corrected_out,True)
    f = open("sup\\Result")
    r = json.load(f)
    f.close()
    f1 = open("sup\\decode_outputBit.ptxt")
    r1 = f1.read()
    f1.close()
    r1 = r1.split("\n")
    result = ""
    rg = 0
    xg=0
    for xc in range(len(r1)):
        if rg < r[xc]:
            rg = r[xc]
            xg = xc
        result = result + r1[xc]+" : "+str(r[xc]) + "\n"
    result = result + "\n\n"+ "Identified Image is > "+ r1[xg] +" : "+ str(r[xg])
    print(result)

def Train(moves):
    def decode_outputBit():
        decode_outputBit = str(glob.glob("TrainingImages_WithNames/*"))
        decode_outputBit = decode_outputBit.replace("TrainingImages_WithNames\\\\","")
        decode_outputBit = decode_outputBit.replace("', '","\n")
        decode_outputBit = decode_outputBit.replace("['","")
        decode_outputBit = decode_outputBit.replace("']","")
        decode_outputBit = decode_outputBit.replace(".jpg","")
        f = open("sup\\decode_outputBit.ptxt","w")
        f.write(decode_outputBit)
        f.close()
        decode_outputBit = decode_outputBit.split("\n")    
        return decode_outputBit
    decode_outputBit = decode_outputBit()

    #'''
    for xz in range(moves): 
        for x in range(8):
            imgS = decode_outputBit[x]
            imgS = "TrainingImages_WithNames\\" +imgS+".jpg"
            Corrected_out = [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]
            Corrected_out[x] = 0.99
            GoingToN(imgS,Corrected_out,False) #Corrected_out = tv..........
    #'''


k = input("Do you want to Test model or Train:\n Enter 1 for Test, or Enter 2 for the Train\n")
if k == "1":
    Test()
else:
    moves = int(input("Enter the Moves to Train: "))
    Train(moves)

















