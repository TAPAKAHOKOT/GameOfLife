import time
import os
import keyboard as kb
import curses

os.system("mode con cols={} lines={}".format( 300 , 100) )
# line = [*map(int, input().split(" "))]
# arr = []

# for k in range(line[1]):
#     arr.append(list(input()))
def draw_field(arr):
    for k in arr: print(" ".join(k))


def create_data():
	size = []

	file = open("life_map.txt", "r").read()

	arr = file.split(",\n")



	for k, item in enumerate(arr):
	    arr[k] = item.split(" ")
	    arr[k] = arr[k]

	arr = arr
	size.append(len(arr))
	size.append(len(arr[0]))

	# size = [*map(int, input().split(" "))]
	# arr = []
	# for k in range(size[0]):
	#     arr.append(list(input()))

	graphics = ["#", "."]

	return arr, size, graphics


def check_death(arr, pos, size, graphics, life = True):
    r, k = pos[0] - 1, pos[1] - 1
    count = 0

    def check_over_pos(pos, size, y=0,x=0):
        y, x = pos[0], pos[1]
        if pos[0] < 0: y = pos[0] + size[0]
        if pos[0] > (size[0] - 1): y = pos[0]- size[0]
        if pos[1] < 0: x = pos[1] + size[1]
        if pos[1] > (size[1] - 1): x = pos[1] - size[1]
        return y, x
    # print(check_over_pos([-1, 5], [5, 5]))
    for j in range(3):
        for i in range(3):
            gg = True if [r, k] != pos else False
            r, k = check_over_pos([r, k], size)
            if arr[r][k] == graphics[0] and gg: count += 1
            k += 1
        r += 1
        k = pos[1] - 1
    # print(count)
    if 2 <= count <= 3 and life: return graphics[0]
    elif not life and count == 3: return graphics[0]
    else: return graphics[1]
# check_death(arr, [0, 0], size, True)
def make_a_step(arr, size, graphics):
    all_field = []
    for k in range(size[0]):
        rows = []
        for i in range(size[1]):
            if arr[k][i] == graphics[0]: sost = True
            else: sost = False

            l = check_death(arr, [k, i], size, graphics, sost)
            rows.append(l)
        all_field.append(rows)
    return all_field


os.system("cls")
time.sleep(1)
def run(stdscr):
	stdscr.clear()
	stdscr.refresh()

	curses.start_color()
	for k in range(255):
		curses.init_pair(k + 1, k, curses.COLOR_BLACK)

	arr, size, graphics = create_data()
	num = 0
	while True:
		num += 1

		arr = make_a_step(arr, size, graphics)

		time.sleep(0.01)
		for y, part in enumerate(arr):
			for x, symbol in enumerate(part):
				if symbol == "#": col = 1
				else: col = 225

				stdscr.addstr(y, x * 2, symbol + " ", curses.color_pair(col))
		stdscr.refresh()

		s = 0
		for k in arr: s += "".join(k).count(".")
		if s == size[0] * size[1]: 
			print("\nYour score is {}".format(num))
			break



def main():
	curses.wrapper(run)

if __name__ == "__main__":
	main()