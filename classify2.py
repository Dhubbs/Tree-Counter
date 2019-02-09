from PIL import Image
from sklearn.neural_network import MLPClassifier
import glob

good_directory = "/home/hubbledylan/good/*.png"
bad_directory = "/home/hubbledylan/bad/*.png"

good_count = 50
bad_count = 150

#used to speed up processing by only classifiy a portion of base images
#1 = 1/1 size, 2 = 1/4 size, 3 = 1/9 size ...
scale = 1


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
locations = glob.glob(good_directory)
for i in locations:
    total += process(i)

#open and read all "bad" pictures
locations = glob.glob(bad_directory)
for i in locations:
    total += process(i)

#Matches Y values to images
Y = [1 for i in range(good_count)] + [0 for i in range(bad_count)


#sets up and fits neural net
clf = MLPClassifier(solver = 'lbfgs' , alpha = 1e-5, hidden_layer_sizes = (250,100,40), random_state = 1)
print "fitting..."
clf.fit(total ,Y)
print "Complete"


#builds list of all png/jpg to be processed
ready = glob.glob("/home/hubbledylan/ready/*.jpg")
ready.extend(glob.glob("/home/hubbledylan/ready/*.png"))

#iterates through all files to be processed
for i in ready:
    #loads image
    base = Image.open(i)
    base = base.convert('RGB')
    pixels = base.load()

    #makes a new blank image
    output = Image.new('RGB',(base.size[0],base.size[1]))
    pixel = output.load()

    #goes through all pixels, adjusted by "scale"
    for i in range((base.size[0]-25)/scale):
        for j in range((base.size[1]-25)/scale):
            tempi = i*scale
            tempj = j*scale
            
            #cuts out a 25*25 pixel box to the left and down from current pixel location
            temp = []
            for x in range(25):
                for y in range(25):
                    vals = pixels[tempi + x, tempj + y]
                    temp += (vals[0]/256.0,vals[1]/256.0,vals[2]/256.0)
            total = [temp]
            

            #classifys cut out image and highlights depending on classifaction
            if clf.predict(total)[0] == 0:
                if pixel[i,j] != (255,255,255):
                    pixel[i,j] =  pixels[tempi,tempj]
            else:
                if pixel[i,j] != (255,255,255):
                    pixel[i,j] = pixels[tempi,tempj]
                    pixel[i+int(scale/2),j+int(scale/12)] = (255,255,255)
        #prints progress through image
        print str(i) + " of " + str(base.size[0]/1)
    #saves each image
    output.save("/home/hubbledylan/" + i + ".png")
            
