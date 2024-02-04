import sys
import colorama
from colorama import Fore, init, Style
import pathlib
from pathlib import Path


def dir_structure_visualization(path, indent='-'):
    init(autoreset=True)  # Ініціалізація colorama
    for entry in path.iterdir():
        if entry.is_dir():
            print(Fore.BLUE + indent + '\U0001F4C1 ' + entry.name)
            dir_structure_visualization(entry, ' ' + indent)
        else:
            print(Fore.GREEN + indent + '\U0001F4C4 ' + entry.name)


def main():
    try:
        if len(sys.argv)!=2:
            print('Path is not defined!')
            sys.exit()

        path_dir=Path(sys.argv[1])
        
        if not path_dir.exists:
            print(f'{path_dir.absolute()} is not exist')
            sys.exit()

        dir_structure_visualization(path_dir)  
        
    except Exception as e:
        print(f'ERROR: {e}')
    

if __name__ == '__main__':
    main()
