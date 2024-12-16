import time
import keyboard

""" Advent of Code solver class """
d = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)
}

def task1():
    """ Task 1 solver """
    result = 0
    with open('sample-big.txt', 'r', encoding='utf8') as file_handle:
        inp = [line.strip() for line in file_handle]
    whstart = []
    mv = []
    rstart = (0, 0)
    for row, line in enumerate(inp):
        if line[:1] == "#":
            l = []
            for col, val in enumerate(line):
                l.append(val)
                if val == "@":
                    rstart = (row, col)
            whstart.append(l)
        elif line != "":
            mv.append(line)
    mv = "".join(mv)
    maxr = len(whstart)
    maxc = len(whstart[0])
    wh1 = whstart.copy()
    robot = (rstart[0], rstart[1])
    for move in mv:
        dr = d[move][0]
        dc = d[move][1]
        i = 0
        while 0 < robot[0]+i*dr < maxr-1 and 0 < robot[1]+i*dc < maxc-1 and wh1[robot[0]+i*dr][robot[1]+i*dc] != "#":
            if wh1[robot[0]+i*dr][robot[1]+i*dc] == ".":
                wh1[robot[0]+i*dr][robot[1]+i*dc] = "O"
                wh1[robot[0]+dr][robot[1]+dc] = "@"
                wh1[robot[0]][robot[1]] = "."
                robot = (robot[0]+dr, robot[1]+dc)
                break
            i += 1
        #print(f"Move {move}:")
        #for l in wh1:
        #    print("".join(l))
        #print("\n")
    for r, row in enumerate(wh1):
        for c, el in enumerate(row):
            if el == "O":
                result += r*100 + c
    return result

start = time.time()
print("Task 1 result:", task1(), f"(time: {(time.time()-start)*10**3:.03f}ms)")

