# python-debug-wrapper
Simple library made to make my (and hopefully your) life easier after I've finished with debugging.

## Why I made this?
If you are like me, you are probably debugging your program with lots of print statements. So you've probably ,more that a few times, ended up with some random prints and you had no idea where those suckers are called. So you spent a few minutes going through all the lines looking for it. This library is made so you don't have to to that any more.

## Usage

Library is just *debug_wrapper.py* file, and for now it only has 2 functions:

- **debug_print** is just a simple wrapper for standard *print()*. You want to call your debug prints with this function instead of standard print.

- **remove_debug** goes through your code and removes all *debug_print* calls from it, so you are left just with your debugged code.  
That debug code is written into file which has the name: *'cleaned_debug' + old_file_name*.  
**Your old file will be intact!** This is done in case something unexpected happens or if you just want to hold on to the debug version a little bit longer. 

## Dependencies
- [Python 3.x](https://python.org)
- [argparse](https://docs.python.org/3/library/argparse.html) library for Python 3.x - Used to make nice CLI

