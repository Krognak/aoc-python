with open("2015/day03/input.txt") as f:
    data = f.read()


def locations(instructions):
    """Return locations visited in part 1"""
    current_loc = (0, 0)
    locations = set()
    locations.add(current_loc)
    for direction in instructions:
        if direction == "<":
            current_loc = (current_loc[0] - 1, current_loc[1])
            locations.add(current_loc)
        elif direction == ">":
            current_loc = (current_loc[0] + 1, current_loc[1])
            locations.add(current_loc)
        elif direction == "^":
            current_loc = (current_loc[0], current_loc[1] + 1)
            locations.add(current_loc)
        else:
            current_loc = (current_loc[0], current_loc[1] - 1)
            locations.add(current_loc)
    return locations


def combined_locations(instructions):
    """Return locations visited in part 2"""
    santa_data = instructions[0::2]
    robot_data = instructions[1::2]
    return locations(santa_data).union(locations(robot_data))


if __name__ == "__main__":
    print(len(locations(data)))
    print(len(combined_locations(data)))
