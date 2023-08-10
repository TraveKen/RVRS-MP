from textual.app import *
from textual.widgets import *
from textual import *
from textual.containers import *
from slider import Slider
from volumeslider import Slider as VolumeSlider
from viewer import ImageViewer
from PIL import Image
import eyed3
from textual.reactive import reactive
import pygame
from multiprocessing import Process
import shutil
from io import BytesIO

import sys

def play_audio(audio, start_time):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(start=start_time)

def convert_seconds_to_mmss(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02}:{remaining_seconds:02}"

def convert_mmss_to_seconds(mmss):
    try:
        if len(mmss.split(':')) == 1:
            return int(mmss)
        elif len(mmss.split(':')) == 2:
            return int(mmss.split(':')[0]) * 60 + int(mmss.split(':')[1])
        else:
            return 'error'
    except (IndexError, ValueError) as e:
        return 'error'
class Player(App):
    CSS_PATH = 'player.css'
    def compose(self) -> ComposeResult:
        yield Header()
        with Center(id='songselect_and_image'):
            with RadioSet():
                with open(os.path.join(config_dir, 'music.txt'), 'r') as f:
                    self.song_list = f.read().split("\n")
                    self.song_list = [os.path.join(i) for i in self.song_list if i != '']
                for song in range(len(self.song_list)):
                    audio = eyed3.load(self.song_list[song])
                    if audio.tag:
                        if audio.tag.title:
                            title_value = audio.tag.title
                        else:
                            title_value = os.path.splitext(os.path.basename(self.song_list[song]))[0]

                    if song == 0:
                        yield RadioButton(title_value, value=True, id=f'song_{song}')
                    else:
                        yield RadioButton(title_value, id=f'song_{song}')

            yield ImageViewer(Image.new(mode="RGB", size=(500, 500)))
        with Center(id='title_container'):
            yield Label("test", id='title')

        yield Slider(0, 1, id='time_slider')
        with Center(id='time'):
            yield Label("00:00", id='current_time')
            yield Label("", id='total_time')
        yield VolumeSlider(0, 10, value=10, id='volume_slider')
        with Center(id='control'):
            yield Button('☰', variant='default', id='songselect')
            yield Button('🔇', variant='default', id='volume')
            yield Input(placeholder='Jump to')
            yield Label(" ", classes='seperator')
            yield Button('<', variant='primary', id='prev')
            yield Button('■', variant='error', id='play')
            yield Button('>', variant='primary', id='next')
            yield Label(" ", classes='seperator')
            yield Label(" ", classes='seperator')
            yield Label(" ", classes='button_placeholder')
            yield Label(" ", classes='button_placeholder')


    @on(Slider.Changed)
    def update_screen(self) -> None:
        time = self.query_one("#time_slider", Slider).value
        current_time = self.query_one("#current_time")
        current_time.update(convert_seconds_to_mmss(time))

    @on(Slider.MouseCapture)
    def pause(self) -> None:
        if self.status == 'playing':
            pygame.mixer.music.stop()
            self.status = 'tem_paused'
        else:
            pass

    @on(Slider.MouseRelease)
    def resume(self) -> None:
        time = self.query_one("#time_slider", Slider).value
        if self.status == 'tem_paused':
            play_audio(self.song_list[self.song_count], time)
            self.status = 'playing'

    @on(Input.Submitted)
    def jump(self, event: Input.Submitted) -> None:
        input_widget = self.query_one(Input)
        time_slider = self.query_one("#time_slider", Slider)
        time_to_jump = convert_mmss_to_seconds(input_widget.value)
        if time_to_jump != 'error':
            if self.status == 'playing':
                pygame.mixer.music.stop()
                input_widget.value = ''
                play_audio(self.song_list[self.song_count], time_to_jump)
                time_slider.value = time_to_jump
            else:
                input_widget.value = ''
                play_audio(self.song_list[self.song_count], time_to_jump)
                time_slider.value = time_to_jump
                pygame.mixer.music.pause()
        else:
            input_widget.value = ''
            self.notify('Please enter a valid value (in seconds or MINUTE:SECOND)')

    def on_key(self, event: events.Key) -> None:
        def press(button_id: str) -> None:
            try:
                self.query_one(f"#{button_id}", Button).press()
            except NoMatches:
                pass

        key = event.key
        if key == "space":
            press('play')
        elif key == "n" or key == "N":
            press('next')
        elif key == "p" or key == "P":
            press('prev')
        elif key == "b" or key == "B":
            press('songselect')
        elif key == "m" or key == "M":
            press('volume')
        elif key == "j" or key == "J":
            j_input = self.query_one(Input)
            j_input.focus()

    @on(Button.Pressed, '#play')
    def playpause(self, event: Button.Pressed) -> None:
        time_slider = self.query_one("#time_slider", Slider)
        play_button = self.query_one("#play")
        if self.status == 'playing':
            pygame.mixer.music.stop()
            play_button.label = '▶'
            play_button.variant = 'default'
            self.status = 'paused'
        else:
            play_audio(self.song_list[self.song_count], time_slider.value)
            play_button.label = '■'
            play_button.variant = 'error'
            self.status = 'playing'
        time_slider.set_state(self.status)

    @on(Button.Pressed, '#prev')
    def prev_song(self, event: Button.Pressed):
        pygame.mixer.music.stop()
        time_slider = self.query_one("#time_slider", Slider)
        if time_slider.value >= 2:
            time_slider.value = 0
            play_audio(self.song_list[self.song_count], 0)
        else:
            if self.song_count == 0:
                self.song_count = len(self.song_list) - 1
            else:
                self.song_count -= 1
            song_button = self.query_one(f'#song_{self.song_count}')
            song_button.value = True
            self.update_player()

    @on(Button.Pressed, '#next')
    def next_song(self, event: Button.Pressed):
        pygame.mixer.music.stop()
        if self.song_count == len(self.song_list) - 1:
            self.song_count = 0
        else:
            self.song_count += 1
        song_button = self.query_one(f'#song_{self.song_count}')
        song_button.value = True
        self.update_player()

    @on(Button.Pressed, '#songselect')
    def show_songselect(self):
        radioset = self.query_one(RadioSet)
        songselect_button = self.query_one('#songselect')
        if radioset.styles.display == "block":
            radioset.styles.display = "none"
            songselect_button.variant = "default"

        else:
            radioset.styles.display = "block"
            songselect_button.variant = "success"
            radioset.focus()
    @on(Button.Pressed, '#volume')
    def show_volume(self):
        volume_button = self.query_one('#volume')
        volume_slider = self.query_one('#volume_slider')
        if volume_slider.styles.display == "block":
            volume_slider.styles.display = "none"
            volume_button.variant = "default"
        else:
            volume_slider.styles.display = "block"
            volume_button.variant = "success"
            volume_slider.focus()

    @on(VolumeSlider.Changed, '#volume_slider')
    def set_volume(self) -> None:
        volume_slider = self.query_one('#volume_slider')
        volume_button = self.query_one('#volume')
        if volume_slider.value == 0:
            volume_button.label = "🔇"
        elif volume_slider.value > 0 and volume_slider.value < 3.3:
            volume_button.label = "🔈"
        elif volume_slider.value > 3.3 and volume_slider.value < 6.6:
            volume_button.label = "🔉"
        else:
            volume_button.label = "🔊"
        pygame.mixer.music.set_volume(volume_slider.value / 10)


    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        if self.song_count != event.radio_set.pressed_index:
            pygame.mixer.music.stop()
            self.song_count = event.radio_set.pressed_index
            self.update_player()
        else:
            pass


    def on_mount(self, event: events.Mount) -> None:
        radioset = self.query_one(RadioSet)
        radioset.styles.display = "none"
        volume_slider = self.query_one('#volume_slider')
        volume_slider.styles.display = "none"
        self.song_count = 0
        self.status = 'playing'
        self.title = "RVRS MP"
        self.update_player()
        #self.set_interval(1/1, self.check_song)

    @on(Slider.SongEnd)
    def check_song(self, event: Slider.SongEnd) -> None:
        if self.song_count == len(self.song_list) - 1:
            self.song_count = 0
        else:
            self.song_count += 1
        song_button = self.query_one(f'#song_{self.song_count}')
        song_button.value = True
        self.update_player()

    def update_player(self) -> None:
        radioset = self.query_one(RadioSet)
        with open(os.path.join(config_dir, 'music.txt'), 'r') as f:
            self.song_list = f.read().split("\n")
            self.song_list = [os.path.join(i) for i in self.song_list if i != '']
        audio = eyed3.load(self.song_list[self.song_count])
        title_widget = self.query_one("#title")
        image_widget = self.query_one(ImageViewer)
        total_time = self.query_one('#total_time')
        time_slider = self.query_one("#time_slider", Slider)
        if audio.tag:
            if audio.tag.title:
                title_value = audio.tag.title
            else:
                title_value = os.path.splitext(os.path.basename(self.song_list[self.song_count]))[0]
            if audio.tag.images:
                image_byte = BytesIO(audio.tag.images[0].image_data)
                thumbnail = Image.open(image_byte)
            else:
                thumbnail = Image.open('music.png')
            self.total_time_value = int(audio.info.time_secs)
        if self.status == 'playing':
            play_audio(self.song_list[self.song_count], 0)
        image_widget.update(thumbnail)
        title_widget.update(title_value)
        time_slider.update(0, self.total_time_value)
        total_time.update(convert_seconds_to_mmss(self.total_time_value))
        self.set_volume()






if __name__ == "__main__":
    if sys.platform.startswith("win"):
        config_dir = os.path.join(os.environ["ProgramFiles"], "RVRS-MP")
    elif sys.platform.startswith("darwin"):
        config_dir = os.path.join(os.path.expanduser("~/Library/Application Support"), "RVRS-MP")
    elif sys.platform.startswith("linux"):
        config_dir = os.path.join(os.path.expanduser("~"), ".config", "RVRS-MP")
    if os.path.exists(os.path.join(config_dir, 'music.txt')):
        pass
    else:
        os.makedirs(config_dir, exist_ok=True)
        open(os.path.join(config_dir, 'music.txt'), "a").close()

    with open(os.path.join(config_dir, 'music.txt'), 'r') as f:
        if f.read() == '':
            print(f"Please add path to your songs to {os.path.join(config_dir, 'music.txt')}, each song seperate by a line break")
            sys.exit()
    pygame.mixer.init(frequency=192000, size=32, channels=2)

    try:
        app = Player()
        app.run()
    except KeyboardInterrupt:
        sys.exit()