import tkinter.font as font      # This lets us use different fonts.
# Importing necessary packages
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog, font


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


# Now we get to the program itself:-
# Let's set up the window ...

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
lbl_heading_quiz = tk.Label(quiz_frame,
                            text='This is the Starting Page',
                            font=font_large)
lbl_logo_quiz.pack(pady=20)
lbl_heading_quiz.pack(pady=20)

lbl_welcome_tsl = tk.Label(quiz_frame,
                            text='안녕하십니까, 환영합니다!',
                            font=font_large)
lbl_logo_quiz.pack(pady=20)
lbl_welcome_tsl.pack(pady=20)

# And finally, the button to swap between the frames.
btn_change_to_work = tk.Button(quiz_frame,
                               text='Go to Download Page',
                               font=font_small,
                               command=change_to_work)
btn_change_to_work.pack(pady=20)

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

root.mainloop()