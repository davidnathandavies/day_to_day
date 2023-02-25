from tkinter import *
from PIL import ImageTk,Image
import calendar
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4 as bs 
import ssl
import lxml
import json
import requests
from datetime import date
import day_to_day_config


today = str(date.today())
todayz = today + "Z"
#print (todayz)
maxtempdays = []
mintempnights = []
maxwinddays = []
winddirections = []
rainprob = []
weathertypedays = []



content = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/html/' + day_to_day_config.met_location + '?res=daily&key=' + day_to_day_config.met_api_key


html = urlopen(url)
soup = BeautifulSoup(html, "xml")


# get max day temp for 5 days
for maxtemp in soup.find_all("Rep", string="Day"):
    maxtempday = (maxtemp.get('Dm'))
    maxtempdays.append(maxtempday)

temp0 = maxtempdays[0]
temp1 = maxtempdays[1]
temp2 = maxtempdays[2]
temp3 = maxtempdays[3]
temp4 = maxtempdays[4]

# get min temp night for 5 days
for mintemp in soup.find_all("Rep", string="Night"):
    mintempnight = (mintemp.get('Nm'))
    mintempnights.append(mintempnight)

mintemp0 = mintempnights[0]
mintemp1 = mintempnights[1]
mintemp2 = mintempnights[2]
mintemp3 = mintempnights[3]
mintemp4 = mintempnights[4]

# get wind direction for 5 days
for windir in soup.find_all("Rep", string="Day"):
    winddirs = (windir.get('D'))
    winddirections.append(winddirs)

winddir0 = winddirections[0]
winddir1 = winddirections[1]
winddir2 = winddirections[2]
winddir3 = winddirections[3]
winddir4 = winddirections[4]

# get max wind speed for 5 days
for maxwind in soup.find_all("Rep", string="Day"):
    maxwindday = (maxwind.get('S'))
    maxwinddays.append(maxwindday)

wind0 = maxwinddays[0]
wind1 = maxwinddays[1]
wind2 = maxwinddays[2]
wind3 = maxwinddays[3]
wind4 = maxwinddays[4]

# get max wind speed for 5 days
for rain in soup.find_all("Rep", string="Day"):
    rainpro = (rain.get('PPd'))
    rainprob.append(rainpro)

rain0 = rainprob[0]
rain1 = rainprob[1]
rain2 = rainprob[2]
rain3 = rainprob[3]
rain4 = rainprob[4]

# get weather type for 5 days
for weathertype in soup.find_all("Rep", string="Day"):
    weathertypeday = (weathertype.get('W'))
    weathertypedays.append(weathertypeday)

weather0 = int(weathertypedays[0])
weather1 = int(weathertypedays[1])
weather2 = int(weathertypedays[2])
weather3 = int(weathertypedays[3])
weather4 = int(weathertypedays[4])

today = datetime.date.today()
daynext0 = datetime.date.today() + datetime.timedelta(days=0)
daynext0day = daynext0.strftime("%a")
daynext1 = datetime.date.today() + datetime.timedelta(days=1)
daynext1day = daynext1.strftime("%a")
daynext2 = datetime.date.today() + datetime.timedelta(days=2)
daynext2day = daynext2.strftime("%a")
daynext3 = datetime.date.today() + datetime.timedelta(days=3)
daynext3day = daynext3.strftime("%a")
daynext4 = datetime.date.today() + datetime.timedelta(days=4)
daynext4day = daynext4.strftime("%a")

current_day_date = today.strftime("%a %d/%m/%y")

root = Tk()
root.title('IMAGES')
root.geometry('648x480')
root.configure(background='white')

w0im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/0im.png"))
w1im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/1im.png"))
w2im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/2im.png"))
w3im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/3im.png"))
w4im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/4im.png"))
w5im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/5im.png"))
w6im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/6im.png"))
w7im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/7im.png"))
w8im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/8im.png"))
w9im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/9im.png"))
w10im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/10im.png"))
w11im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/11im.png"))
w12im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/12im.png"))
w13im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/13im.png"))
w14im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/14im.png"))
w15im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/15im.png"))
w16im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/16im.png"))
w17im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/17im.png"))
w18im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/18im.png"))
w19im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/19im.png"))
w20im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/20im.png"))
w21im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/21im.png"))
w22im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/22im.png"))
w23im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/23im.png"))
w24im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/24im.png"))
w25im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/25im.png"))
w26im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/26im.png"))
w27im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/27im.png"))
w28im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/28im.png"))
w29im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/29im.png"))
w30im = ImageTk.PhotoImage(Image.open("/home/moneyo/Documents/Python/day_to_day/weather icons/30im.png"))

