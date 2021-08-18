from tkinter import *
from tkinter import messagebox
import main
import sys

#FIXME Notes to do:
"""
1. create a way to remove songs artists and genres
"""

bg_color = 'black'
fg_color = 'pale green'
font_code = ('Gill Sans MT', 20)                                            
font_code12 = ('Gill Sans MT', 12)
font_code10 = ('Gill Sans MT', 10)
font_code8 = ('Gill Sans MT', 8)

def clear_frame():
   for widgets in window.winfo_children():
      widgets.destroy()

def home_window():
    window.title('Spotify Algorithm Playlist Maker')
    clear_frame()
    song_list = tag_list.get_song_names()
    artist_list = tag_list.get_artist_names()
    genre_list = tag_list.genres

    #creating all labels and buttons
    label = Label(text='Welcome to the Spotify reccommended music playlist generator.', fg=fg_color, bg=bg_color, font=font_code) 
    label2 = Label(text='You can choose up to 5 total songs, artists, and genres to input into the algorithm for a playlist to be automatically generated', bg=bg_color, fg=fg_color, font=font_code12)
    song_label = Label(text=f'songs: {song_list}', bg=bg_color, fg=fg_color, font=font_code)
    artist_label = Label(text=f'artists: {artist_list}', bg=bg_color, fg=fg_color, font=font_code)
    genre_label = Label(text=f'genres: {genre_list}', bg=bg_color, fg=fg_color, font=font_code)
    song_button = Button(text='Search for Songs', command=song_window, bg=bg_color, fg=fg_color, font=font_code)
    artists_button = Button(text='Search for artists', command=artist_window, bg=bg_color, fg=fg_color, font=font_code)
    genre_button = Button(text='Browse all Spotify genres', command=genre_window, bg=bg_color, fg=fg_color, font=font_code)
    
    #if there is no song, artist, or genre entered grey out the submit button
    if len(song_list) + len(artist_list) + len(genre_list) > 0:
        submit_button = Button(text='Submit List and Enter Parameters', command=lambda: param_window(song_list, artist_list, genre_list), bg=bg_color, fg=fg_color, font=font_code)
    else:
        submit_button = Button(text='Submit List and Enter Parameters', state=DISABLED, command=lambda: param_window(song_list, artist_list, genre_list), bg=bg_color, fg=fg_color, font=font_code)
    
    #putting everything into the window
    label.pack(fill=BOTH, expand=True)
    label2.pack(fill=BOTH, expand=True)
    song_label.pack(fill=BOTH, expand=True)
    artist_label.pack(fill=BOTH, expand=True)
    genre_label.pack(fill=BOTH, expand=True)
    song_button.pack(fill=BOTH, expand=True)
    artists_button.pack(fill=BOTH, expand=True)
    genre_button.pack(fill=BOTH, expand=True)
    submit_button.pack(fill=BOTH, expand=True)

#Search for Songs
#add song to list
def add_songs(num):
    messagebox.showinfo('', tag_list.add_song(song_client.song_ids[num], song_client.song_names[num]))

#search for list of songs
def search_songs():
    global button1
    global button2
    global button3
    global button4
    global button5
    global song_ids
    global songs
    global song_client

    song_client = main.search_song(song_search_bar.get())
    try:
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
    except Exception:
        pass
    button1 = Button(text=f'1. {song_client.artist_names[0]}: {song_client.song_names[0]}', command=lambda: add_songs(0), fg=fg_color, bg=bg_color, font=font_code12)
    button2 = Button(text=f'2. {song_client.artist_names[1]}: {song_client.song_names[1]}', command=lambda: add_songs(1), fg=fg_color, bg=bg_color, font=font_code12)
    button3 = Button(text=f'3. {song_client.artist_names[2]}: {song_client.song_names[2]}', command=lambda: add_songs(2), fg=fg_color, bg=bg_color, font=font_code12)
    button4 = Button(text=f'4. {song_client.artist_names[3]}: {song_client.song_names[3]}', command=lambda: add_songs(3), fg=fg_color, bg=bg_color, font=font_code12)
    button5 = Button(text=f'5. {song_client.artist_names[4]}: {song_client.song_names[4]}', command=lambda: add_songs(4), fg=fg_color, bg=bg_color, font=font_code12)
    button1.grid(row=3, column=0, sticky=W)
    button2.grid(row=4, column=0, sticky=W)
    button3.grid(row=5, column=0, sticky=W)
    button4.grid(row=6, column=0, sticky=W)
    button5.grid(row=7, column=0, sticky=W)

