import sys
import os
import re
from simple_term_menu import TerminalMenu


def main():
    if os.name == "posix":
        from .mac import main
        main()
    
if __name__ == '__main__':
    main()