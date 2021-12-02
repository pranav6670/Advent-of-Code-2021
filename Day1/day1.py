class Answer:
    def __init__(self):
        print("Advent of Code - Day 1")

    def read_input(self, filename):
        data = []
        with open(filename, "r") as t:
            for values in t.readlines():
                data.append(int(values))
        return data

    def print_values(self, list_values):
        return print([i for i in list_values])

    def calculate(self, val_array):
        count = 0
        for i in range(1, len(val_array)):
            if val_array[i - 1] < val_array[i]:
                count += 1
        return count


if __name__ == "__main__":
    a = Answer()
    data = a.read_input("./input.txt")
    a.print_values(data)
    print(a.calculate(data))






