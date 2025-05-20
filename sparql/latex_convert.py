
# loop over files in this dir
import os
import re

def convert_text_to_latex(text):
    result = "\\begin{verbatim}"
    for line in text.splitlines():
        result += line + "\\\\"
    result += "\\end{verbatim}"
    return result

def convert_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".sparql"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                latex_text = convert_text_to_latex(text)
                print("file:", filename)
                print(latex_text)
                print("")

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    convert_files_in_directory(directory)