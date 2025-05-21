def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file '{filename}' contains {word_count} words.")
    except FileNotFoundError as e:
        print(f"An error occurred: {e}")

# This part should be outside the function
filename = input("Enter the filename to count words: ")
count_words_in_file(filename)
