from rover import Rover


def test_reports_position():
    rover1 = Rover()
    assert rover1.positionAndDirection() == "N:0:0"


def test_forward():
    rover1 = Rover()
    rover1.move("f")


def test_one_movement():
    rover1 = Rover()
    rover1.move("f")
    assert rover1.positionAndDirection() == "N:1:0"


def test_one_movement_backwards():
    rover1 = Rover()
    rover1.move("b")
    assert rover1.positionAndDirection() == "N:-1:0"


def test_rotate_rover_left():
    rover1 = Rover()
    rover1.move("l")
    assert rover1.positionAndDirection() == "W:0:0"


def test_rotate_left_move_forward():
    rover1 = Rover()
    rover1.move("l")
    rover1.move("f")
    assert rover1.positionAndDirection() == "W:1:0"


def test_rotate_two_lefts():
    rover1 = Rover()
    rover1.move("l")
    rover1.move("l")
    assert rover1.positionAndDirection() == "S:0:0"


def test_multiple_commands():
    rover1 = Rover()
    rover1.move("fl")
    assert rover1.positionAndDirection() == "W:1:0"


def test_rotate_right():
    rover1 = Rover()
    rover1.move("r")
    assert rover1.positionAndDirection() == "E:0:0"


def test_clock_overflow():
    rover1 = Rover()
    rover1.move("rrrr")
    assert rover1.positionAndDirection() == "N:0:0"
