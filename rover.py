class Rover:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        # Our clock has North = 0, East = 1, South = 2, West = 3
        self.clock = 0

    def positionAndDirection(self):
        clock_str = "NESW"
        return f"{clock_str[self.clock]}:{self.x}:{self.y}"

    def move(self, commands):

        for command in commands:

            if command == "f":
                self.x += 1

            elif command == "b":
                self.x -= 1

            elif command == "l":
                self.clock -= 1

            elif command == "r":
                self.clock += 1
