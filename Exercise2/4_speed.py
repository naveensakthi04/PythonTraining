speed_limit = 70


def check_speed(speed):
    try:
        speed = int(speed)
    except Exception:
        print("Invalid input")
        return False
    return True


def get_speed():
    speed = input("Enter the speed: ")
    check = check_speed(speed)
    if check:
        return speed
    else:
        return get_speed()


def calculate_points(speed):
    global speed_limit
    if speed < speed_limit:
        return "OK"
    else:
        speed -= speed_limit
        points = speed // 5
        if points <= 12:
            return "Points: {}".format(points)
        else:
            return "License suspended!"


# Driver code
speed = int(get_speed())
result = calculate_points(speed)
print(result)
