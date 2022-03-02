from input import input_text


def main():
    increased = 0
    for i in range(len(input_text)-1):
        if int(input_text[i]) < int(input_text[i+1]):
            increased += 1
    print(increased)


if __name__ == "__main__":
    main()
