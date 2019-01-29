# Day 13 part 1+2


class Cart:
    def __init__(self, id, x, y, velocity):
        self.id = id
        self.x = x
        self.y = y
        self.velocity = velocity
        self.junctions = 0
        self.crashed = False


def parse(file_name):
    junctions = []
    corners = []
    carts = []
    with open(file_name) as f:
        i = 0
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line):
                if char == "+":
                    junctions.append((x, y))
                if char == "/" or char == "\\":
                    corners.append((x, y, char))
                if char == ">" or char == "<" or char == "^" or char == "v":
                    carts.append(Cart(i, x, y, get_velocity(char)))
                    i = i + 1

    return junctions, corners, carts


def get_velocity(cart_str):
    x = 0 if cart_str == "^" or cart_str == "v" else 1 if cart_str == ">" else -1
    y = 0 if cart_str == ">" or cart_str == "<" else 1 if cart_str == "v" else -1
    return x, y


def tick(junctions, corners, carts):
    sorted_cars = sorted(carts, key=lambda cart: (cart.y, cart.x))

    for cart in sorted_cars:
        if cart.crashed:
            continue

        cart.x = cart.x + cart.velocity[0]
        cart.y = cart.y + cart.velocity[1]

        for other_cart in sorted_cars:
            if other_cart.id != cart.id and cart.x == other_cart.x and cart.y == other_cart.y and not other_cart.crashed:
                print("Collision", (cart.x, cart.y))
                cart.crashed = True
                other_cart.crashed = True

        corner_cols = [x for x in corners if x[0] == cart.x and x[1] == cart.y]
        if len(corner_cols) > 0:
            corner = corner_cols[0]
            if corner[2] == "/":
                if cart.velocity[1] == 0:
                    cart.velocity = (0, -cart.velocity[0])
                else:
                    cart.velocity = (-cart.velocity[1], 0)

            if corner[2] == "\\":
                if cart.velocity[1] == 0:
                    cart.velocity = (0, cart.velocity[0])
                else:
                    cart.velocity = (cart.velocity[1], 0)

        if len([x for x in junctions if x[0] == cart.x and x[1] == cart.y]) > 0:
            cart.junctions = cart.junctions + 1

            if cart.junctions % 3 == 1:
                if cart.velocity[1] == 0:
                    cart.velocity = (0, -cart.velocity[0])
                else:
                    cart.velocity = (cart.velocity[1], 0)

            if cart.junctions % 3 == 0:
                if cart.velocity[1] == 0:
                    cart.velocity = (0, cart.velocity[0])
                else:
                    cart.velocity = (-cart.velocity[1], 0)

    return [cart for cart in sorted_cars if not cart.crashed]


j, c, k = parse("input")
import time
start = time.time()


z = 0
while len(k) != 1:
    # print(z)
    k = tick(j, c, k)
    z +=1

print(k[0].x, k[0].y)
print(time.time() - start)