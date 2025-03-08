import standings
import team_page
import logo_paths
import pandas as pd
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

team_logos = logo_paths.logos

# Build menu window with team icons
def build_menu():

    # Create but hide the main window
    main_window = Tk()
    main_window.title('Baseball Assistant')
    main_window.resizable(False, False)
    window_width = 672
    window_height = 695

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    main_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coord, y_coord))
    main_window.configure(bg = '#ffffff')

    # Add top label for displaying text
    title_label = Label(main_window, text = 'BASEBALL ASSISTANT', bg = 'white', font = ('Anton', 48))
    title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5)  # Span across all columns

    # Add text labels for each division
    divisions = ['AL East', 'AL Central', 'AL West', 'NL East', 'NL Central', 'NL West']
    for i, division in enumerate(divisions):
        division_label = Label(main_window, text = division, bg = 'white', font = ('Calibri', 14))
        division_label.grid(row = 1, column = i, padx = 5, pady = 2)

    # Retrieve standings with image paths
    standings_list = standings.get_standings_images() 
    standings_df = pd.concat(standings_list, ignore_index=True)
    team_logos = standings_df['image'].tolist()
    team_images = create_images(team_logos)

    # Define grid dimensions
    num_columns = 6  # Number of columns in the grid
    num_rows = (len(team_images) + num_columns - 1) // num_columns  # Calculate necessary rows

    # Create buttons with images
    buttons = []
    team_names = standings_df['team_name'].tolist()  # Extract team names

    for index, (image, team_name) in enumerate(zip(team_images, team_names)):
        row = index % num_rows  # Fill column from top to bottom
        col = index // num_rows  # Move to the next column after filling the previous one

        # Create button with image and pass team_name to build_team_page
        button = tk.Button(main_window, image=image, command=lambda name=team_name: team_page.build_team_page(name))
        button.grid(row=row + 2, column=col, padx=5, pady=2)  # Shift row down 2 to make room for text
        buttons.append(button)

    main_window.mainloop()

# Create PhotoImage objects from team icon paths
def create_images(team_logos, size=(96, 96)):
    images = []
    for logo in team_logos:
        try:
            # Open PNG image data using PIL
            image = Image.open(logo)

            # Resize the image to the specified dimensions
            image = image.resize(size)

            # Convert image to PhotoImage
            photo_image = ImageTk.PhotoImage(image)
            images.append(photo_image)
        except Exception as e:
            print(f'Error loading {logo}: {e}')
        
    return images