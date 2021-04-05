import re
import requests
import urllib.request
from tkinter import *
from pytube import *
#from pytube import Playlist
 
 
 
#starting The Window   
window=Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

#Tittle Of The Window
window.title("Download Videos By Link ")
#size Of The Window
window.geometry('350x300')

#multiple Video i.e PLaylist Action 
def lst():
    playlist = Playlist(vdurl.get())
    #Shows The Number of Videos Available in The Playlist On The Status Box 
    number=len(playlist.video_urls)
    status='Number of videos in Link:'+str(number)
    t1.insert(END,'\n'+status)
    
    i=0 #Video Count Initialization
    for video in playlist.videos:
        video.streams.first().download()
        #Video count Iteration
        i=i+1
        #Shows The Status on The Status Box
        status ='\n'+"Video Downloaded Successfully:"+str(i)
        t1.insert(END,status)

def fcebk():
    #print("Inside The Facebook Function")
    link = vdurl.get()
    #Get Url Data
    html=requests.get(link)

    #parse Url
    try:
        url=re.search('hd_src:"(.+?)"',html.text)[1]
        t1.insert(END,"HD Video")
        #print("HD Video")
    
    except:
        url=re.search('sd_src:"(.+?)"',html.text)[1]
        t1.insert(END,"SD Video")
        #print("SD Video")

    #Download File
    #print("Downloading....")
    urllib.request.urlretrieve(url, 'FBVideo.mp4')
    #print("Download Successfull")
    t1.insert(END,'\n'+"The Facebook Video Successfully Downloaded")


        
       
#Single Youtube Video link Action      
def youtube():
      link = vdurl.get()
      yt_obj = YouTube(link)
      filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
      filters.get_highest_resolution().download()
      
      #Showing Status Of Download To The Status Box
      status ='\n'+"Video Downloaded Successfully"
      t1.insert(END,status)   

#check Box Function

def print_selection():
    t1.insert(END,"Select Only One Operation At A time"+'\n')
    
    choice = IntVar()
    if (var1.get() == 0) & (var2.get() == 0) & (var3.get()==0):
        choice=0
        
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get()==0):
        choice=1
        
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get()==0):
        choice=2
        
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get()==1):
        choice=3
        
     #elif (var1.get() == 0) & (var2.get() == 0)&(ver3.get()==1):
       # choice=1
       
    else:
        t1.insert(END,"One Operation At A time,Please!!")

    #Ignore This !!!! Testing Comment   
    #print("This Is Print Statement Before Returning The VAlue Fron Print Selection",choice)
        
    return(choice)

#Ignore This !!!! Testing Comment 
#print ("This is print Statement outside the Print Selection ",print_selection())

def download():
    choice = 0 + print_selection()
    if choice==0:
         t1.insert(END,'\n'+"Please Choose An Operation!!")
    elif choice==1:
         youtube()
    elif choice==2:
         lst()
    elif choice==3:
         fcebk()
    #Ignore This !!!! Testing Comment      
    #print("Successfully Executed")


def clear():
    e1.delete(0,'end')
    t1.delete("1.0","end")
    t1.insert(END,"Textbox Cleared")
     
#Download Button
b1=Button(window,height=1,text="Download",command=download)
b1.place(x=254,y=16)


#Clear Button
b2=Button(window,height=1,text="Clear",command=clear)
b2.place(x=200,y=16)


#Check Box

#var1 = IntVar()
#var2 = IntVar()
#var3 = IntVar()
#This Part Is at The Top

c1 = Checkbutton(window, text='Youtube',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c1.place(x=10,y=80)

c2 = Checkbutton(window, text='YT Playlist',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c2.place(x=85,y=80)

c3 = Checkbutton(window, text='FBVideo',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c3.place(x=170,y=80)


#Lebel Above the Entry Box
lbl = Label(window, text="Enter The Link")
lbl.place(x=7,y=1)
#Taking Input OF The link in the Entry Box
vdurl=StringVar()
e1=Entry(window,width=30,textvariable=vdurl)
e1.place(x=10,y=20)

#Showing Download Status [Status Box]

t1=Text(window,height=7,width=41)
t1.place(x=10,y=110)

#Helps To keep up the Tinkter Window Alive

window.mainloop()
