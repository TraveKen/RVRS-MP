<a name="readme-top"></a>




![applogo](https://github.com/TraveKen/RVRS-MP/blob/main/previews/logo.png?raw=true)

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


## Install
### Windows
* Download and run the installer: https://github.com/TraveKen/RVRS-MP/releases/download/1.0/rvrsmp_windows_1.0_x64_install.exe

### Debian-based distros
* Download the package: https://github.com/TraveKen/RVRS-MP/releases/download/1.0/rvrsmp_1.0_amd64.deb
* Run `sudo dpkg -i rvrsmp_1.0_amd64.deb`

### Other distros
* You'll need to download the binary and manually install: https://github.com/TraveKen/RVRS-MP/releases/download/1.0/rvrsmp_linux_x64

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Running/Compiling from source
### Wil be updated...

<!-- USAGE EXAMPLES -->
## Usage

### Start
* Run `rvrsmp` in a terminal

### Adding songs
For now, there isn't add/remove song feature, you'll need to manually edit the `music.txt` file. Add paths to your audio file in the `music.txt` file, each song seperate by a line break, don't leave empty line or non-existing paths.</br>
The path to the `music.txt` file for each OS is as following:
* Windows: `C:\Users\{YourUserName}\AppData\Roaming\RVRS-MP`
* Linux: `/home/{YourUserName}/.config/RVRS-MP`
* MacOS (untested): `~/Library/Application Support/RVRS-MP`

### Keybinds
* Tab/Shift+Tab: Navigate
* Enter: Press/Choose/Submit
* Space: Play/pause
* N: Next song
* P: Previous song
* B: Show song list
* M: Show volume slider
* J: Focus the Input widget

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Cons/Known bugs/Features to add

- [ ] Add in-app add/remove songs feature
- [ ] Add album/group feature
- [ ] Add app's icon (not really necessary but it would be very cool to have)
- [ ] Add Discord rich presence
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
- Removed some unnecessary functions
- Added `update` function to change the image
### textual-slider
- Added `SongEnd` event
- Added `set_state` function
- Added `update` function
