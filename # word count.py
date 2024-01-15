# word count
def count_words_in_file(file_path):
    try:
        with open(file_path)as file:
            Content = file.read()
            word_count = len(Content.split())
            return word_count
    except FileNotFoundError :
        print("file not found. please provide a valid file path.")
        return -1
    
    
if __name__ == "__main__":
            try:
                file_path = input("Enter the path of the text file:")
                num_words = count_words_in_file(file_path) 
                
                if num_words >= 0:
                    print(f"numer of words in the file: {num_words}")
            except KeyboardInterrupt:
                print("\nProgram interrupted.")
            except Exception as e:
                print(f"An error occurred: {e}")
                