#search for songs window
def song_window():
    global song_search_bar
    clear_frame()
        
    window.title('Search for Songs')
    label = Label(text='Search for Songs', fg=fg_color, bg=bg_color, font=font_code)
    song_search_bar = Entry(width=80, borderwidth=2)
    search_button = Button(text='Search', padx=50, pady=5, command=search_songs, fg=fg_color, bg=bg_color, font=font_code)
    home_button = Button(text='Home', padx=20, pady=5, command=home_window, fg=fg_color, bg=bg_color, font=font_code)

    label.grid(row=0, column=0)
    song_search_bar.grid(row=1, column=0, columnspan=3)
    search_button.grid(row=2, column=0)
    home_button.grid(row=8, column=3)

#Search for Artists
#Add artist to list
def add_artists(num):
        messagebox.showinfo('', tag_list.add_artist(artist_client.artist_ids[num], artist_client.artist_names[num]))

#search for list of artists
def search_artists():
    global button1
    global button2
    global button3
    global button4
    global button5
    global artist_client

    try:
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        button5.destroy()
    except Exception:
        pass

    artist_client = main.search_artist(artist_search_bar.get())
    button1 = Button(text=f'1. {artist_client.artist_names[0]}', command=lambda: add_artists(0), fg=fg_color, bg=bg_color, font=font_code12)
    button1.grid(row=3, column=0, sticky=W)
    if len(artist_client.artist_names) > 1:
        button2 = Button(text=f'2. {artist_client.artist_names[1]}', command=lambda: add_artists(1), fg=fg_color, bg=bg_color, font=font_code12)
        button2.grid(row=4, column=0, sticky=W)
    if len(artist_client.artist_names) > 2:
        button3 = Button(text=f'3. {artist_client.artist_names[2]}', command=lambda: add_artists(2), fg=fg_color, bg=bg_color, font=font_code12)
        button3.grid(row=5, column=0, sticky=W)
    if len(artist_client.artist_names) > 3:
        button4 = Button(text=f'4. {artist_client.artist_names[3]}', command=lambda: add_artists(3), fg=fg_color, bg=bg_color, font=font_code12)
        button4.grid(row=6, column=0, sticky=W)
    if len(artist_client.artist_names) > 4:
        button5 = Button(text=f'5. {artist_client.artist_names[4]}', command=lambda: add_artists(4), fg=fg_color, bg=bg_color, font=font_code12)
        button5.grid(row=7, column=0, sticky=W)

#Artist window
def artist_window():
    global artist_search_bar
    clear_frame()
    
    window.title('Search for Artists')
    label = Label(text='Search for Artists', fg=fg_color, bg=bg_color, font=font_code)
    artist_search_bar = Entry(width=80, borderwidth=2, relief=SUNKEN)
    search_button = Button(text='Search', padx=50, pady=5, command=search_artists, fg=fg_color, bg=bg_color, font=font_code)
    home_button = Button(text='Home', padx=20, pady=5, command=home_window, fg=fg_color, bg=bg_color, font=font_code)

    label.grid(row=0, column=0)
    artist_search_bar.grid(row=1, column=0, columnspan=3)
    search_button.grid(row=2, column=0)
    home_button.grid(row=8, column=3, sticky=E)

#Search for Genres
#add genre to list
def add_genres():
    if genre_search_bar.get().lower() in genre_client.genre_names:
        messagebox.showinfo('Success', tag_list.add_genre(genre_search_bar.get().lower()))
    else:
        messagebox.showerror('Error', 'Invalid Genre Entry')

#get a list of all genres
def genres():
    global genre_client
    genre_client = main.search_genres()
    popup = Toplevel()
    popup.title('All Valid Spotify Genres')

    for num, item in enumerate(genre_client.genre_names):
        global genre_label
        row_num = num // 6
        genre_label = Label(popup, text=item, fg=fg_color, bg=bg_color, font=font_code10)
        genre_label.grid(column=num%6, row=row_num, sticky=NSEW)

#display the genre search window
def genre_window():
    global genre_search_bar
    clear_frame()

    window.title('Spotify Genre Selection')
    
    genre_search_bar = Entry(width=60)
    label = Label(text='Enter a genre to add to the list', fg=fg_color, bg=bg_color, font=font_code)
    enter_button = Button(text='Add genre to list', command=add_genres, fg=fg_color, bg=bg_color, font=font_code)
    home_button = Button(text='Home', padx=20, pady=5, command=home_window, fg=fg_color, bg=bg_color, font=font_code)
    genres_button = Button(text='see a list of all genres', command=genres, fg=fg_color, bg=bg_color, font=font_code)

    label.grid(row=0, column=0, columnspan=3)
    enter_button.grid(column=0, row=2)
    genres_button.grid(row=3, column=0)
    genre_search_bar.grid(row=1, column=0, columnspan=3)
    home_button.grid(column=2, row=3, sticky=E)

