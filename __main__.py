from src import Program
from os import path

def main():
    ws_path = path.dirname(path.abspath(__file__))
    program = Program(ws_path)
    program.run()


class A:
    def __new__(cls):
        return super().__new__(cls)
    
    def __init__(self):
        print("haho")

if __name__ == "__main__":
    main()
