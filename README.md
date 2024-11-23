# Directory Tree
Coding a directory tree using os, sys, pathlib, argsparser modules in Python.

Got help from [realpython.com](https://www.realpython.com)
## User Guide
Use `python tree.py -h  ` command to see help massage :
```console
usage: Directory Tree [-h] [-v] [-d] [-e [EXTENTION]] [DIRECTORY]

itzsadraa Directory Tree

positional arguments:
  DIRECTORY             Generate a full directory starting at [DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show programs version number and exit
  -d, --dir-only        Generate a only directory tree
  -e [EXTENTION], --extention [EXTENTION]
                        Find files with a specific extention in a directory

Thanks for using itzsadraa Directory Tree
```

example of using Directory Tree:
```console
> python tree.py "../Game"

../Game/
│
├── Game files/
│   ├── __init__.py
│   └── MyGame.py
│
├── tests/
│   └── test_game.py
│
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## Library 
You can use `TreeClasses.py` library to make your own file with `DirectoryTree` class and self methodes.
