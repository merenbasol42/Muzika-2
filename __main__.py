
def main():
    from src import Program
    from os import path
    
    space_path: str = path.dirname(__file__)

    program = Program(
        pls_dir_path = path.join(space_path, "playlists")
    )
    
    program.run()

if __name__ == "__main__":
    main()