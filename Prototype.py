
import tkinter.font as font      # This lets us use different fonts.
# Importing necessary packages
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog, font
from PIL import ImageTk, Image
from PyDictionary import PyDictionary
from googletrans import Translator
import requests
import json


# Defining Browse() to select a
# destination folder to save the video

def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining Download() to download the video
def Download():
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()

    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)

    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.first()

    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining Download() to download the video
def Download():
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()

    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()

    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)

    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.first()

    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


def center_window_on_screen():
    """
    This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below.
    :return: Nothing
    """
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def change_to_work():
    """
    This function swaps from the quiz
    frame to the work frame.
    :return: Nothing
    """
    quiz_frame.forget()
    work_frame.pack(fill='both', expand=1)


def change_to_quiz():
    """
    This function swaps from the work
    frame to the quiz frame.
    :return: Nothing
    """
    quiz_frame.pack(fill='both', expand=1)
    work_frame.forget()

def change_to_dict():
    """
    This function swaps from the work
    frame to the quiz frame.
    :return: Nothing
    """
    quiz_frame.forget()
    dict_frame.pack(fill='both', expand=1)


#root = tk.Tk()
#root.title('Dictionary')
#root.geometry('600x300')
#root['bg'] = 'white'
#frame = Frame(root, width=200, height=300, borderwidth=1, relief=RIDGE)
#frame.grid(sticky="W")


def get_meaning():
    dictionary = PyDictionary()
    get_word = entry.get()
    langauages = langauage.get()

    if get_word == "":
        messagebox.showerror('Dictionary', 'please write the word')

    elif langauages == 'English-to-English':
        d = dictionary.meaning(get_word)
        output.insert('end', d['Noun'])

    elif langauages == 'English-to-Hindi':
        translator = Translator()
        t = translator.translate(get_word, dest='hi')
        output.insert('end', t.text)


# Now we get to the program itself:-
# Let's set up the window ...

# API Integration --------------------------------------------------------------------

# defining the api-endpoint
API_ENDPOINT = "http://cs361translator.wl.r.appspot.com/translate"


# data to be sent to api
data2 = {
        "q": "Hello and welcome to the Handy Application Bundle!",
        "target": "ko",
        "source": "en"
        }

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, json=data2)
response = r.json()

print(response['translation'])


root = tk.Tk()
root.title("My Work - Swapping frames")
root.configure(bg='lightyellow')
# Set the icon used for your program


width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

# Here, we create two frames of which only
# one will be visible at a time.
quiz_frame = tk.Frame(root)
work_frame = tk.Frame(root)
dict_frame = tk.Frame(root)

# Let's create the fonts that we need.
font_large = font.Font(family='Georgia',
                       size='24',
                       weight='bold')
font_small = font.Font(family='Georgia',
                       size='12')

# The widgets needed for the quiz frame.
# First, let's display te logo.
img_logo = tk.PhotoImage(file='youtube.png')
lbl_logo_quiz = tk.Label(quiz_frame)

# Next, comes the heading for this frame.
#lbl_heading_quiz = tk.Label(quiz_frame,
#                            text='This is the Starting Page',
#                            font=font_large)
#lbl_logo_quiz.pack(pady=20)
#lbl_heading_quiz.pack(pady=20)

lbl_welcome_tsl = tk.Label(quiz_frame,
                            text=response['translation'],
                            font=font_small)
lbl_logo_quiz.pack(pady=20)
lbl_welcome_tsl.pack(pady=20)

lbl_instruct = tk.Label(quiz_frame, text='This is a collective application featuring several useful capabilities!')
lbl_logo_quiz.pack(pady=10)
lbl_instruct.pack(pady=3)

lbl_instruct = tk.Label(quiz_frame, text='Please click from the options below which feature you want to use.')
lbl_logo_quiz.pack(pady=10)
lbl_instruct.pack(pady=3)

# And finally, the button to swap between the frames.
btn_change_to_work = tk.Button(quiz_frame,
                               text='Go to Download Page',
                               font=font_small,
                               command=change_to_work)
btn_change_to_work.pack(pady=20)

btn_change_to_dict = tk.Button(quiz_frame,
                               text='Go to Dictionary',
                               font=font_small,
                               command=change_to_dict)
btn_change_to_dict.pack(pady=20)

# The widgets needed for the work frame.
# These are only being used in this example
# to show that both frames are working as
# expected.

video_Link = StringVar()
download_Path = StringVar()

link_label = Label(work_frame,
                       text="YouTube link  :",
                       bg="#E8D579")
link_label.pack()

root.linkText = Entry(work_frame,
                      width=55,
                      textvariable=video_Link)
root.linkText.pack()

destination_label = Label(work_frame,
                          text="Destination    :",
                          bg="#E8D579")
destination_label.pack()

root.destinationText = Entry(work_frame,
                             width=40,
                             textvariable=download_Path)
root.destinationText.pack()

browse_B = Button(work_frame,
                  text="Browse",
                  command=Browse,
                  width=10,
                  bg="#05E8E0")
browse_B.pack()

Download_B = Button(work_frame,
                    text="Download",
                    command=Download,
                    width=20,
                    bg="#05E8E0")
Download_B.pack()

# Next, we'll add a heading.
lbl_heading_work = tk.Label(work_frame,
                            text='This is the Download page',
                            font=font_large)
lbl_heading_work.pack(pady=20)

lbl_step1 = tk.Label(work_frame, text='Step 1: Enter the URL of the youtube video you wish to download')
lbl_logo_quiz.pack(pady=10)
lbl_step1.pack(pady=3)

lbl_step2 = tk.Label(work_frame, text='Step 2: Click the browse button and select the file destination for your mp4 file')
lbl_logo_quiz.pack(pady=10)
lbl_step2.pack(pady=3)

lbl_step3 = tk.Label(work_frame, text='Step 3: Click the download button and wait a bit, and you are done!')
lbl_logo_quiz.pack(pady=10)
lbl_step3.pack(pady=3)

# Finally, we need the button to
# swap back to the quiz frame.
btn_change_to_quiz = tk.Button(work_frame,
                               font=font_small,
                               text='Back to main menu',
                               command=change_to_quiz)
btn_change_to_quiz.pack(pady=20)

# Only the quiz frame needs to be shown
# when the program starts.  The work frame
# will only appear when the Change button
# is clicked.
quiz_frame.pack(fill='both', expand=1)


#Dictionary frame components:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


word = tk.Label(dict_frame, text="Enter Word", bg="white", font=('verdana', 10, 'bold'))
word.pack(pady = 5)

a = tk.StringVar()
langauage = ttk.Combobox(dict_frame, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'), )

langauage['values'] = (
    'English-to-English',
    'English-to-Hindi',

)

langauage.pack(pady = 5)
langauage.current(0)

entry = Entry(dict_frame, width=50, borderwidth=2, relief=RIDGE)
entry.pack(pady = 5)

search = Button(dict_frame, text="Search", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=get_meaning)
search.pack(pady = 5)

quit = Button(dict_frame, text="Quit", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=quit)
quit.pack(pady = 5)

meaning = Label(dict_frame, text="Meaning", bg="white", font=('verdana', 15, 'bold'))
meaning.pack(pady = 5)

output = Text(dict_frame, height=8, width=40, borderwidth=2, relief=RIDGE)
output.place(x=230, y=160)

root.mainloop()