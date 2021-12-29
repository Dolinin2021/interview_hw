from balance import check_str


if __name__ == '__main__':

    example = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}",
               "}{}", "{{[(])]}}", "[[{())}]"]

    for str in example:
        print(f"{str} - {check_str(str)}")
