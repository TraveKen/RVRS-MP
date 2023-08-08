<a name="readme-top"></a>






<h3 align="center">RVRS Music Player</h3>

  <p align="center">
    A simple TUI/Text-based music player.
    <br />
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
RVRS-MP is a simple music player created using Python and Texual framework.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Previews
![preview1](https://github.com/TraveKen/RVRS-MP/blob/main/previews/1.png?raw=true)
![preview2](https://github.com/TraveKen/RVRS-MP/blob/main/previews/2.png?raw=true)
![preview3](https://github.com/TraveKen/RVRS-MP/blob/main/previews/3.png?raw=true)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* <a href="https://github.com/Textualize/textual">Textual</a></li>
* <a href="https://github.com/pygame/pygame"> Pygame
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Compatibility
### Tested on:
* Windows 10
* Debian 12
### Untested:
* MacOS


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Adding songs
For now, there isn't add/remove song feature, you'll need to manually edit the `music.txt` file. Add paths to your audio file in the `music.txt` file, each song seperate by a line break, don't leave empty line or non-existing paths.</br>
The path to the `music.txt` file for each OS is as following:
* Windows: `C:\Users\{YourUserName}\AppData\Roaming\RVRS-MP`
* Linux: `/home/{YourUserName}/.config/RVRS-MP`
* MacOS (untested): `~/Library/Application Support/RVRS-MP`

### Keybinds
* Space: Play/pause
* N: Next song
* P: Previous song
* Tab/Shift+Tab: Navigate

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Cons/Known bugs/Features to add

- [ ] Lack of in-app add/remove songs feature
- [ ] Lack of album/group feature
- [ ] Lack of app's icon (not really necessary but it would be very cool to have)
- [ ] High CPU usage when adjusting the slider
- [ ] Can't adjust the slider using keyboard (keyboard users will have to use the Input box to navigate within a song)
- [ ] Improve interface
- <a href="https://github.com/TraveKen/RVRS-MP/issues"> And many more...

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments
### A part of the source code is from:
* <a href="https://github.com/adamviola/textual-imageview"> textual-imageview
* <a href="https://github.com/TomJGooding/textual-slider"> textual-slider

### And an icon from:
* <a href="https://github.com/daniruiz/flat-remix"> Flat Remix icons pack

## Changes made to pre-exist codes
### textual-imageviewer
- Removed some unnecessary features
- Added `update` feature to change the image
### textual-slider
- Added `SongEnd` event
- Added `set_state` function
- Added `update` function
