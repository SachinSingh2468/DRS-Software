import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils

# height and width of the main screen starts here
SET_WIDTH=739
SET_HEIGHT=415

# GUI section
window = tkinter.Tk()
window.title("Third Umpire Decision Review System Software")
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("download (3).jpeg"), cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
canvas_image = canvas.create_image(0,0,ancho = tkinter.NW, image = photo)
canvas.pack()

#play function
def play(speed):
    print(f"The currently speed of video is {speed}")

#out function
def out():
    thread = threading.Thread(target=pending, args=("OUT"))
    thread.daemon = 1
    thread.start()
    print("confirm OUT ")

# not_out function
def not_out():
    thread = threading.Thread(target=pending, args=("NOT OUT"))
    thread.daemon = 1
    thread.start()
    print("confirm NOT OUT ")

# decision pending function
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("decision_pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)

    time.sleep(1)
    if decisionImgVar == "OUT":
         decisionImgVar = "out.png"
    else:
        decisionImgVar = "notout.png"
    frame = cv2.cvtColor(cv2.imread("decisionImgVar"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)


    
#Button section
btn = tkinter.Button(window, text="<<< Fast Prev", width=80, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="Fast Next >>>", width=80, command = partial(play, 20))
btn.pack()

btn = tkinter.Button(window, text="<< Slow Prev", width=80, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Slow Next >>", width=80, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Confirm for OUT", width=80, command = out)
btn.pack()

btn = tkinter.Button(window, text="Confirm for NOT OUT", width=80, command = not_out)
btn.pack()


window.mainloop()

