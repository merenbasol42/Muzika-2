from src import Program
from os import path

def main():
    ws_path = path.dirname(path.abspath(__file__))
    program = Program(ws_path)
    program.run()

if __name__ == "__main__":
    main()
