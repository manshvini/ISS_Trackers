import ISS_Info
from pathlib import Path
import time
import turtle

screen = turtle.Screen()
screen.setup(width=720, height=360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic(str(Path(__file__).resolve().with_name("World_Converted.png")))
image_path = str(Path(__file__).resolve().with_name("ISS_Changed_Small.gif"))
screen.register_shape(image_path)

iss = turtle.Turtle()
iss.shape(image_path)
iss.penup()

while True:
    location = ISS_Info.iss_current_location()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("Position : \n latitude : ", lat, "\n longitude : ", lon)
    iss.goto(float(lon), float(lat))
    time.sleep(5)
    