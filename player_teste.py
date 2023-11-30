import tkinter as tk
import pygame

def play_music():
    question = entry.get().lower()
    pygame.init()

    if question == 'karma butterfly':
        pygame.mixer.music.load('Karma Butterfly - Girls Generation.mp3')
    elif question == 'koe':
        pygame.mixer.music.load('Sadie_-_Koe.mp3')
    elif question == 'day n night':
        pygame.mixer.music.load('07. Day _ Night.mp3')
    else:
        result_label.config(text='Música indisponível. Tente novamente.')
        return

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.quit()


root = tk.Tk()
root.title("Reprodutor de Música")

label = tk.Label(root, text='Qual música deseja ouvir?')
label.pack()

entry = tk.Entry(root)
entry.pack()

play_button = tk.Button(root, text="Reproduzir", command=play_music)
play_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