def param_window(tracks, artists, genres):
    list = ['Acousticness', 'Danceability', 'Energy', 'Instrumentallness', 'Liveness', 'Loudness', '   Key   ', 'Tempo', 'popularity']
    clear_frame()
    for num, param in enumerate(list):
        label = Label(text=param, bg=bg_color, fg=fg_color, font=font_code).grid(row=0, column=num)
    global slider1, slider2, slider3, slider4, slider5, slider6, slider7, slider8
    slider1 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider2 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider3 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider4 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider5 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider6 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)
    slider7 = Scale(from_=300, to=1, bg=bg_color, fg=fg_color)
    slider8 = Scale(from_=100, to=0, bg=bg_color, fg=fg_color)

    #creating radio boxes for key
    global key
    key = StringVar()
    key.set('none')
    frame = Frame(bg=bg_color)
    major = Radiobutton(frame, text='Major', variable=key, fg=fg_color, selectcolor='black', value=1, bg=bg_color, font=font_code12)
    minor = Radiobutton(frame, text='Minor', variable=key, value=0, fg=fg_color, selectcolor='black', bg=bg_color, font=font_code12)

    #checkboxes for enabling each parameter
    global key1, key2, key3, key4, key5, key6, key7, key8, key9
    key1 = IntVar()
    box1 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key1)
    key2 = IntVar()
    box2 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key2)
    key3 = IntVar()
    box3 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key3)
    key4 = IntVar()
    box4 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key4)
    key5 = IntVar()
    box5 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key5)
    key6 = IntVar()
    box6 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key6)
    key7 = IntVar()
    box7 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key7)
    key8 = IntVar()
    box8 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key8)
    key9 = IntVar()
    box9 = Checkbutton(text='enable', bg=bg_color, font=font_code12, fg=fg_color, selectcolor='Black', variable=key9)
    continue_button = Button(text='Continue', command=num_songs, bg=bg_color, fg=fg_color, font=font_code)
    home_button = Button(text='Home', padx=20, pady=5, command=home_window, fg=fg_color, bg=bg_color, font=font_code)

    #putting everything in window with grid
    slider1.grid(row=1, column=0, sticky=NSEW)
    slider2.grid(row=1, column=1, sticky=NSEW)
    slider3.grid(row=1, column=2, sticky=NSEW)
    slider4.grid(row=1, column=3, sticky=NSEW)
    slider5.grid(row=1, column=4, sticky=NSEW)
    slider6.grid(row=1, column=5, sticky=NSEW)
    frame.grid(row=1, column=6, sticky=NSEW)
    major.pack()
    minor.pack()
    slider7.grid(row=1, column=7, sticky=NSEW)
    slider8.grid(row=1, column=8, sticky=NSEW)
    box1.grid(row=2, column=0, sticky=NSEW)
    box2.grid(row=2, column=1, sticky=NSEW)
    box3.grid(row=2, column=2, sticky=NSEW)
    box4.grid(row=2, column=3, sticky=NSEW)
    box5.grid(row=2, column=4, sticky=NSEW)
    box6.grid(row=2, column=5, sticky=NSEW)
    box7.grid(row=2, column=6, sticky=NSEW)
    box8.grid(row=2, column=7, sticky=NSEW)
    box9.grid(row=2, column=8, sticky=NSEW)
    continue_button.grid(row=3, column=8, sticky=NSEW)
    home_button.grid(row=3, column=0, sticky=NSEW)

def create_playlist():
        playlist_create = main.add_to_playlist(recs.get_rec_uris(), playlist_name.get())
        num_songs_added = messagebox.showinfo('Success', f'{len(recs.get_rec_uris())} songs added to {playlist_name.get()}')
        sys.exit()

#FIXME maked wolf: astronaut in the ocean song add 40 songs you only get 37
#less songs being added to playlist than shown
#
def add_to_playlist():
    global playlist_name
    clear_frame()
    label = Label(text='Enter Playlist Name', font=font_code, bg=bg_color, fg=fg_color)
    playlist_name = Entry()
    submit = Button(text='Enter', font=font_code, bg=bg_color, fg=fg_color, command=create_playlist)

    label.grid(row=0, column=0)
    playlist_name.grid(row=1, column=0)
    submit.grid(row=2, column=1)

