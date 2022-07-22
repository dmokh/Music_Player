import pygame
import os
import random

width = 1100
height = 700

# colors
COLOR_THEME = (255, 200, 200)
BLUE = (0, 70, 200)
BLACK = (10, 0, 10)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
RED = (220, 0, 0)
TURQUOISE = pygame.Color('turquoise')
BEIGE = pygame.Color('beige')
BROWN = (196, 108, 108)
WHITE = (255, 255, 255)

# file parameters
path = "D:/Music/"

# play parameters
Play_fl = False
now_song = False
was_pause = False
now_time_seconds = 0.0
now_time_minutes = 0
pos_circle = 210
pos_of_music = 0
type_play = "All_of_playlist"
now_playlist = False
volume = 10
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pos = 20 * int(pygame.mixer.music.get_volume() * 10) + 500

# playlist parameters
fl_playlist = True

# delete
fl = False

import time
from mutagen.mp3 import MP3


def manager(screen):
    global now_time_minutes, now_time_seconds
    import time
    import win32api
    import pygame
    import os
    import subprocess
    width = 1000
    height = 400
    pygame.font.init()
    sc = pygame.Surface((width, height))
    direc = "C:/"
    wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
    disks = list(win32api.GetLogicalDriveStrings())
    v = len(wholes)
    File_which_is_choice_user = False
    n = 0
    while True:
        sc.fill((255, 100, 50))
        pygame.draw.rect(sc, (125, 125, 125), (200, 0, 50, height))
        for r in range(v):
            pygame.draw.rect(sc, (255, 255, 255), (250, r * 30 + n * 30, width - 250, 20))
            sc.blit(pygame.font.SysFont("Calibri", 15).render(wholes[r][0], False, (0, 0, 0)), (250, r * 30 + n * 30))
        for y in range(len(disks) // 4):
            pygame.draw.rect(sc, (255, 255, 255), (0, y * 30, 200, 30))
            sc.blit(pygame.font.SysFont("Calibri", 30).render(disks[y * 4], False, (0, 0, 0)), (0, y * 30))
        for t in pygame.event.get():
            if t.type == pygame.QUIT:
                if len(direc) > 4:
                    n = 0
                    a = -1
                    while a > (-len(direc)) and direc[a] != "/":
                        a -= 1
                    direc = direc[:a]
                    wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                    v = len(wholes)
                else:
                    exit(1)
            elif t.type == pygame.MOUSEBUTTONDOWN:
                cords = pygame.mouse.get_pos()
                if t.button == 1:
                    if cords[0] > 250 and cords[1] // 30 - n < v:
                        if wholes[cords[1] // 30 - n][1]:
                            direc = os.path.join(direc + "/" + wholes[cords[1] // 30 - n][0])
                            n = 0
                            try:
                                wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                            except PermissionError:
                                print(PermissionError)
                            except FileNotFoundError:
                                print(FileNotFoundError)
                            v = len(wholes)
                        elif os.path.join(direc + "/" + wholes[cords[1] // 30 - n][0]) != File_which_is_choice_user:
                            File_which_is_choice_user = os.path.join(direc + "/" + wholes[cords[1] // 30 - n][0])
                        else:
                            return File_which_is_choice_user
                    elif cords[0] < 200 and cords[1] // 30 < len(disks) // 4:
                        direc = str(disks[(cords[1] // 30) * 4]) + ":/"
                        wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                        v = len(wholes)
                elif t.button == 3:
                    if cords[0] > 250 and cords[1] // 30 - n < v:
                        time.sleep(0.2)
                        fl = True
                        while fl:
                            sc.fill((200, 150, 0))
                            pygame.draw.rect(sc, (125, 125, 125), (200, 0, 50, height))
                            for r in range(v):
                                pygame.draw.rect(sc, (255, 255, 255), (250, r * 30 + n * 30, width - 250, 20))
                                sc.blit(pygame.font.SysFont("Calibri", 15).render(wholes[r][0], False, (0, 0, 0)),
                                        (250, r * 30 + n * 30))
                            for y in range(len(disks) // 4):
                                pygame.draw.rect(sc, (255, 255, 255), (0, y * 30, 200, 30))
                                sc.blit(pygame.font.SysFont("Calibri", 30).render(disks[y * 4], False, (0, 0, 0)),
                                        (0, y * 30))
                            pygame.draw.rect(sc, (100, 255, 255), (cords[0], cords[1], 100, 100))
                            for u in pygame.event.get():
                                if u.type == pygame.MOUSEBUTTONDOWN:
                                    now_cords = pygame.mouse.get_pos()
                                    if (cords[0] + 100 > now_cords[0] > cords[0]) and (
                                            cords[1] + 100 > now_cords[1] > cords[1]) and u.button == 1 and not \
                                            wholes[cords[1] // 30 - n][1]:
                                        subprocess.Popen(("start", direc + "/" + wholes[cords[1] // 30 - n][0]),
                                                         shell=True)
                                        fl = False
                                    elif u.button == 3 and (cords[0] + 100 > now_cords[0] > cords[0]) and (
                                            cords[1] + 100 > now_cords[1] > cords[1]):
                                        os.chdir(direc + "/")
                                        if not wholes[cords[1] // 30 - n][1]:
                                            os.remove(direc + "/" + wholes[cords[1] // 30 - n][0])
                                            wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                                            v = len(wholes)
                                            fl = False
                                        else:
                                            if len(os.listdir(direc + "/" + wholes[cords[1] // 30 - n][0])) == 0:
                                                os.rmdir(direc + "/" + wholes[cords[1] // 30 - n][0])
                                        wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                                        v = len(wholes)
                                        fl = False
                                    else:
                                        fl = False
                            time.sleep(0.1)
                            pygame.display.flip()
                    elif cords[0] > 250:
                        time.sleep(0.2)
                        fl = True
                        while fl:
                            sc.fill((200, 150, 0))
                            pygame.draw.rect(sc, (125, 125, 125), (200, 0, 50, height))
                            for r in range(v):
                                pygame.draw.rect(sc, (255, 255, 255), (250, r * 30 + n * 30, width - 250, 20))
                                sc.blit(pygame.font.SysFont("Calibri", 15).render(wholes[r][0], False, (0, 0, 0)),
                                        (250, r * 30 + n * 30))
                            for y in range(len(disks) // 4):
                                pygame.draw.rect(sc, (255, 255, 255), (0, y * 30, 200, 30))
                                sc.blit(pygame.font.SysFont("Calibri", 30).render(disks[y * 4], False, (0, 0, 0)),
                                        (0, y * 30))
                            pygame.draw.rect(sc, (100, 255, 255), (cords[0], cords[1], 100, 100))
                            for u in pygame.event.get():
                                if u.type == pygame.MOUSEBUTTONDOWN:
                                    now_cords = pygame.mouse.get_pos()
                                    if (cords[0] + 100 > now_cords[0] > cords[0]) and (
                                            cords[1] + 100 > now_cords[1] > cords[1]) and u.button == 1:
                                        os.chdir(direc + "/")
                                        new_file = open("new_file.txt", "w")
                                        new_file.write("")
                                        new_file.close()
                                        wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                                        v = len(wholes)
                                        fl = False
                                    elif u.button == 3 and (cords[0] + 100 > now_cords[0] > cords[0]) and (
                                            cords[1] + 100 > now_cords[1] > cords[1]):
                                        os.chdir(direc + "/")
                                        if not os.path.isdir("New_folder"):
                                            os.mkdir("New_folder")
                                        wholes = [(x, os.path.isdir(direc + "/" + x)) for x in os.listdir(direc)]
                                        v = len(wholes)
                                        fl = False
                                    else:
                                        fl = False
                            time.sleep(0.1)
                            pygame.display.flip()
                elif t.button == 4:
                    if n < 0:
                        n += 1
                elif t.button == 5:
                    if len(wholes) > height // 30:
                        if n - 1 >= (-(len(wholes) - height // 30)):
                            n -= 1
        screen.blit(sc, (0, 0))
        now_time_minutes = (now_time_minutes * 60) // 60 + now_time_seconds // 60
        now_time_seconds = (now_time_seconds) % 60 + 0.1
        time.sleep(0.088)
        pygame.display.flip()


import mutagen
from mutagen.wave import WAVE

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.mixer.init(frequency=44200)

# songs file
song_file = open('songs_information.txt', "r+", encoding='windows-1251', errors="ignore")
songs_tech = song_file.readlines()
song_file.close()
songs = []
playlist_file = open('Playlist_info.txt', "r+", encoding='windows-1251', errors="ignore")
playlist_tech = playlist_file.readlines()
playlist_file.close()
Playlists = []
pygame.mixer.music.set_volume(1)


def new_playlist(screen):
    surf = pygame.Surface((500, 250))
    font_style_of_playlist_new = pygame.font.Font("HighVoltage Rough.ttf", 40)
    create_rect = pygame.Rect(210, 200, 100, 50)
    text = ""
    while True:
        surf.fill(WHITE)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit(1)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x_rect = pygame.Rect((pygame.mouse.get_pos()[0] - width // 2 + 250, pygame.mouse.get_pos()[1] - height // 2 + 125, 1, 1))
                if x_rect.colliderect(create_rect):
                    return text
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                else:
                    text += e.unicode
        surf.blit(font_style_of_playlist_new.render("Name of new playlist:", False, BLACK), (100, 0))
        pygame.draw.rect(surf, YELLOW, (210, 200, 100, 50))
        pygame.draw.lines(surf, YELLOW, True, ((50, 100), (450, 100), (450, 150), (50, 150)))
        surf.blit(font_style_of_playlist_new.render(text, False, BLACK), (50, 100))
        surf.blit(font_style_of_playlist_new.render("Create", False, BLACK), (210, 200))
        screen.blit(surf, (width // 2 - 250, height // 2 - 125))
        pygame.display.flip()
        time.sleep(0.1)

# buttons
class buttons:
    def __init__(self, color, type_button, cords, size, text, text_color):
        self.color = color
        self.type = type_button
        self.cords = cords
        self.size = size
        self.rect = pygame.Rect((cords[0], cords[1], size[0], size[1]))
        self.text = text
        if self.type == "Playlist":
            self.font_style = pygame.font.Font("HighVoltage Rough.ttf", 50)
        else:
            self.font_style = pygame.font.Font("HighVoltage Rough.ttf", max(size) // 3)
        self.text_color = text_color

    def draw(self, pos):
        pygame.draw.rect(screen, self.color, pos + self.size)
        font_render = self.font_style.render(self.text, False, self.text_color)
        screen.blit(font_render, (pos[0] + 42 if self.type != 'Playlist' else pos[0] + 20, pos[1] + 30))

    def get_click(self, pos):
        global fl, song_file, fl_playlist, pos_of_music, now_playlist, songs
        song_file = open("songs_information.txt", "a")
        cords_of_mouse = pygame.mouse.get_pos()
        rect_of_mouse = pygame.Rect((cords_of_mouse[0], cords_of_mouse[1], 1, 1))
        rect_pos = pygame.Rect(pos + self.size)
        if rect_of_mouse.colliderect(rect_pos):
            if self.type == "add_music":
                if not fl_playlist:
                    x = manager(screen)
                    paths = []
                    for c in songs:
                        paths.append(c.path)
                    if (x[-3:] == "mp3") and x not in paths:
                        try:
                            f = mutagen.File(x, easy=True)
                            audio = MP3(x)
                            now_playlist.songs.append(song(x, str(f['title'])[2:-2], str(f['date'])[2:-2], str(f['album'])[2:-2],
                                              str(f['artist'])[2:-2], 0, audio.info.length))
                            song_file.write(
                                x + "  " + str(f['title'])[2:-2] + "  " + str(f['date'])[2:-2] + "  " + str(f['album'])[
                                                                                                        2:-2] + "  " + str(
                                    f['artist'])[2:-2] + "  " + str(audio.info.length) + "\n")
                            songs_tech.append(
                                x + "  " + str(f['title'])[2:-2] + "  " + str(f['date'])[2:-2] + "  " + str(f['album'])[
                                                                                                        2:-2] + "  " + str(
                                    f['artist'])[2:-2] + "  " + str(audio.info.length) + "\n")
                            playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
                            x = playlist_file.readlines()
                            song_file = open("songs_information.txt", 'r', encoding="windows-1251", errors="ignore")
                            print(Playlists.index(now_playlist))
                            x[Playlists.index(now_playlist)] = x[Playlists.index((now_playlist))][:-1] + f" {len(song_file.readlines()) - 1}" + "\n"
                            print(x)
                            song_file.close()
                            playlist_file.close()
                            playlist_file = open("Playlist_info.txt", "w+", encoding="windows-1251", errors="ignore")
                            for t in x:
                                playlist_file.write(t)
                            playlist_file.close()
                        except KeyError:
                            f = mutagen.File(x, easy=True)
                            audio = MP3(x)
                            now_playlist.songs.append(
                                song(x, str(f['title'])[2:-2], str(f['date'])[2:-2], "Un know", str(f['artist'])[2:-2], 0,
                                     audio.info.length))
                            song_file.write(
                                x + "  " + str(f['title'])[2:-2] + "  " + str(f['date'])[
                                                                          2:-2] + "  " + "Un know" + "  " + str(
                                    f['artist'])[2:-2] + "  " + str(audio.info.length) + "\n")
                            songs_tech.append(x + "  " + str(f['title'])[2:-2] + "  " + str(f['date'])[
                                                                                        2:-2] + "  " + "Un know" + "  " + str(
                                f['artist'])[2:-2] + "  " + str(audio.info.length) + "\n")
                            playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
                            x = playlist_file.readlines()
                            song_file = open("songs_information.txt", 'r', encoding="windows-1251", errors="ignore")
                            x[Playlists.index(now_playlist)] = x[Playlists.index((now_playlist))][
                                                               :-1] + f" {len(song_file.readlines()) - 1}" + "\n"
                            song_file.close()
                            playlist_file.close()
                            playlist_file = open("Playlist_info.txt", "w+", encoding="windows-1251", errors="ignore")
                            for t in x:
                                playlist_file.write(t)
                            playlist_file.close()
                    elif x[-3:] == "wav":
                        f = mutagen.File(x, easy=True)
                        audio = WAVE(x)
                        now_playlist.songs.append(song(x, "Un know", "Un know", "Un know", "Un know", 0, audio.info.length))
                        song_file.write(
                            x + "  " + "Un know" + "  " + "Un know" + "  " + "Un know" + "  " + "Un know" + "  " + str(
                                audio.info.length) + "\n")
                        songs_tech.append(
                            x + "  " + "Un know" + "  " + "Un know" + "  " + "Un know" + "  " + \
                            "Un know" + "  " + str(audio.info.length) + "\n")
                        playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
                        x = playlist_file.readlines()
                        song_file = open("songs_information.txt", 'r', encoding="windows-1251", errors="ignore")
                        x[Playlists.index(now_playlist)] = x[Playlists.index((now_playlist))][
                                                           :-1] + f" {len(song_file.readlines()) - 1}" + "\n"
                        song_file.close()
                        playlist_file.close()
                        playlist_file = open("Playlist_info.txt", "w+", encoding="windows-1251", errors="ignore")
                        for t in x:
                            playlist_file.write(t)
                        playlist_file.close()
                else:
                    x = new_playlist(screen)
                    playlist_file = open("Playlist_info.txt", "a", encoding="windows-1251", errors="ignore")
                    playlist_tech.append(x + "  " + "-1" + "\n")
                    playlist_file.write(playlist_tech[-1])
                    playlist_file.close()
                    Playlists.append(PlayList(x, [], BLUE))
            elif self.type == "del_music":
                fl = not fl
            elif self.type == "Playlist":
                fl_playlist = True
                now_playlist = False
                print(pos_of_music)
                pos_of_music = 0
                songs = [0] * 70
        song_file.close()


button_add_music = buttons(TURQUOISE, "add_music", (width - 100, 0), (100, 100), "+", BLACK)
button_del_music = buttons(TURQUOISE, "del_music", (0, 0), (100, 100), "-", BLACK)
button_playlist_mode = buttons(TURQUOISE, "Playlist", (200, 0), (200, 100), "Playlists", BLACK)


# songs


class song:
    def __init__(self, path, name, date, album, who_play, status, length):
        self.path = path
        self.name = name
        self.date = date
        self.album = album
        self.who_play = who_play
        self.status = status
        self.length_minutes = int(float(length)) // 60
        self.length_seconds = int(float(length)) % 60
        self.length = int(float(length))

    def draw(self, pos, size, color):
        pygame.draw.rect(screen, color, (pos[0], pos[1], size[0], size[1]))
        font_style = pygame.font.Font("HighVoltage Rough.ttf", 50)
        render_song = font_style.render(f"{self.name}", False, BLACK)
        render_artist = font_style.render(f"{self.who_play}", False, BLACK)
        screen.blit(render_song, pos)
        screen.blit(render_artist, (width - len(self.who_play) * 24, pos[1]))

    def get_and_play(self, pos, size):
        global s, player
        pos_mouse = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect((pos_mouse[0], pos_mouse[1], 1, 1))
        pos_rect = pygame.Rect((pos[0], pos[1], size[0], size[1]))
        if mouse_rect.colliderect(pos_rect) and pos_mouse[1] < height - 100:
            pygame.mixer.music.load(self.path)
            pygame.mixer.music.play(1)
            for t in songs:
                t.status = 0
            self.status = 1
            return True
        else:
            return False

    def get_and_delete(self, pos, size, n):
        global fl, now_song, songs
        pos_mouse = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect((pos_mouse[0], pos_mouse[1], 1, 1))
        pos_rect = pygame.Rect((pos[0], pos[1], size[0], size[1]))
        if mouse_rect.colliderect(pos_rect) and pos_mouse[1] < height - 100:
            if now_song == songs[n]:
                now_song = False
                pygame.mixer.music.stop()
            now_playlist.songs.pop(n)
            songs = now_playlist.songs
            if len(now_playlist.songs_tech) > 0:
                now_playlist.songs_tech.pop(n)
            playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
            c = playlist_file.readlines()
            playlist_file.close()
            playlist_file = open("Playlist_info.txt", "w", encoding="windows-1251", errors="ignore")
            for t in c:
                v = t.split("  ")[0] + '  '
                for g in t.split("  ")[1].split():
                    if int(g) != n:
                        v += str(int(g) - 1) + " "
                playlist_file.write(v[:-1] + "\n")
            fl = False
            return True
        else:
            return False


for t in songs_tech:
    y = t.split(sep="  ")
    y[-1] = y[-1][:-1]
    songs.append(song(y[0], y[1], y[2], y[3], y[4], 0, y[5]))


# playlists
class PlayList:
    def __init__(self, name, songss, color):
        self.name = name
        self.songs = []
        self.songs_tech = []
        songs_file = open("songs_information.txt", "r")
        x = songs_file.readlines()
        songs_file.close()
        print(songss)
        for r in range(len(songss)):
            if int(songss[r]) >= 0:
                self.songs_tech.append(x[int(songss[r])])
        for y in songss:
            if int(y) >= 0:
                self.songs.append(songs[int(y)])
        print(self.songs)
        self.color = color

    def draw_playlist(self, pos, size):
        pygame.draw.rect(screen, self.color, (pos[0], pos[1], size[0], size[1]))
        font_style = pygame.font.Font("HighVoltage Rough.ttf", 40)
        if len(self.name) < 12:
            screen.blit(font_style.render(self.name, False, BLACK), (pos[0], pos[1] + 20))
        else:
            for t in range(len(self.name) // 8 + 1):
                screen.blit(font_style.render(self.name[t * 8: (t + 1) * 8], False, BLACK), (pos[0], pos[1] + t * 40))

    def get_click(self, pos, size):
        global songs, fl_playlist, now_playlist, songs_tech, pos_of_music
        x_rect = pygame.Rect(pygame.mouse.get_pos() + (1, 1))
        pos_rect = pygame.Rect(pos + size)
        if x_rect.colliderect(pos_rect):
            fl_playlist = False
            now_playlist = Playlists[Playlists.index(self)]
            songs = self.songs
            pos_of_music = 0

    def get_click_and_delete(self, pos, size):
        x_rect = pygame.Rect(pygame.mouse.get_pos() + (1, 1))
        pos_rect = pygame.Rect(pos + size)
        if x_rect.colliderect(pos_rect):
            playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
            real_parameters = playlist_file.readlines()
            playlist_file.close()
            real_parameters.pop(Playlists.index(self))
            playlist_file = open("Playlist_info.txt", "w", encoding="windows-1251", errors="ignore")
            for t in real_parameters:
                playlist_file.write(t)
            playlist_file.close()
            print(Playlists)
            Playlists.pop(Playlists.index(self))
            return True
        else:
            return False


for t in playlist_tech:
    t_2 = t.split("  ")
    Playlists.append(PlayList(t_2[0], t_2[1].split(), BLUE))


# pygame part
screen = pygame.display.set_mode((width, height))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if not fl:
                x = pygame.mouse.get_pos()
                x_rect = pygame.Rect((x[0], x[1], 1, 1))
                play_circle_rect = pygame.Rect((80, height - 70, 56, 60))
                next_track_rect = pygame.Rect(150, height - 70, 50, 55)
                last_track_rect = pygame.Rect(0, height - 70, 50, 55)
                random_rect = pygame.Rect(width - 165, height - 50, 50, 50)
                all_rect = pygame.Rect(width - 100, height - 50, 100, 50)
                one_rect = pygame.Rect(width - 300, height - 50, 100, 50)
                volume_rect = pygame.Rect(500, height - 20, 200, 10)
                if x_rect.colliderect(play_circle_rect):
                    Play_fl = not Play_fl
                if x_rect.colliderect(volume_rect):
                    print((x[0] - 500) / 20 / 10)
                    if x[0] == 500:
                        pygame.mixer.music.set_volume(0)
                        pos = 500
                    else:
                        pygame.mixer.music.set_volume((x[0] - 500) / 20 / 10)
                        pos = 20 * int((x[0] - 500) / 20 + 1) + 500
                if x_rect.colliderect(random_rect):
                    type_play = "Random"
                if x_rect.colliderect(all_rect):
                    type_play = "All_of_playlist"
                if x_rect.colliderect(one_rect):
                    type_play = "One_repeat"
                if x_rect.colliderect(next_track_rect) and now_song in songs:
                    now_song.status = 0
                    if songs.index(now_song) + 1 < len(songs):
                        now_song = songs[songs.index(now_song) + 1]
                    else:
                        now_song = songs[0]
                    now_time_minutes = 0
                    now_time_seconds = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(now_song.path)
                    pygame.mixer.music.play(1)
                    now_song.status = 1
                if x_rect.colliderect(last_track_rect):
                    if now_time_seconds > 1 or now_time_minutes > 0:
                        pygame.mixer.music.play(1)
                        now_time_minutes = 0
                        now_time_seconds = 0
                    else:
                        now_song.status = 0
                        now_song = songs[songs.index(now_song) - 1]
                        now_time_minutes = 0
                        now_time_seconds = 0
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(now_song.path)
                        pygame.mixer.music.play(1)
                        now_song.status = 1
                if not fl_playlist:
                    for song_obj in range(len(songs)):
                        if pos_of_music < 0:
                            x_2 = songs[song_obj].get_and_play((0, 70 * (song_obj + 1) + 70 + pos_of_music), (1100, 70))
                        else:
                            x_2 = songs[song_obj].get_and_play((0, 70 * (song_obj + 1) + 70), (1100, 70))
                        if x_2:
                            now_song = songs[song_obj]
                            now_time_seconds = 0.0
                            now_time_minutes = 0
                            break
                else:
                    for playlist in range(len(Playlists)):
                        if pos_of_music > 0:
                            print("ok", pos_of_music)
                            Playlists[playlist].get_click((190 * (playlist % 5), 200 * (playlist // 5) + 200 + pos_of_music), (180, 200))
                        else:
                            Playlists[playlist].get_click((190 * (playlist % 5), 200 * (playlist // 5) + 200),
                                                          (180, 200))

                if now_song:
                    rect_of_line = pygame.Rect((210, height - 90 - 10, 840, 15))
                    if x_rect.colliderect(rect_of_line):
                        sec_of_click = (x[0] - 210) / (840 / now_song.length)
                        begin_position = sec_of_click - (now_time_minutes * 60 + int(now_time_seconds))
                        pygame.mixer.music.set_pos(sec_of_click)
                        now_time_seconds += begin_position % 60
                        now_time_minutes += begin_position // 60
                if pos_of_music > 0:
                    button_add_music.get_click((button_add_music.cords[0], button_add_music.cords[1]))
                    button_del_music.get_click((button_del_music.cords[0], button_del_music.cords[1]))
                    button_playlist_mode.get_click(button_playlist_mode.cords)
                else:
                    button_add_music.get_click((button_add_music.cords[0], button_add_music.cords[1] + pos_of_music))
                    button_del_music.get_click((button_del_music.cords[0], button_del_music.cords[1] + pos_of_music))
                    button_playlist_mode.get_click((button_playlist_mode.cords[0], button_playlist_mode.cords[1] + pos_of_music))
            else:
                if not fl_playlist:
                    for song_obj in range(len(songs)):
                        if len(songs) >= 7:
                            x_2 = songs[song_obj].get_and_delete((0, 70 * (song_obj + 1) + 70 + pos_of_music), (1100, 70),
                                                                 song_obj)
                        else:
                            x_2 = songs[song_obj].get_and_delete((0, 70 * (song_obj + 1) + 70), (1100, 70), song_obj)
                        if x_2:
                            break
                else:
                    for t in range(len(Playlists)):
                        if len(Playlists) > 5:
                            x = Playlists[t].get_click_and_delete(
                                (190 * (t % 5), 200 * (t // 5) + 200 + pos_of_music), (180, 200))
                        else:
                            x = Playlists[t].get_click_and_delete((190 * (t % 5), 200 * (t // 5) + 200),
                                                          (180, 200))
                        if x:
                            break
                if pos_of_music >= 0:
                    button_del_music.get_click((button_del_music.cords[0], button_del_music.cords[1]))
                else:
                    button_del_music.get_click((button_del_music.cords[0], button_del_music.cords[1] + pos_of_music))
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 4:
            pos_of_music += 10
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 5:
            pos_of_music -= 10

    # motion control
    if pos_of_music > 0:
        pos_of_music = 0
    if pos_of_music < -(len(songs) - 7) * 70 - 10 and not fl_playlist:
        pos_of_music = -(len(songs) - 7) * 70 - 10

    # delete type
    if fl:
        screen.fill(RED)
    else:
        screen.fill(BEIGE)
        if pos_of_music > 0 or (fl_playlist and len(Playlists) <= 5):
            pygame.draw.rect(screen, BROWN, (0, 0, width, 100))
            pygame.draw.rect(screen, BROWN, (0, height - 300, width, 50))
        else:
            pygame.draw.rect(screen, BROWN, (0, 0 + pos_of_music, width, 100))
            pygame.draw.rect(screen, BROWN, (0, height - 300 + pos_of_music, width, 50))

    # buttons
    if pos_of_music > 0 or (fl_playlist and len(Playlists) <= 5):
        button_add_music.draw((button_add_music.cords[0], button_add_music.cords[1]))
        button_del_music.draw((button_del_music.cords[0], button_del_music.cords[1]))
        button_playlist_mode.draw(button_playlist_mode.cords)
    else:
        button_add_music.draw((button_add_music.cords[0], button_add_music.cords[1] + pos_of_music))
        button_del_music.draw((button_del_music.cords[0], button_del_music.cords[1] + pos_of_music))
        button_playlist_mode.draw((button_playlist_mode.cords[0], button_playlist_mode.cords[1] + pos_of_music))

    # decor
    font_style = pygame.font.Font("HighVoltage Rough.ttf", 30)
    render_of_music = font_style.render("Songs:", False, BLACK)
    if pos_of_music > 0 or (fl_playlist and len(Playlists) <= 5):
        screen.blit(render_of_music, (500, 100))
    else:
        screen.blit(render_of_music, (500, 100 + pos_of_music))

    # playlist draw
    if fl_playlist:
        for t in range(len(Playlists)):
            if len(Playlists) > 5:
                Playlists[t].draw_playlist((190 * (t % 5), 300 * (t // 5) + 200 + pos_of_music), (180, 200))
            else:
                Playlists[t].draw_playlist((190 * (t % 5), 300 * (t // 5) + 200), (180, 200))

    # songs drawing
    if Play_fl:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
        now_time_minutes = (now_time_minutes * 60) // 60 + now_time_seconds // 60
        now_time_seconds = (now_time_seconds) % 60 + 0.1
        if now_song and (
                now_time_seconds + now_time_minutes * 60 >= now_song.length_minutes * 60 + now_song.length_seconds):
            now_song.status = 0
            if type_play == "One":
                now_song = False
            elif type_play == "All_of_playlist":
                if songs.index(now_song) + 1 < len(songs):
                    now_song = songs[songs.index(now_song) + 1]
                else:
                    now_song = False
            elif type_play == "Random":
                now_song = random.choice(songs)
            elif type_play == "One_repeat":
                now_song.status = 1
            if now_song and type_play != "one_repeat":
                now_song.status = 1
                pygame.mixer.music.load(now_song.path)
                pygame.mixer.music.play(1)
            now_time_minutes = 0
            now_time_seconds = 0
    if not fl_playlist:
        for song_obj in range(len(songs)):
            if songs[song_obj].status == 0:
                if len(songs) > 7:
                    songs[song_obj].draw((0, 70 * (song_obj + 1) + pos_of_music + 70), (1100, 70), TURQUOISE)
                else:
                    songs[song_obj].draw((0, 70 * (song_obj + 1) + 70), (1100, 70), TURQUOISE)
            else:
                if len(songs) > 7:
                    songs[song_obj].draw((0, 70 * (song_obj + 1) + pos_of_music + 70), (1100, 70), BLUE)
                else:
                    songs[song_obj].draw((0, 70 * (song_obj + 1) + 70), (1100, 70), BLUE)

    # song play tablet
    pygame.draw.rect(screen, TURQUOISE, (0, height - 100, width, 100))
    if Play_fl:
        pygame.draw.polygon(screen, YELLOW, ((125, height - 45), (75, height - 70), (75, height - 15)))
    else:
        pygame.draw.rect(screen, YELLOW, (75, height - 70, 22, 55))
        pygame.draw.rect(screen, YELLOW, (105, height - 70, 22, 55))
    pygame.draw.polygon(screen, BLUE, ((200, height - 45), (150, height - 70), (150, height - 15)))
    pygame.draw.polygon(screen, BLUE, ((0, height - 45), (50, height - 70), (50, height - 15)))
    if now_song:
        render_all_time = font_style.render(f"{now_song.length_minutes}.{now_song.length_seconds}", False, BLACK)
        screen.blit(render_all_time,
                    (width - len(f"{now_song.length_minutes}.{now_song.length_seconds}") * 15, height - 90))
        now_time_render = font_style.render(str(int(now_time_minutes)) + '.' + str(int(now_time_seconds)), False, BLACK)
        screen.blit(now_time_render, (150, height - 90))
        pygame.draw.line(screen, RED, (210, height - 90), (1050, height - 90), 5)
        pos_circle = int((840 / now_song.length) * (now_time_minutes * 60 + now_time_seconds) + 210)
        pygame.draw.circle(screen, BLUE, (pos_circle, height - 90), 5)
        pygame.draw.line(screen, BLUE, (210, height - 90), (pos_circle, height - 90), 5)

    # mode buttons
    image_random_play = pygame.image.load("images/random.png")
    screen.blit(image_random_play, (width - 165, height - 50))
    image_all_play = pygame.image.load("images/all.png")
    screen.blit(image_all_play, (width - 100, height - 50))
    image_one_repeat = pygame.image.load("images/one.png")
    screen.blit(image_one_repeat, (width - 300, height - 50))
    if type_play == "Random":
        pygame.draw.lines(screen, YELLOW, True, ((width - 190, height - 50), (width - 95, height - 50), (width - 95, height), (width - 190, height)), 5)
    elif type_play == "One_repeat":
        pygame.draw.lines(screen, YELLOW, True, ((width - 300, height - 50), (width - 190, height - 50), (width - 190, height), (width - 300, height)), 5)
    elif type_play == "All_of_playlist":
        pygame.draw.lines(screen, YELLOW, True, ((width - 100, height - 50), (width, height - 50), (width, height), (width - 100, height)), 5)

    # volume
    pygame.draw.line(screen, GRAY, (500, height - 20), (700, height - 20), 10)
    pygame.draw.line(screen, YELLOW, (500, height - 20), (pos, height - 20), 10)
    pygame.draw.circle(screen, YELLOW, (pos, height - 20), 10)

    # names
    if now_song:
        font_style = pygame.font.Font("HighVoltage Rough.ttf", 40)
        screen.blit(font_style.render(now_song.name, False, BLACK), (220, height - 80))
        screen.blit(font_style.render(now_song.who_play, False, GRAY), (220, height - 50))

    pygame.display.flip()
    time.sleep(0.085)
