

#Part 1
#Open file input.txt and read line by line. Adding the value of the line to frequency. Print frequency.
def part1(values):
    frequency = 0
    for value in values:
        frequency += value
    print(frequency)


def part2(values):
    individual_frequency = set()
    frequency = 0
    while True:
            for value in values:
                frequency += int(value)
                if frequency in individual_frequency:
                    print(frequency)
                    return
                individual_frequency.add(frequency)




if __name__ == "__main__":
    values = []
    with open("input.txt") as f:
        for line in f:
            values.append(int(line))
    part1(values)
    part2(values)