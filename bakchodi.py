from tkinter import *
import wikipedia
import os
from gtts import gTTS
import time
import pynput
from pynput.keyboard import Key, Controller
import webbrowser
from googlesearch import search
import random
import subprocess
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
suresir=gTTS(text="sure, sir",lang="en")
suresir.save("suresir.mp3")
keyboard = Controller()
namaste=gTTS(text="hello",lang="en")
namaste.save("hello.mp3")
wiyn=gTTS(text="what is your name sir?",lang="en")
wiyn.save("wiyn.mp3")

question=["who","where","what","how","when","which"]


def joke1():
    j1=("गांव की गोरी के साथ इश्क में बस एक ही परेशानी है कि, अगर रोमांटिक होकर उसकी गोद में सर रखो, तो वो जुएँ देखने लगती है")
    joke1=gTTS(text=j1,lang="hi")
    joke1.save("joke1.mp3")
    os.startfile("joke1.mp3")
    os.startfile("laugh.wav")
    time.sleep(13)
    

def joke2():
    j2=("पति : शादी से पहले तुम्हारे कितने boyfriend थे..?, पत्नी चुप... पति चिल्ला के : , मैं इस ख़ामोशी को क्या समझूं..? पत्नी : ,  गिन तो रही हूँ | चिल्ला क्यों रहे हो ?")
    joke2=gTTS(text=j2,lang="hi")
    joke2.save("joke2.mp3")
    os.startfile("joke2.mp3")
    os.startfile("laugh.wav")
    time.sleep(15)
    

