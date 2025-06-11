# ASCII Art

This project is a terminal-based ASCII art generator built with Python.  
It loads image files, automatically resizes and applies color, and then converts them into color ASCII art directly in the terminal.  
The output can also be saved as a `.txt` file (without color).

## Features

- Converts image files into **color ASCII art**
- Displays output directly in the **terminal**
- Saves ASCII art as a **`.txt` file** (color removed)
- Provides a **user-friendly CLI interface**
- Supports path shortcuts like `~`, `/`, etc.

## Motivation

I wanted to express simple images as text-based art using Python.  
I was inspired by the idea that visual creativity can happen even within the terminal, so I started this project to explore that concept.

## Commands

- `make [name] [image_path]` - Create a new ASCII art from an image
- `list` - Show a list of all created ASCII art
- `print [name]` - Display a specific ASCII art in the terminal
- `save [name]` - Save a specific ASCII art to a `.txt` file
- `exit` - Exit the program

### Example
```bash
make hack-club ./demo/hack-club.png
list
print hack-club
save hack-club
exit