weatherimages = (w0im, w1im, w2im, w3im, w4im, w5im, w6im, w7im, w8im, w9im, w10im, w11im, w12im, w13im, w14im, w15im, w16im, w17im, w18im, w19im, w20im, w21im, w22im, w23im, w24im, w25im, w26im, w27im, w28im, w29im, w30im)

image0 = (weatherimages[weather0])
image1 = (weatherimages[weather1])
image2 = (weatherimages[weather2])
image3 = (weatherimages[weather3])
image4 = (weatherimages[weather4])


day_date_label = Label(text=current_day_date, background='white', font=('Arial', 25))

daynext0day_label = Label(text="Today", background='white', font=('Arial', 15), width=8)
daynext1day_label = Label(text=daynext1day, background='white', font=('Arial', 15), width=8)
daynext2day_label = Label(text=daynext2day, background='white', font=('Arial', 15), width=8)
daynext3day_label = Label(text=daynext3day, background='white', font=('Arial', 15), width=8)
daynext4day_label = Label(text=daynext4day, background='white', font=('Arial', 15), width=8)

my_label00 = Label(image=image0, background='white')
my_label01 = Label(image=image1, background='white')
my_label02 = Label(image=image2, background='white')
my_label03 = Label(image=image3, background='white')
my_label04 = Label(image=image4, background='white')

templabel00 = Label(text=temp0 + "\u00b0C" + " / " + mintemp0 + "\u00b0C", background='white', font=('Arial', 15), width=9)
templabel01 = Label(text=temp1 + "\u00b0C" + " / " + mintemp1 + "\u00b0C", background='white', font=('Arial', 15), width=9)
templabel02 = Label(text=temp2 + "\u00b0C" + " / " + mintemp2 + "\u00b0C", background='white', font=('Arial', 15), width=9)
templabel03 = Label(text=temp3 + "\u00b0C" + " / " + mintemp3 + "\u00b0C", background='white', font=('Arial', 15), width=9)
templabel04 = Label(text=temp4 + "\u00b0C" + " / " + mintemp4 + "\u00b0C", background='white', font=('Arial', 15), width=9)

windrainlabel00 = Label(text=wind0 + " " + winddir0 + "  /  " + rain0 + "%", background='white', font=('Arial', 10), width=14)
windrainlabel01 = Label(text=wind1 + " " + winddir1 + "  /  " + rain1 + "%", background='white', font=('Arial', 10), width=14)
windrainlabel02 = Label(text=wind2 + " " + winddir2 + "  /  " + rain2 + "%", background='white', font=('Arial', 10), width=14)
windrainlabel03 = Label(text=wind3 + " " + winddir3 + "  /  " + rain3 + "%", background='white', font=('Arial', 10), width=14)
windrainlabel04 = Label(text=wind4 + " " + winddir4 + "  /  " + rain4 + "%", background='white', font=('Arial', 10), width=14)


day_date_label.place(x=224, y=10)

templabel00.place(x=20, y=170)
templabel01.place(x=147, y=170)
templabel02.place(x=274, y=170)
templabel03.place(x=401, y=170)
templabel04.place(x=528, y=170)

my_label00.place(x=20, y=70)
my_label01.place(x=147, y=70)
my_label02.place(x=274, y=70)
my_label03.place(x=401, y=70)
my_label04.place(x=528, y=70)

windrainlabel00.place(x=20, y=200)
windrainlabel01.place(x=147, y=200)
windrainlabel02.place(x=274, y=200)
windrainlabel03.place(x=401, y=200)
windrainlabel04.place(x=528, y=200)

daynext0day_label.place(x=20, y=222)
daynext1day_label.place(x=147, y=222)
daynext2day_label.place(x=274, y=222)
daynext3day_label.place(x=401, y=222)
daynext4day_label.place(x=528, y=222)

root.mainloop()