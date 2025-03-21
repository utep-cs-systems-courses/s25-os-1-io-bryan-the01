import re
import sys

def word_count(inText, outText):
    with open(inText, "r") as file:
        word_dict = {}
        text = file.read().lower()
    words = re.findall(r"\b\w+\b", text)

    for word in words:
        word_dict[word] = word_dict.get(word, 0)+1

    sorted_list = sorted(word_dict.items())
    with open(outText, "w") as file:
        for word,  count in sorted_list:
            file.write(f"{word} {count}\n")
            
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 Assn1NoOS.py input_file output_file")
    else:
        word_count(sys.argv[1], sys.argv[2])
