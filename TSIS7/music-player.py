import pygame as py
import os

def play_next_song():
    global _currently_playing_song, songs
    py.mixer.music.stop
    if py.mixer.music.get_busy() == False:
        _currently_playing_song = songs[(songs.index(history[-1])+1)%len(songs)]        
    else:  
        _currently_playing_song = songs[(songs.index(_currently_playing_song)+1)%len(songs)]
    py.mixer.music.load("music/"+_currently_playing_song)
    history.append(_currently_playing_song)
    py.mixer.music.play()

def play_previous_song():
    global _currently_playing_song, songs
    if len(history)!=1:
        py.mixer.music.stop
        if py.mixer.music.get_busy() == False:
            _currently_playing_song = songs[(songs.index(history[-1])-1)%len(songs)]        
        else:  
            _currently_playing_song = songs[(songs.index(_currently_playing_song)-1)%len(songs)]
        py.mixer.music.load("music/"+_currently_playing_song)
        if len(history)!=0:
            del history[-1]
        py.mixer.music.play()


py.init()
py.display.set_mode((100,100))
done = True
playing = True
songs = []
history = []

for i in os.listdir("music"):
    if i.endswith(".mp3"):
        songs.append(i)
_currently_playing_song = songs[0]
py.mixer.music.load("music/"+_currently_playing_song)
py.mixer.music.play()
history.append(songs[0])
print(songs)
print(_currently_playing_song)
while done:
    
    for event in py.event.get():
          
        if event.type == py.KEYDOWN:    
            if event.key == py.K_ESCAPE:
                done = False
            if event.key == py.K_SPACE:
                if playing ==True:
                    py.mixer.music.pause()
                    playing = False
                else:
                    py.mixer.music.unpause()
                    playing = True
            if event.key == py.K_RIGHT:
                play_next_song()
            if event.key == py.K_LEFT:
                play_previous_song()
    print(_currently_playing_song)
    print(history)
    print(songs)

    py.display.update()