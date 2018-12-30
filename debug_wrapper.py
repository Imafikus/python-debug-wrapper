import argparse

def debug_print(*args):
    """
    Receive any number of arguments to print, and print them
    separated by ' '

    If you want a new line PUT IT INTO STRING!
    """

    for item in args:
        if(item[-1] == '\n'):
            print(item, end='')
        else:
            print(item, end='')
            
    
def remove_debug(old_fpath):
    """
    Make a copy of the file specified by the old_fpath
    which has all debug prints removed.

    It creates a file in the same folder where is your file.
    """
    KEYWORD = "debug_print"

    new_fpath = "cleaned_debug_" + old_fpath

    f = open(old_fpath, "r")
    all_lines = f.readlines()
    f.close()

    cleaned_lines = []
    for line in all_lines:
        if KEYWORD not in line:
            cleaned_lines.append(line)

    f = open(new_fpath, "w")
    for line in cleaned_lines:
        f.write(line)
    f.close()
    
if __name__ == "__main__":
    
    parser_desc = """
        Make a copy of the file specified by old_file_path 
        which has all lines where debug_print is used removed.
    """
    parser = argparse.ArgumentParser(description=parser_desc)
    parser.add_argument('old_file_path', type=str, help="Path to original file.")
    
    args = parser.parse_args()

    remove_debug(args.old_file_path)