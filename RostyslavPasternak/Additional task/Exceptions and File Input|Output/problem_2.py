from random import choice

def random_walk(max_iters=1e12):
    walk = 0
    directions = [1, -1]

    try:
        for i in range(int(max_iters)):
            walk += choice(directions)
    except KeyboardInterrupt:
        print(f"Process interrupted at iteration {i}")
    else:
        print("Process completed")

    return walk


if __name__ =="__main__":
    result = random_walk()
    print("Final position:", result)