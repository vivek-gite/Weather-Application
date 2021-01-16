import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


def weather_info(weather):
    try:
        sky = weather['weather'][0]['main']
        name = weather['name']
        temp = weather['main']['temp']
        final = 'Sky:%s \nCity:%s \nTemperature(°C):%s' % (sky, name, temp)

    except:
        final = "check the city and \ncountry name and\n try again"
    return final


def weather_api(city):
    weather_key = '458f14059399ddb9f9444e366f872a2f'
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {'APPID': weather_key, 'q': city,
             'units': 'Metric'}  # we are creating params because params sends the request from the server
    response = requests.get(url, params=param)
    weather = response.json()

    data = weather_info(weather)
    label['text'] = data  # label['text'] is used to access the text argument..

    icon = weather['weather'][0]['icon']
    open_image(icon)

def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img

top = tk.Tk()

top.title("Weather Application")

Canvas = tk.Canvas(top, height=700, width=800)
Canvas.pack()

background_image = tk.PhotoImage(file="./img/landscape.png")
background_label = tk.Label(top, image=background_image)
background_label.place(relheight=1, relwidth=1)

Frame = tk.Frame(top, bg="lightblue", bd=5)
Frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

Entry = tk.Entry(Frame,
                 font="verdana")  # we used 'Frame' as parameter because we want to use Entery box in the frame container with 0.65 of the
# width of the frame and 1 as height i.e full height of the height
Entry.place(relheight=1, relwidth=0.65)

button = tk.Button(Frame, text="Get Weather", command=lambda: weather_api(Entry.get()))
button.place(relx=0.70, relheight=1, relwidth=0.29)

lower_frame = tk.Frame(top, bg="lightblue", bd=5)  # bd is used to create a border ,by deafult bd is 2.
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

label = tk.Label(lower_frame, font=('verdana', 35), justify='left', anchor='nw')
label.place(relheight=1, relwidth=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

top.mainloop()
