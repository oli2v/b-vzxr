import numpy as np
import matplotlib.pyplot as plt


def main():
    # Read width and height
    uni = open("instructions/universe.txt", "r").readlines()
    width = int(uni[0].split(":")[1])
    height = int(uni[1].split(":")[1])

    # Read instructions
    instructions = open("instructions/instruction_list.txt", "r").readlines()

    # Initialize postion and orientation
    x, y = 0, 0
    theta = np.pi / 2

    # Read instructions
    positions = []
    for instruction in instructions:
        direction, k = instruction.split(",")
        k = int(k)
        if direction == "right":
            theta -= np.pi / 2
        else:
            theta += np.pi / 2
        theta = theta % (2 * np.pi)
        dx = k * np.cos(theta)
        dy = k * np.sin(theta)
        if (x + dx) > width:
            x = width
        elif (x + dx) < 0:
            x = 0
        else:
            x += dx
        if (y + dy) > height:
            y = height
        elif (y + dy) < 0:
            y = 0
        else:
            y += dy
        x = int(round(x))
        y = int(round(y))
        positions.append((x, y))

    # Plot positions iteratively
    plot_positions(width, height, positions)

    # Print result
    print("The final (x, y) position of B-VZXR is", positions[-1])


def plot_positions(w, h, positions):
    plt.axis([0, w, 0, h])
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    color = ["b"] * (len(positions) - 1) + ["r"]
    markers = ["x"] * (len(positions) - 1) + ["o"]

    for i in range(len(positions)):
        x, y = positions[i]
        plt.scatter(x, y, marker=markers[i], c=color[i])
        plt.title("Instruction #" + str(i + 1))
        plt.pause(0.05)

    plt.show()


if __name__ == "__main__":
    main()
