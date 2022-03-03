from input import input_text


def main():
    horizontal = 0
    depth = 0

    for i in input_text:
        if i[0] == 'f':
            horizontal += int(i[-1])
        elif i[0] == 'd':
            depth += int(i[-1])
        elif i[0] == 'u':
            depth -= int(i[-1])

    print(horizontal*depth)


if __name__ == "__main__":
    main()