def clear_search():
    clear_frame()

    #gui elements
    label = Label(text='Enter the amount of songs you would like to see', font=font_code, bg=bg_color, fg=fg_color)
    label2 = Label(text='(between 1 - 100)', font=font_code10, bg=bg_color, fg=fg_color)
    num_songs_entry = Entry()
    #command for back button must remove everything from params dictionary and from query params dict in main
    #every back button will have to do stuf like this so they will take longer
    back_button = Button(text='Home', font=font_code, bg=bg_color, fg=fg_color, command=back)
    search_button = Button(text='Search', font=font_code, command=lambda: rec_search(num_songs_entry.get()), bg=bg_color, fg=fg_color)

    #putting everything in the window
    label.grid(row=0, column=1, sticky=NSEW)
    label2.grid(row=1, column=1, sticky=NSEW)
    num_songs_entry.grid(row=2, column=1, sticky=NSEW)
    search_button.grid(row=3, column=3, sticky=NSEW)
    back_button.grid(row=3, column=0, sticky=NSEW)

#display window with number of songs to display asked
def rec_search(num):
    try:
        num = int(num)
        if num < 1:
            messagebox.showerror('Error', 'number must be greater than 0')
        elif num > 100:
            messagebox.showerror('Error', 'number must be less than 100')
        else:
            #FIXME numbers over 60 work but you can't see the top of the screen
            #unsure if you can fix this in tkinter or do a scroll but clear button makes this ok for now
            #very low priority for now
            global recs
            recs = main.get_reccommendations(num, tag_list.songs, tag_list.artists, tag_list.genres, params)
            for num, item in enumerate(recs.get_rec_names()):
                global song_label
                row_num = num // 3
                song_label = Label(text=item, font=font_code8, bg=bg_color, fg=fg_color)
                song_label.grid(row=row_num+3, column=num%3, sticky=NSEW)
            redo = Button(text='Clear Search', command=clear_search, font=font_code, bg=bg_color, fg=fg_color)
            playlist = Button(text='Add to Playlist', command=add_to_playlist, font=font_code, bg=bg_color, fg=fg_color)
            redo.grid(row=100, column=0)
            playlist.grid(row=100, column=2)

    #exception in case a non number is entered
    except Exception:
        messagebox.showerror('Error', 'You must enter a valid number')

def back():
    home_window()

def num_songs():
    global params
    #getting the data from the sliders
    params = {}
    # Acousticness
    if key1.get() == 1:
        params['target_acousticness'] = slider1.get()
    # Danceability
    if key2.get() == 1:
        params['target_danceability'] = slider2.get()
    # Energy
    if key3.get() == 1:
        params['target_energy'] = slider3.get()
    # Instrumentallness
    if key4.get() == 1:
        params['target_instrumentalness'] = slider4.get()
    # Liveness
    if key5.get() == 1:
        params['target_liveness'] = slider5.get()
    # Loudness
    if key6.get() == 1:
        params['target_loudness'] = slider6.get()
    # Mode
    if key7.get() == 1:
        #major = 1 minor = 0
        params['target_mode'] = key.get()
    # Tempo
    if key8.get() == 1:
        params['target_tempo'] = slider7.get()
    # Popularity
    if key9.get() == 1:
        params['target_popularity'] = slider8.get()
    
    clear_frame()

    label = Label(text='Enter the amount of songs you would like to see', font=font_code, bg=bg_color, fg=fg_color)
    label2 = Label(text='(between 1 - 100)', font=font_code10, bg=bg_color, fg=fg_color)
    num_songs_entry = Entry()
    #command for back button must remove everything from params dictionary and from query params dict in main
    #every back button will have to do stuf like this so they will take longer
    back_button = Button(text='Home', font=font_code, bg=bg_color, fg=fg_color, command=back)
    search_button = Button(text='Search', font=font_code, command=lambda: rec_search(num_songs_entry.get()), bg=bg_color, fg=fg_color)

    #putting everything in the window
    label.grid(row=0, column=1, sticky=NSEW)
    label2.grid(row=1, column=1, sticky=NSEW)
    num_songs_entry.grid(row=2, column=1, sticky=NSEW)
    search_button.grid(row=3, column=3, sticky=NSEW)
    back_button.grid(row=3, column=0, sticky=NSEW)

if __name__ == '__main__':
    tag_list = main.tag_list()
    window = Tk()
    window.configure(bg=bg_color)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)
    window.grid_rowconfigure(6, weight=1)
    window.grid_rowconfigure(7, weight=1)
    window.grid_rowconfigure(8, weight=1)
    window.grid_rowconfigure(9, weight=1)
    p1 = PhotoImage(file = 'spotify.png')
    # Setting icon of master window
    window.iconphoto(False, p1)
    window.resizable(True, True)
    if main.client.access_token == None:
        messagebox.showerror('Unable to Connect', 'Check your internet connection')
    home_window()
    window.mainloop()