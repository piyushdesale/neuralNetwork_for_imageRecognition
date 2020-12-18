iplength = int(input("Enter No of IP length(prefer:128):\n"))
oplength = int(input("Enter No of OP length(prefer:8):\n"))

hip = []
for x in range(iplength):
    hip = hip+[0]

hop = []
for x in range(oplength):
    hop = hop+[hip]

hop = [hop]
f =open("weights\hweight","w")
f.write(str(hop))
f.close()

f =open("weights\Error_weight","w")
f.write(str(hop))
f.close()