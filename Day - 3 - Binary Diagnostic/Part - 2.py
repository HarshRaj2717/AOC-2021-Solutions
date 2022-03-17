from input import input_text


def main():
    ratings = {}
    for h in range(2):
        input_text_copy = input_text.copy()
        input_text_copy2 = input_text.copy()
        while len(input_text_copy) > 2:
            try:
                for i in range(len(input_text[0])):
                    list1 = []

                    for j in range(len(input_text)):
                        list1.append(input_text[j][i])

                    if list1.count('0') > list1.count('1'):
                        for k in input_text_copy:
                            if k[0] == '1' and h == 0:
                                print(input_text_copy2.count(k))
                                input_text_copy2.remove(k)
                            if k[0] == '0' and h == 1:
                                input_text_copy2.count(k)
                                print(input_text_copy2.remove(k))

                    else:
                        for k in input_text_copy:
                            if k[0] == '0' and h == 0:
                                print(input_text_copy2.count(k))
                                input_text_copy2.remove(k)
                            if k[0] == '1' and h == 1:
                                print(input_text_copy2.count(k))
                                input_text_copy2.remove(k)

                input_text_copy = input_text_copy2.copy()

            except Exception as e:
                print("err :",e)
                print(input_text_copy)
                print(input_text_copy2)

        if h == 0:
            ratings["oxygen_generator"] = int(input_text_copy[0], 2)
        else:
            ratings["co2_scrubber"] = int(input_text_copy[0], 2)

    print(ratings["oxygen_generator"] * ratings["co2_scrubber"])


if __name__ == "__main__":
    main()
