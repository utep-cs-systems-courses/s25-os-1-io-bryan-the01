import re
import sys
import os

def word_count(inText, outText):
    text = ""
    fd = os.open(inText, os.O_RDONLY)
    while True:
        chunk = os.read(fd, 4096)
        if not chunk:
            break
        text += chunk.decode().lower()
    os.close(fd)
    
    word_dict = {}
    words = re.findall(r"\b\w+\b", text)

    for word in words:
        word_dict[word] = word_dict.get(word, 0)+1

    sorted_list = sorted(word_dict.items())

    fd = os.open(outText, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    for word, freq in sorted_list:
        os.write(fd, f"{word} {freq}\n".encode())
    os.close(fd)
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 Assn1NoOS.py input_file output_file")
    else:
        word_count(sys.argv[1], sys.argv[2])
