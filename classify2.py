from PIL import Image
from sklearn.neural_network import MLPClassifier
from skimage import feature
from skimage import io
import numpy as np
import scipy
from scipy import ndimage
import glob
import time
#clf = MLPClassifier(solver = 'lbfgs' , alpha = 1e-5, hidden_layer_sizes(5,2), random_state 
from sklearn.ensemble import RandomForestClassifier

def process(location):
    base = Image.open(i).convert("RGB")
    pixel = base.load()
    temp = []
    for x in range(25):
        for y in range(25):
            vals = pixel[x,y]
            temp += (vals[0]/256.0,vals[1]/256.0,vals[2]/256.0)
    return [temp]

total = []

#open and read all "good" pictures
locations = glob.glob("/home/hubbledylan/good/*.png")
for i in locations:
    total += process(i)

#open and read all "bad" pictures
locations = glob.glob("/home/hubbledylan/bad/*.png")
for i in locations:
    total += process(i)

#currently set up with 50 "good" and 150 "bad"
Y = [1 for i in range(50)]
Y += [0 for i in range(150)]


clf = MLPClassifier(solver = 'lbfgs' , alpha = 1e-5, hidden_layer_sizes = (250,100,40), random_state = 1)

print "fitting..."

clf.fit(total ,Y)
print "Complete"
ready = glob.glob("/home/hubbledylan/ready/*.jpg")
ready.extend(glob.glob("/home/hubbledylan/ready/*.png"))
count = 0
for i in ready:
    print i
    base =Image.open(i)
    base = base.convert('RGB')
    pixels = base.load()

    output = Image.new('RGB',(base.size[0],base.size[1]))
    pixel = output.load()
    temp = []
    count1 = 0
    for i in range((base.size[0]-27)/1):
        for j in range((base.size[1]-27)/1):
            tempi = i*1
            tempj = j*1
            
            temp = []
            for x in range(25):
                for y in range(25):
                    vals = pixels[tempi + x, tempj + y]
                    temp += (vals[0]/256.0,vals[1]/256.0,vals[2]/256.0)
            total = [temp]
            

            if clf.predict(total)[0] == 0:
                if pixel[i,j] != (255,255,255):
                    pixel[i,j] =  pixels[tempi,tempj]
            else:
                if pixel[i,j] != (255,255,255):
                    pixel[i,j] = pixels[tempi,tempj]
                    pixel[i+12,j+12] = (255,255,255)
        
        print str(i) + " of " + str(base.size[0]/1)
        if i%20 == 0:
            output.save("/home/hubbledylan/3.png")
    output.save("/home/hubbledylan/" + str(i) + ".png")
            
