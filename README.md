# airdefence

An addictive, arcade-like, 2D air defence game, made with *Python3* and *Pygame*

### **BETA** v0.7 ###

## How to play ##

**Shoot down incoming enemy aircraft, by launching missiles with your mouse.**

The missiles will fly in the direction you click. They have no homing device,
so you need to lead your targets.

Your ship has four (4) missile tubes. The tubes are reloaded as you use them,
but there is a small delay. If you shoot all four missiles very quickly, you
need to wait for at least one tube to be reloaded, in order to fire again.

The game ends, when three (3) enemies have escaped.

The *highest* score of *the session* is displayed at the top of the *main menu*.

### Key Bindings ###

| Action | Key                     |
| ------ | ----------------------- |
| Shoot  | any mouse button        |
| Start  | Enter / Space-Bar       |
| Stop   | Enter / Space-Bar / Esc |
| Exit   | Esc                     |

### Menu ###

In *Main Menu*, you can enter Full Screen mode by clicking on the game resolution.

## Install and Run ##

### Run with python (recommended) ###

Requrements:
- [Python3](https://www.python.org/downloads/)
  - Windows: [Download Python3](https://www.python.org/downloads/)
  - Debian Linux: ```apt-get install python3.8```
- [Pygame](https://www.pygame.org/wiki/GettingStarted):
  - ```python3 -m pip install pygame```


### Run exe in Windows ###
- ~~Copy the **game.exe** from ```airdefence/dist``` to the game root folder ```airdefence```~~
- Double-click **game.exe** to run

**Note:** In the unlikely case that the game would **crash** or **be killed with** ***Task Manager***,
a temporary folder (approx. 20 MB in size) created in to ```[User]\AppData\Local\Temp\_MEIxxxxx``` would be
left behind. A new folder is created each time, the new never effecting the old.
**To free the space, you need to delete the folder manually.**

## TO-DO ##
- highlite selection
- turn the missiles along their launch vector
- more refactoring...
- ~~implement different resolutions~~ (basic scaling implemented)

### CI ###

![Build exe for Windows](https://github.com/JValtteri/airdefence/workflows/Build%20exe%20for%20Windows/badge.svg)

CI does not work. EXE Must be built manually.
- Batch files for making a fresh *virtual enviroment*: ```setup_venv.bat``` and
- building an exe ```build_exe.bat``` are supplied for you.

### BATCH FILES DO NOT WORK ###
**RUN THE COMMANDS IN THE BATCH FILES MANUALLY**

The problem is thath batch files stop when starting the venv.
