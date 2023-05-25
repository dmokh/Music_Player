import pygame
import os
import random
import time
import win32api
import mutagen
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init(frequency=44200)

WIDTH = 1100
HEIGHT = 700

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
LIGHT_BLUE = (135, 206, 250)
LIGHT_GRAY = (181, 184, 177)
LIGHT_RED = (255, 71, 76)

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


def manager(surface):
    global now_time_minutes, now_time_seconds
    width = 1000
    height = 400
    sc = pygame.Surface((width, height))
    now_path = "C:/"
    wholes = [(i, os.path.isdir(now_path + "/" + i)) for i in os.listdir(now_path)]
    disks = list(win32api.GetLogicalDriveStrings())
    count = len(wholes)
    File_which_is_choice_user = False
    rect_from_dir = pygame.Rect(0, height - 80, 100, 100)
    n = 0
    while True:
        # draw GUI
        sc.fill(WHITE)
        pygame.draw.rect(sc, LIGHT_GRAY, (200, 0, 50, height))
        sc.blit(pygame.image.load("images/Fromdirectory.xcf"), (0, height - 80))
        for i in range(count):
            pygame.draw.rect(sc, BEIGE, (250, i * 30 + n * 30, width - 250, 20))
            sc.blit(pygame.font.SysFont("Calibri", 17).render(wholes[i][0], False, BLACK), (250, i * 30 + n * 30))
        for i in range(len(disks) // 4):
            pygame.draw.rect(sc, BEIGE, (0, i * 30, 200, 30))
            sc.blit(pygame.font.SysFont("Calibri", 30).render(disks[i * 4], False, BLACK), (0, i * 30))

        # check all events from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cords = pygame.mouse.get_pos()
                if event.button == 1:
                    if rect_from_dir.colliderect(cords[0], cords[1], 1, 1) and len(now_path) > 4:
                        n = 0
                        a = -1
                        while a > (-len(now_path)) and now_path[a] != "/":
                            a -= 1
                        now_path = now_path[:a]
                        wholes = [(i, os.path.isdir(now_path + "/" + i)) for i in os.listdir(now_path)]
                        count = len(wholes)
                    if cords[0] > 250 and cords[1] // 30 - n < count:
                        if wholes[cords[1] // 30 - n][1]:
                            now_path = os.path.join(now_path + "/" + wholes[cords[1] // 30 - n][0])
                            n = 0
                            try:
                                wholes = [(i, os.path.isdir(now_path + "/" + i)) for i in os.listdir(now_path)]
                            except PermissionError:
                                print(PermissionError)
                            except FileNotFoundError:
                                print(FileNotFoundError)
                            count = len(wholes)
                        elif os.path.join(now_path + "/" + wholes[cords[1] // 30 - n][0]) != File_which_is_choice_user:
                            File_which_is_choice_user = os.path.join(now_path + "/" + wholes[cords[1] // 30 - n][0])
                        else:
                            return File_which_is_choice_user
                    elif cords[0] < 200 and cords[1] // 30 < len(disks) // 4:
                        now_path = str(disks[(cords[1] // 30) * 4]) + ":/"
                        wholes = [(i, os.path.isdir(now_path + "/" + i)) for i in os.listdir(now_path)]
                        count = len(wholes)
                elif event.button == 4:
                    if n < 0:
                        n += 1
                elif event.button == 5:
                    if len(wholes) > height // 30:
                        if n - 1 >= (-(len(wholes) - height // 30)):
                            n -= 1
        surface.blit(sc, (0, 0))
        now_time_minutes = (now_time_minutes * 60) // 60 + now_time_seconds // 60
        now_time_seconds = now_time_seconds % 60 + 0.1
        time.sleep(0.03)
        pygame.display.flip()


# songs file
with open('songs_information.txt', "r+", encoding='windows-1251', errors="ignore") as song_file:
    songs_tech = song_file.readlines()
with open('Playlist_info.txt', "r+", encoding='windows-1251', errors="ignore") as playlist_info:
    playlist_tech = playlist_info.readlines()
Playlists = []
songs = []


def new_playlist(surface):
    surf = pygame.Surface((500, 250))
    font_new_playlist = pygame.font.Font("HighVoltage Rough.ttf", 40)
    create_rect = pygame.Rect(210, 200, 100, 50)
    text = ""
    index_of_cursor = 0
    while True:
        surf.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                rect = pygame.Rect(
                    (pygame.mouse.get_pos()[0] - WIDTH // 2 + 250, pygame.mouse.get_pos()[1] - HEIGHT // 2 + 125, 1, 1))
                if rect.colliderect(create_rect):
                    return text
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(text) > 0 and index_of_cursor > 0:
                        text = text[:index_of_cursor - 1] + text[index_of_cursor:]
                        index_of_cursor -= 1
                elif event.key == pygame.K_LEFT:
                    if index_of_cursor > 0:
                        index_of_cursor -= 1
                elif event.key == pygame.K_RIGHT:
                    if index_of_cursor < len(text):
                        index_of_cursor += 1
                else:
                    if len(text) < 14:
                        text += event.unicode
                        index_of_cursor += 1
        surf.blit(font_new_playlist.render("Name of new playlist:", False, BLACK), (100, 0))
        pygame.draw.rect(surf, YELLOW, (210, 200, 100, 50))
        pygame.draw.lines(surf, YELLOW, True, ((50, 100), (450, 100), (450, 150), (50, 150)))
        surf.blit(font_new_playlist.render(text[:index_of_cursor] + '|' + text[index_of_cursor:], False, BLACK),
                  (50, 100))
        surf.blit(font_new_playlist.render("Create", False, BLACK), (210, 200))
        surface.blit(surf, (WIDTH // 2 - 250, HEIGHT // 2 - 125))
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

    def draw(self, position):
        pygame.draw.rect(screen, self.color, position + self.size)
        font_render = self.font_style.render(self.text, False, self.text_color)
        screen.blit(font_render, (position[0] + 42 if self.type != "Playlist" else position[0] + 20, position[1] + 30))

    def get_click(self, position):
        global fl, song_file, fl_playlist, pos_of_music, now_playlist, songs
        cords_of_mouse = pygame.mouse.get_pos()
        rect_of_mouse = pygame.Rect((cords_of_mouse[0], cords_of_mouse[1], 1, 1))
        rect_pos = pygame.Rect(position + self.size)
        if rect_of_mouse.colliderect(rect_pos):
            if self.type == "add_music":
                if not fl_playlist:
                    new_file = manager(screen)
                    if not new_file:
                        return False
                    paths = []
                    for c in songs:
                        paths.append(c.path)
                    f = mutagen.File(new_file, easy=True)
                    if new_file[-3:] == "mp3" and new_file not in paths:
                        audio = MP3(new_file)
                        try:
                            title = str(f['title'])[2:-2]
                        except KeyError:
                            title = "Unknown"
                        try:
                            date = str(f['date'])[2:-2]
                        except KeyError:
                            date = "Unknown"
                        try:
                            album = str(f['album'])[2:-2]
                        except KeyError:
                            album = "Unknown"
                        try:
                            artist = str(f['artist'])[2:-2]
                        except KeyError:
                            artist = "Unknown"
                        now_playlist.songs.append(
                            song(new_file, title, date, album,
                                 artist, 0, audio.info.length))
                        with open("songs_information.txt", 'a', encoding="windows-1251",
                                  errors="ignore") as song_file:
                            song_file.write(new_file + "  " + title + "  " + date + "  " + album + "  " +
                                            artist + "  " + str(audio.info.length) + "\n")
                        songs_tech.append(new_file + "  " + title + "  " + date + "  " + album + "  " +
                                          artist + "  " + str(audio.info.length) + "\n")
                        now_playlist.songs_tech.append(new_file + "  " + title + "  " + date + "  " + album + "  " +
                                                       artist + "  " + str(audio.info.length) + "\n")
                    elif new_file[-3:] == "wav" and new_file not in paths:
                        audio = WAVE(new_file)
                        now_playlist.songs.append(
                            song(new_file, "Unknown", "Unknown", "Unknown", "Unknown", 0, audio.info.length))
                        with open("songs_information.txt", 'a', encoding="windows-1251",
                                  errors="ignore") as song_file:
                            song_file.write(
                                new_file + "  " + "Unknown  " + "Unknown  " + "Unknown  " + "Unknown  " + str(
                                    audio.info.length) + "\n")
                        songs_tech.append(
                            new_file + "  " + "Unknown  " + "Unknown  " + "Unknown  " + "Unknown  " + str(
                                audio.info.length) + "\n")
                        now_playlist.songs_tech.append(
                            new_file + "  " + "Unknown  " + "Unknown  " + "Unknown  " + "Unknown  " + str(
                                audio.info.length) + "\n")
                    file_of_playlist = open("Playlist_info.txt", "r", encoding="windows-1251",
                                            errors="ignore")
                    playlist_file = file_of_playlist.readlines()
                    song_file = open("songs_information.txt", 'r', encoding="windows-1251", errors="ignore")
                    playlist_file[Playlists.index(now_playlist)] = \
                        playlist_file[Playlists.index((now_playlist))][:-1] \
                        + f" {len(song_file.readlines()) - 1}" + "\n"
                    song_file.close()
                    file_of_playlist.close()
                    file_of_playlist = open("Playlist_info.txt", "w+", encoding="windows-1251", errors="ignore")
                    for t in playlist_file:
                        file_of_playlist.write(t)
                    file_of_playlist.close()
                else:
                    new_file = new_playlist(screen)
                    if new_file:
                        file_of_playlist = open("Playlist_info.txt", "a", encoding="windows-1251", errors="ignore")
                        playlist_tech.append(new_file + "  " + "-1" + "\n")
                        file_of_playlist.write(playlist_tech[-1])
                        file_of_playlist.close()
                        Playlists.append(PlayList(new_file, [], BLUE))
            elif self.type == "del_music":
                fl = not fl
            elif self.type == "Playlist":
                fl_playlist = True
                now_playlist = False
                pos_of_music = 0
                songs = [0] * 70


button_add_music = buttons(TURQUOISE, "add_music", (WIDTH - 100, 0), (100, 100), "+", BLACK)
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

    def draw(self, position, size, color):
        pygame.draw.rect(screen, color, (position[0], position[1], size[0], size[1]))
        font = pygame.font.Font("HighVoltage Rough.ttf", 50)
        render_song = font.render(f"{self.name}", False, BLACK)
        render_artist = font.render(f"{self.who_play}", False, BLACK)
        screen.blit(render_song, position)
        screen.blit(render_artist, (WIDTH - len(self.who_play) * 24, position[1]))

    def get_and_play(self, pos, size):
        global s, player
        pos_mouse = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect((pos_mouse[0], pos_mouse[1], 1, 1))
        pos_rect = pygame.Rect((pos[0], pos[1], size[0], size[1]))
        if mouse_rect.colliderect(pos_rect) and pos_mouse[1] < HEIGHT - 100:
            pygame.mixer.music.load(self.path)
            pygame.mixer.music.play(1)
            for t in songs:
                t.status = 0
            self.status = 1
            return True
        else:
            return False

    def get_and_delete(self, position, size, n):
        global fl, now_song, songs
        pos_mouse = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect((pos_mouse[0], pos_mouse[1], 1, 1))
        pos_rect = pygame.Rect((position[0], position[1], size[0], size[1]))
        if mouse_rect.colliderect(pos_rect) and pos_mouse[1] < HEIGHT - 100:
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
                        if int(g) < n:
                            v += str(int(g)) + " "
                        else:
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
    def __init__(self, name, song_playlist, color):
        self.name = name
        self.songs = []
        self.songs_tech = []
        songs_file = open("songs_information.txt", "r")
        x = songs_file.readlines()
        songs_file.close()
        d = -1
        for r in range(len(song_playlist)):
            if int(song_playlist[r]) >= 0:
                self.songs_tech.append(x[int(song_playlist[r]) - d])
            else:
                d += 1
        d = -1
        for y in song_playlist:
            if int(y) >= 0:
                self.songs.append(songs[int(y) - d])
            else:
                d += 1
        self.color = color

    def draw_playlist(self, position, size):
        pygame.draw.rect(screen, self.color, (position[0], position[1], size[0], size[1]))
        font = pygame.font.Font("HighVoltage Rough.ttf", 40)
        if len(self.name) < 12:
            screen.blit(font.render(self.name, False, BLACK), (position[0] + 20, position[1] + size[1] / 2 - 40))
        else:
            for t in range(len(self.name) // 8 + 1):
                screen.blit(font.render(self.name[t * 8: (t + 1) * 8], False, BLACK),
                            (position[0], position[1] + t * 40))

    def get_click(self, position, size):
        global songs, fl_playlist, now_playlist, songs_tech, pos_of_music
        mous_rect = pygame.Rect(pygame.mouse.get_pos() + (1, 1))
        pos_rect = pygame.Rect(position + size)
        if mous_rect.colliderect(pos_rect):
            fl_playlist = False
            now_playlist = Playlists[Playlists.index(self)]
            songs = self.songs
            pos_of_music = 0

    def get_click_and_delete(self, pos, size):
        m_rect = pygame.Rect(pygame.mouse.get_pos() + (1, 1))
        pos_rect = pygame.Rect(pos + size)
        if m_rect.colliderect(pos_rect):
            playlist_file = open("Playlist_info.txt", "r", encoding="windows-1251", errors="ignore")
            real_parameters = playlist_file.readlines()
            playlist_file.close()
            real_parameters.pop(Playlists.index(self))
            playlist_file = open("Playlist_info.txt", "w", encoding="windows-1251", errors="ignore")
            for t in real_parameters:
                playlist_file.write(t)
            playlist_file.close()
            Playlists.pop(Playlists.index(self))
            return True
        else:
            return False


for t in playlist_tech:
    t_2 = t.split("  ")
    Playlists.append(PlayList(t_2[0], t_2[1].split(), BLUE))

# pygame part
screen = pygame.display.set_mode((WIDTH, HEIGHT))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if not fl:
                x = pygame.mouse.get_pos()
                m_rect = pygame.Rect((x[0], x[1], 1, 1))
                play_circle_rect = pygame.Rect((80, HEIGHT - 70, 56, 60))
                next_track_rect = pygame.Rect(150, HEIGHT - 70, 50, 55)
                last_track_rect = pygame.Rect(0, HEIGHT - 70, 50, 55)
                random_rect = pygame.Rect(WIDTH - 165, HEIGHT - 50, 50, 50)
                all_rect = pygame.Rect(WIDTH - 100, HEIGHT - 50, 100, 50)
                one_rect = pygame.Rect(WIDTH - 300, HEIGHT - 50, 100, 50)
                volume_rect = pygame.Rect(500, HEIGHT - 20, 200, 10)
                if m_rect.colliderect(play_circle_rect):
                    Play_fl = not Play_fl
                if m_rect.colliderect(volume_rect):
                    if x[0] == 500:
                        pygame.mixer.music.set_volume(0)
                        pos = 500
                    else:
                        pygame.mixer.music.set_volume((x[0] - 500) / 20 / 10)
                        pos = 20 * int((x[0] - 500) / 20 + 1) + 500
                if m_rect.colliderect(random_rect):
                    type_play = "Random"
                if m_rect.colliderect(all_rect):
                    type_play = "All_of_playlist"
                if m_rect.colliderect(one_rect):
                    type_play = "One_repeat"
                if m_rect.colliderect(next_track_rect) and now_song in songs:
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
                    else:
                        now_song = songs[0]
                    now_time_minutes = 0
                    now_time_seconds = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(now_song.path)
                    pygame.mixer.music.play(1)
                    now_song.status = 1
                if m_rect.colliderect(last_track_rect):
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
                            Playlists[playlist].get_click(
                                (190 * (playlist % 5), 200 * (playlist // 5) + 200 + pos_of_music), (180, 200))
                        else:
                            Playlists[playlist].get_click((190 * (playlist % 5), 200 * (playlist // 5) + 200),
                                                          (180, 200))

                if now_song:
                    rect_of_line = pygame.Rect((210, HEIGHT - 90 - 10, 840, 15))
                    if m_rect.colliderect(rect_of_line):
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
                    button_playlist_mode.get_click(
                        (button_playlist_mode.cords[0], button_playlist_mode.cords[1] + pos_of_music))
            else:
                if not fl_playlist:
                    for song_obj in range(len(songs)):
                        if len(songs) >= 7:
                            x_2 = songs[song_obj].get_and_delete((0, 70 * (song_obj + 1) + 70 + pos_of_music),
                                                                 (1100, 70),
                                                                 song_obj)
                        else:
                            x_2 = songs[song_obj].get_and_delete((0, 70 * (song_obj + 1) + 70), (1100, 70), song_obj)
                        if x_2:
                            o = open("songs_information.txt", "r")
                            o_t = o.readlines()
                            o.close()
                            o = open("songs_information.txt", "w")
                            o_t.pop(song_obj)
                            for t in o_t:
                                o.write(t)
                            o.close()
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
        screen.fill(LIGHT_RED)
    else:
        screen.fill(LIGHT_BLUE)
        if pos_of_music > 0 or (fl_playlist and len(Playlists) <= 5):
            pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WIDTH, 100))
            pygame.draw.rect(screen, LIGHT_GRAY, (0, HEIGHT - 300, WIDTH, 50))
        else:
            pygame.draw.rect(screen, LIGHT_GRAY, (0, 0 + pos_of_music, WIDTH, 100))
            pygame.draw.rect(screen, LIGHT_GRAY, (0, HEIGHT - 300 + pos_of_music, WIDTH, 50))

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
        now_time_seconds = now_time_seconds % 60 + 0.1
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
    pygame.draw.rect(screen, TURQUOISE, (0, HEIGHT - 100, WIDTH, 100))
    if Play_fl:
        pygame.draw.polygon(screen, YELLOW, ((125, HEIGHT - 45), (75, HEIGHT - 70), (75, HEIGHT - 15)))
    else:
        pygame.draw.rect(screen, YELLOW, (75, HEIGHT - 70, 22, 55))
        pygame.draw.rect(screen, YELLOW, (105, HEIGHT - 70, 22, 55))
    pygame.draw.polygon(screen, BLUE, ((200, HEIGHT - 45), (150, HEIGHT - 70), (150, HEIGHT - 15)))
    pygame.draw.polygon(screen, BLUE, ((0, HEIGHT - 45), (50, HEIGHT - 70), (50, HEIGHT - 15)))
    if now_song:
        render_all_time = font_style.render(f"{now_song.length_minutes}.{now_song.length_seconds}", False, BLACK)
        screen.blit(render_all_time,
                    (WIDTH - len(f"{now_song.length_minutes}.{now_song.length_seconds}") * 15, HEIGHT - 90))
        now_time_render = font_style.render(str(int(now_time_minutes)) + '.' + str(int(now_time_seconds)), False, BLACK)
        screen.blit(now_time_render, (150, HEIGHT - 90))
        pygame.draw.line(screen, RED, (210, HEIGHT - 90), (1050, HEIGHT - 90), 5)
        pos_circle = int((840 / now_song.length) * (now_time_minutes * 60 + now_time_seconds) + 210)
        pygame.draw.circle(screen, BLUE, (pos_circle, HEIGHT - 90), 5)
        pygame.draw.line(screen, BLUE, (210, HEIGHT - 90), (pos_circle, HEIGHT - 90), 5)

    # mode buttons
    image_random_play = pygame.image.load("images/random.png")
    screen.blit(image_random_play, (WIDTH - 165, HEIGHT - 50))
    image_all_play = pygame.image.load("images/all.png")
    screen.blit(image_all_play, (WIDTH - 100, HEIGHT - 50))
    image_one_repeat = pygame.image.load("images/one.png")
    screen.blit(image_one_repeat, (WIDTH - 300, HEIGHT - 50))
    if type_play == "Random":
        pygame.draw.lines(screen, YELLOW, True, (
            (WIDTH - 190, HEIGHT - 50), (WIDTH - 95, HEIGHT - 50), (WIDTH - 95, HEIGHT), (WIDTH - 190, HEIGHT)), 5)
    elif type_play == "One_repeat":
        pygame.draw.lines(screen, YELLOW, True, (
            (WIDTH - 300, HEIGHT - 50), (WIDTH - 190, HEIGHT - 50), (WIDTH - 190, HEIGHT), (WIDTH - 300, HEIGHT)), 5)
    elif type_play == "All_of_playlist":
        pygame.draw.lines(screen, YELLOW, True,
                          ((WIDTH - 100, HEIGHT - 50), (WIDTH, HEIGHT - 50), (WIDTH, HEIGHT), (WIDTH - 100, HEIGHT)), 5)

    # volume
    pygame.draw.line(screen, GRAY, (500, HEIGHT - 20), (700, HEIGHT - 20), 10)
    pygame.draw.line(screen, YELLOW, (500, HEIGHT - 20), (pos, HEIGHT - 20), 10)
    pygame.draw.circle(screen, YELLOW, (pos, HEIGHT - 20), 10)

    # names
    if now_song:
        font_style = pygame.font.Font("HighVoltage Rough.ttf", 40)
        screen.blit(font_style.render(now_song.name, False, BLACK), (220, HEIGHT - 80))
        screen.blit(font_style.render(now_song.who_play, False, GRAY), (220, HEIGHT - 50))

    pygame.display.flip()
    time.sleep(0.07)
