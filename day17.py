from utils import read_input

X_RANGE = (156, 202)
Y_RANGE = (-110, -69)


def hits_target(vx, vy, x_range, y_range):
    x, y = 0, 0
    while x <= x_range[1] and y >= y_range[0]:
        if (x_range[0] <= x and y_range[1] >= y):
            return True
        x += vx
        y += vy
        vx = max(vx - 1, 0)
        vy -= 1
    return False
    

def part_two(x_range=X_RANGE, y_range=Y_RANGE):
    result = []
    for vx in range(0, 203):
        for vy in range(-110, 110):
            if hits_target(vx, vy, x_range, y_range):
                result.append((vx, vy))
    return len(result)


if __name__ == "__main__":
    print(part_two())
