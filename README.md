# ALX AirBnB Clone Project - The Console

![App Screenshot]9https://repository-images.githubusercontent.com/520063788/a91abf2d-82e3-40e6-96d7-75043c684ff3)

## Description
In this project, we are building the airbnb console.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Single Use function. A command line interface from which we can create, modify and delete objects in the file storage.

## How it should work in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================

EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

## How it should work in non-interactive mode:

```
$echo "help" | ./console.py
(hbnb)

Documented command (type help <topic>):
=======================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
```
