import glob

decode_outputBit = str(glob.glob("TrainingImages_WithNames/*"))
decode_outputBit = decode_outputBit.replace("TrainingImages_WithNames\\\\","")
decode_outputBit = decode_outputBit.replace("', '","\n")
decode_outputBit = decode_outputBit.replace("['","")
decode_outputBit = decode_outputBit.replace("']","")


decode_outputBit = decode_outputBit.replace(".jpg","")
f = open("sup\\decode_outputBitQ.ptxt","w")
f.write(decode_outputBit)
f.close()

print(decode_outputBit)