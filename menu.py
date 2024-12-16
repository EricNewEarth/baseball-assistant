# Imports
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import logo_paths
import standings
import team_page

team_logos = logo_paths.get_logos()

# Build menu window with team icons
def build_menu():

    # Create but hide the main window
    main_window = Tk()
    main_window.title("Baseball Assistant")
    main_window.resizable(False, False)
    window_width = 672
    window_height = 695

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    main_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    main_window.configure(bg = '#ffffff')

    # Add top label for displaying text
    title_label = Label(main_window, text = 'BASEBALL ASSISTANT', bg = 'white')
    title_label.configure(font = ('Anton', 48))
    title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5)  # Span across all columns

    # Add text labels for each division
    divisions = ['AL East', 'AL Central', 'AL West', 'NL East', 'NL Central', 'NL West']
    for i, division in enumerate(divisions):
        division_label = Label(main_window, text = division, bg = 'white')
        division_label.configure(font = ('Calibri', 14))
        division_label.grid(row = 1, column = i, padx = 5, pady = 2)

    # Grab all team images
    image_order = standings.get_image_order()
    team_images = create_images(image_order)

    # Create buttons with images
    buttons = []
    for index, image in enumerate(team_images):
        row = index // 6 # Calculate the row index
        col = index % 6 # Calculate the column index
        button = tk.Button(main_window, image=image, command=lambda idx=index: team_page.build_team_page(idx))
        button.grid(row=row + 2, column=col, padx=5, pady=2) # Shift row down 2 to make room for text
        buttons.append(button)
    
    main_window.mainloop()

# Create PhotoImage objects from team icon paths
def create_images(team_logos, size=(96, 96)):
    images = []
    for logo in team_logos:
        # Open PNG image data using PIL
        image = Image.open(logo)

        # Resize the image to the specified dimensions
        image = image.resize(size)

        # Convert image to PhotoImage
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)
        
    return images