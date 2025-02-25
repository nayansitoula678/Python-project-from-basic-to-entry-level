def read_file(file):
    try:
        file = open(file, "r")  
        content = file.read()
        print("File Content:\n", content)
    except FileNotFoundError:  
        print(f"Error: The file '{file}' does not exist.")
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            file.close() 
            print("File closed successfully.")
        except NameError:
            print("No file to close.")


read_file("nonexistent.txt") 
