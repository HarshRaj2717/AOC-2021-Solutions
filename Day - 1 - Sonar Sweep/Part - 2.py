from input import input_text


def main():
    increased = 0
    for i in range(len(input_text)-3):
        a = int(input_text[i]) + int(input_text[i+1]) + int(input_text[i+2])
        b = int(input_text[i+1]) + int(input_text[i+2]) + int(input_text[i+3])
        if a < b:
            increased += 1
    print(increased)


if __name__ == "__main__":
    main()
