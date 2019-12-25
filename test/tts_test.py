from gtts import gTTS 

import os 

mytext = "Welcome to my Page"

langauge = 'en'

myobj = gTTS(text = mytext, lang = langauge, slow = False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")

def talkit(arr):
    arr = natural(arr)    
    s = ''
    for i in arr:
        s += i + ", "
    
    myobj = gTTS(text = s, lang = 'en', slow = False)
    myobj.save('object.mp3')
    os.system("mpg321 object.mp3")

def natural(arr):
    d ={}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    final = []
    sp = "There are "
    ss = "There is "

    for i in d:
        if d[i] == 1:
            f = ss + str(d[i]) + " "+ i
            final.append(f)
        else:
            f = sp + str(d[i]) + " " + i
            final.append(f)

    return final