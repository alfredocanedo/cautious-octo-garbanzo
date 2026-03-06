import sys

# Function to retrieve input and output file paths from user.
def get_file_paths():
    input_file_path = input("Please enter the input file path: ")
    output_file_path = input("Please enter the output file path: ")
    return input_file_path, output_file_path

if __name__ == '__main__':
    input_file, output_file = get_file_paths()
    # Further processing with input_file and output_file
