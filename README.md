# AirBnB clone - The console

## Project Description
AirBnb clone Project is Python-based application that replicates the core functionality of the popular [Airbnb](https://www.airbnb.com/) platform in a simpler manner.
It utilizes data persistance through JSON files and providing interaction via a custom command-line interpreter.

### The Command-line interpreter
The Command-Line Interpreter (CLI) is a text-based interface designed to interact with the Airbnb Clone Project. It serves as the primary means of communication between users and the application. The CLI allows users to issue text commands and receive responses from the system, all within the command-line environment.


## General Use
1. Clone this repository
2. Move into the directory and locate "console.py" at the root and run it
```bash
/AirBnB_clone$ ./console.py
```
3. The following prompt should appear if the console launched successfully
```bash
(hbnb)
```
4. Use help command to get a list of available commands
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
5. Using "help" command with an available command you give you more information about the command
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
 Creates new instance of BaseModel class or subclass
```
6. Use "quit" command to exit the console
```bash
(hbnb) quit
```
