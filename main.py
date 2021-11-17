def my_operation(input_nb):
    return 2 * input_nb


def load_data():
    with open("./data.txt", "r") as file:
        data = file.read()
    return int(data)


if __name__ == "__main__":
    a = load_data()
    print(my_operation(a))