def start():



    time.sleep(2)
    print("what is your name sir?  ")
    os.startfile("wiyn.mp3")
    time.sleep(1.3)
    with mic as source:
        try:
            print("---listening---")
            r.adjust_for_ambient_noise(source)
            audio=r.listen(source)
            print("recognising...")
            name=r.recognize_google(audio)
            print(name)
        except:
            name=("Sir")

    greet= gTTS(text=name,lang="hi")
    greet.save("name.mp3")
    os.startfile("hello.mp3")
    os.startfile("hello.mp3")
    time.sleep(1.1)
    os.startfile("name.mp3")
    time.sleep(2.0)
    text=("I am Mouli. your virtual assistant, say ' hey molly ', if you need any help ")
    intro=gTTS(text=text,lang="en")
    intro.save("text.mp3")
    os.startfile("text.mp3")
    time.sleep(4.3)




    
    while True:
        bkchd=-5
        with mic as source:
            try:
                print("listening")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
                print("recognising")
                openw=r.recognize_google(audio)
                if (openw=="Hemali" or openw=="hey only" or openw=="hey money" or openw=="hey Molly"):
                    os.startfile("beep.mp3")
                    print("verified")
                    bkchd=5
                
            
            except:
                a=("hye")
        if (bkchd>0):
            hcihy=gTTS(text="how can i help you?",lang="en")
            hcihy.save("hcihy.mp3")
            os.startfile("hcihy.mp3")
            time.sleep(2)
            with mic as source:
                try:
                    print("---listening---")
                    r.adjust_for_ambient_noise(source)
                    audio=r.listen(source)
                    print("recognising...")
                    task=r.recognize_google(audio)
                    print(task)
                except:
                    print("could not recognise")
                    task=("hi Molly")
                    bkchd=-5
            j = search(task,num=1,tld="com",lang="en",stop=2,pause=1,start=1)
            for i in j:
                website=i
            w1=task.find("remind")
            w2=task.find("play")
            w3=task.find("open")
            w4=task.find("music")
            w5=task.find("stop listening")
            w6=task.find("shutdown")
            w7=task.find("joke")
            w8=task.find("please molly")
            w9=task.find("hi Molly")
            if (w2>=0):
                os.startfile("suresir.mp3")
                time.sleep(3.5)
                ntask=(task)
                n1=ntask.replace("on YouTube","")
                n1=n1.replace("on gaana","")
                n2=n1.replace("play","")
                n3=n2.replace("video","")
                n0=n3.replace("song","")
                n5=n0.replace("1","")
                n5=n5.replace("2","")
                n5=n5.replace("3","")
                n5=n5.replace("4","")
                n5=n5.replace("5","")
                n5=n5.replace("6","")
                n5=n5.replace("7","")
                n5=n5.replace("8","")
                n5=n5.replace("9","")
                n5=n5.replace("0","")
                n4=n5.replace("and stop listining for","")
                n4=n4.replace("minute","")
                n4=n4.replace("minutes","")
                n4=n4.replace("second","")
                n4=n4.replace("seconds","")
                
                


                w10=task.find("movie")
                w11=task.find("song")
                if (w11>=0):
                    w13=task.find("gaana")
                    if (w13>=0):
                        webbrowser.open("www.gaana.com")
                        time.sleep(4)
                        keyboard.press(Key.space)
                        keyboard.release(Key.space)
                        bkchd=-5
                    else:
                        y=1
                        webbrowser.open("www.youtube.com")
                        time.sleep(5)
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        keyboard.type(n4)
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(2)
                        for y in range (1,11):
                            keyboard.press(Key.tab)
                            keyboard.release(Key.tab)
                            y=y+1
                            time.sleep(0.5)
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        bkchd=-5
                elif(w10>=0):
            
                    webbrowser.open("www.khatrimaza.link")
                    bkchd=-5
                else:
                    y=1
                    webbrowser.open("www.youtube.com")
                    time.sleep(5)
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    keyboard.type(n4)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(2)
                    for y in range (1,11):
                        keyboard.press(Key.tab)
                        keyboard.release(Key.tab)
                        y=y+1
                        time.sleep(0.5)
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    bkchd=-5

            
            if(w7>=0):
                os.startfile("suresir.mp3")
                time.sleep(1)
                i=random.randint(0,1)
                if (i==0):
                    joke1()
                elif (i==1):
                    joke2()
                bkchd=-5

            
            if(w6>=0):
                os.startfile("suresir.mp3")
                print("Bye...")
                time.sleep(2)
                subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
                bkchd=-5
            if(w3>=0):
                os.startfile("suresir.mp3")
                time.sleep(2)
                fname1=task.replace("open","")
                fname2=fname1.replace("game","")
                fname3=fname2.replace("folder","")
                fname4=fname3.replace("file","")
                fname41=fname4.replace("calculator","calc")
                fname5=fname41.replace("app","")
        
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)
                time.sleep(0.05)
                keyboard.type(fname5)
                time.sleep(0.15)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                bkchd=-5


            if(w1<0 and w2<0 and w3<0 and w4<0 and w5<0 and w6<0 and w7<0 and w8<0 and w9<0):
                os.startfile("suresir.mp3")
                a=0
                i=0
                ntask=(task)
                n1=ntask.replace("on YouTube","")
                n1=n1.replace("on gaana","")
                n2=n1.replace("play","")
                n3=n2.replace("video","")
                n0=n3.replace("song","")
                n5=n0.replace("1","")
                n5=n0.replace("2","")
                n5=n0.replace("3","")
                n5=n0.replace("4","")
                n5=n0.replace("5","")
                n5=n0.replace("6","")
                n5=n0.replace("7","")
                n5=n0.replace("8","")
                n5=n0.replace("9","")
                n5=n0.replace("0","")
                n4=n5.replace("and stop listining for","")
                n4=n4.replace("minute","")
                n4=n4.replace("minutes","")
                n4=n4.replace("second","")
                n4=n4.replace("seconds","")
                for i in range(0,6):
                    prob=task.find(question[i])+1
                    a=a+prob
                    i=i+1
                if(a==0):
                    
                    try:
                        detail= (wikipedia.summary(task,sentences=2))
                        tts= gTTS(text=detail,lang="en")
                        tts.save("a.mp3")
                        os.startfile("a.mp3")
                        print(detail)
                        time.sleep(15)
                        bkchd=-5
                    except:
                        print ("I can search it for you")
                        time.sleep(1)
                        webbrowser.open(website)
                        bkchd=-5
                
                else:
                    print ("I can search it for you")
                    time.sleep(1)
                    webbrowser.open(website)
                    bkchd=-5

        
                
            if(w5>=0):
                f1=task.find("minute")
                f2=task.find("minutes")
                a1=task.replace("a","")
                a2=a1.replace("b","")
                a3=a2.replace("c","")
                a4=a3.replace("d","")
                a5=a4.replace("e","")
                a6=a5.replace("f","")
                a7=a6.replace("g","")
                a8=a7.replace("h","")
                a9=a8.replace("i","")
                a10=a9.replace("j","")
                a11=a10.replace("k","")
                a12=a11.replace("l","")
                a13=a12.replace("m","")
                a14=a13.replace("n","")
                a15=a14.replace("o","")
                a16=a15.replace("p","")
                a17=a16.replace("q","")
                a18=a17.replace("r","")
                a19=a18.replace("s","")
                a20=a19.replace("t","")
                a21=a20.replace("u","")
                a22=a21.replace("v","")
                a23=a22.replace("w","")
                a24=a23.replace("x","")
                a25=a24.replace("y","")
                a26=a25.replace("z","")
                task=a26
                a1=task.replace("A","")
                a2=a1.replace("B","")
                a3=a2.replace("C","")
                a4=a3.replace("D","")
                a5=a4.replace("E","")
                a6=a5.replace("F","")
                a7=a6.replace("G","")
                a8=a7.replace("H","")
                a9=a8.replace("I","")
                a10=a9.replace("J","")
                a11=a10.replace("K","")
                a12=a11.replace("L","")
                a13=a12.replace("M","")
                a14=a13.replace("N","")
                a15=a14.replace("O","")
                a16=a15.replace("P","")
                a17=a16.replace("Q","")
                a18=a17.replace("R","")
                a19=a18.replace("S","")
                a20=a19.replace("T","")
                a21=a20.replace("U","")
                a22=a21.replace("V","")
                a23=a22.replace("W","")
                a24=a23.replace("X","")
                a25=a24.replace("Y","")
                a26=a25.replace("Z","")
                a27=a26.replace(" ","")
                print(a27)
                
                if(f1>=0 or f2>=0):
                    a0=int(a27)
                    a4=a0*60
                else:
                    a4=int(a27)
                os.startfile("suresir.mp3")
                time.sleep(a4)
                bck=gTTS(text="Back again. sir",lang="en")
                bck.save("backagain.mp3")
                os.startfile("backagain.mp3")
                time.sleep(1.5)

                






window=Tk()
window.title("Moully v3.0")
photo=PhotoImage(file="moully.gif")
window.configure(background="black")
Label(window,image=photo,bg="black").grid(row=0,column=0,sticky=E)

Button(window,text="Start",width=6,command=start,font="none 12 bold").grid(row=2,column=0,sticky=W)
window.mainloop()
input("press enter")

