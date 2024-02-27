import re
import sys

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    sum_enabled = False
    total = 0
    equals_count = 0

    words = re.findall(r'(?i:on|off|\d+|=)', text)

    for word in words:
        if word.lower() == "on":
            sum_enabled = True
        elif word.lower() == "off":
            sum_enabled = False
            total = 0
        elif sum_enabled and word.isdigit():
            total += int(word)
        elif word == "=":
            equals_count += 1
            print(f"{equals_count}º '=': {total}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python somador.py <file_path>")
        return
    
    file_path = sys.argv[1]
    process_text(file_path)

if __name__ == "__main__":
    main()