def task2():
    """ Task 2 solver """
    with open('input.txt', 'r', encoding='utf8') as file_handle:
        inp = [line.strip() for line in file_handle]

    wh2 = []
    mv = []
    robot = (0, 0)
    for row, line in enumerate(inp):
        if line[:1] == "#":
            l = []
            for col, val in enumerate(line):
                if val == "#":
                    l.append("#")
                    l.append("#")
                if val == "O":
                    l.append("[")
                    l.append("]")
                if val == ".":
                    l.append(".")
                    l.append(".")
                if val == "@":
                    l.append("@")
                    l.append(".")
                    robot = (row, col*2)
            wh2.append(l)
        elif line != "":
            mv.append(line)
    mv = "".join(mv)
    maxr = len(wh2)
    maxc = len(wh2[0])

    #for l in wh2:
    #    print("".join(l))
    #print("\n")

    stop = 0
    for move in mv:
        stop += 1
        i = 1
        seen = []

        # "easier" case: move sideways. only need to place boxes after move (if space)
        if move == "<" or move == ">":
            dc = d[move][1]
            while 0 < robot[1]+i*dc < maxc-1 and wh2[robot[0]][robot[1]+i*dc] != "#":
                #print(move, dc, i, robot[1]+i*dc, wh2[robot[0]][robot[1]+i*dc])
                if wh2[robot[0]][robot[1]+i*dc] != ".":
                    seen.append((robot[0], robot[1]+i*dc, wh2[robot[0]][robot[1]+i*dc]))
                    i += 1
                else:
                    for _ in range(i-1):
                        r, c, v = seen.pop(0)
                        wh2[r][c+dc] = v
                    wh2[robot[0]][robot[1]] = "."
                    wh2[robot[0]][robot[1]+dc] = "@"
                    robot = (robot[0], robot[1]+dc)
                    break

        if move == "^" or move == "v":
            dr = d[move][0]
            while 0 < robot[0]+i*dr < maxr-1:
                # no boxes!
                if len(seen) == 0:
                    # hit wall, end
                    if wh2[robot[0]+i*dr][robot[1]] == "#":
                        break
                    # free spot, move and end
                    elif wh2[robot[0]+i*dr][robot[1]] == ".":
                        wh2[robot[0]][robot[1]] = "."
                        wh2[robot[0]+dr][robot[1]] = "@"
                        robot = (robot[0]+dr, robot[1])
                        break
                    # add box
                    elif wh2[robot[0]+i*dr][robot[1]] != "#":
                        if wh2[robot[0]+i*dr][robot[1]] == "[":
                            seen.append((robot[0]+i*dr, robot[1], "[", robot[1]+1, "]"))
                        else:
                            seen.append((robot[0]+i*dr, robot[1]-1, "[", robot[1], "]"))
                # we got boxes in front of us... need to look 2 ahead
                else:
                    # there might be multiple boxes! check all on same row!
                    check = []
                    for box in reversed(seen):
                        if len(check) == 0:
                            check.append(box)
                        else:
                            if box[0] == check[0][0]:
                                check.append(box)
                    #first check if there's any wall or free space
                    free = True
                    wall = False
                    for box in check:
                        cc1 = box[1]
                        cc2 = box[3]
                        # we hit a wall!
                        if wh2[robot[0]+i*dr][cc1] == "#" or wh2[robot[0]+i*dr][cc2] == "#":
                            wall = True
                            break
                        elif wh2[robot[0]+i*dr][cc1] in ["[","]"] or wh2[robot[0]+i*dr][cc2] in ["[","]"]:
                            free = False
                    if wall:
                        break
                    for box in check:
                        cc1 = box[1]
                        cc2 = box[3]
                        # we hit a free spot, do the moving! (but only if there's no more boxes in this row to check)
                        if free:
                            for j in reversed(range(len(seen))):
                            #for j in range(i-1):
                                r, c1, v1, c2, v2 = seen.pop()
                                #if stop == 874:
                                #    print(stop, r, c1, v1, c2, v2)
                                wh2[r+dr][c1] = v1
                                wh2[r+dr][c2] = v2
                                wh2[r][c1] = "."
                                wh2[r][c2] = "."
                                if j == 0:
                                    wh2[robot[0]][robot[1]] = "."
                                    if c1 == robot[1]:
                                        wh2[r][c1] = "@"
                                        robot = (r, c1)
                                    else:
                                        wh2[r][c2] = "@"
                                        robot = (r, c2)
                        # more boxes... are they on the first or second box ahead?
                        elif wh2[robot[0]+i*dr][cc1] == "[":
                            seen.append((robot[0]+i*dr, cc1, "[", cc2, "]"))
                        elif wh2[robot[0]+i*dr][cc1] == "]" and wh2[robot[0]+i*dr][cc2] == ".":
                            seen.append((robot[0]+i*dr, cc1-1, "[", cc1, "]"))
                        elif wh2[robot[0]+i*dr][cc1] == "." and wh2[robot[0]+i*dr][cc2] == "[":
                            seen.append((robot[0]+i*dr, cc2, "[", cc2+1, "]"))
                        elif wh2[robot[0]+i*dr][cc1] == "]" and wh2[robot[0]+i*dr][cc2] == "[":
                            seen.append((robot[0]+i*dr, cc1-1, "[", cc1, "]"))
                            seen.append((robot[0]+i*dr, cc2, "[", cc2+1, "]"))
                    if free:
                        break
                i += 1

        """
        #print(f"Move {move}: (on stop {stop})")
        box1 = 0
        box2 = 0
        for l in wh2:
            box1 += "".join(l).count("[")
            box2 += "".join(l).count("]")
            #if stop == 873:
            #    print("".join(l))
        if stop == 1:
            print(box1,box2,"\n")
        if box1 < 582 or box2 < 582:
            print(stop)
            print(robot)
            break
        #keyboard.wait("p")

    for l in wh2:
        print("".join(l))
        """

    result = 0
    for r, row in enumerate(wh2):
        for c, el in enumerate(row):
            if el == "[":
                result += r*100 + c
    return result

start = time.time()
print("Task 2 result:", task2(), f"(time: {(time.time()-start)*10**3:.03f}ms)")
