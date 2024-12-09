import time
start_time = time.time()

""" Advent of Code solver class """
with open("input.txt", 'r', encoding='utf8') as file_handle:
    inp = file_handle.readline().strip()
    filelengths = []
    for pos, val in enumerate(inp):
        if pos % 2 == 0:
            filelengths.append(val)

def updatelowestfree(spaces, position):
    if spaces not in lowestfree:
        lowestfree[spaces] = position
    else:
        if lowestfree[spaces] > position:
            lowestfree[spaces] = position

disk = []
freespaces = {}
lowestfree = {}
files = {}
id = 0
for pos, val in enumerate(inp):
    fill = "."
    if pos % 2 == 0:
        fill = id
        files[len(disk)] = [id, int(val)]
        id += 1
    else:
        if int(val) > 0:
            freespaces[len(disk)] = int(val)
            updatelowestfree(int(val), len(disk))
    for _ in range(int(val)):
        disk.append(fill)

# returns the best position for the file and returns that pos
def getbest(space):
    pos = 99999999
    for i in lowestfree:
        if i >= space and lowestfree[i] < pos:
            pos = lowestfree[i]
    return pos

# finds the next lowest spot and updates lowestfree (no return val)
def setnextlowest(val):
    for i in sorted(freespaces.keys()):
        if freespaces[i] == val:
            lowestfree[val] = i
            break

def checksum(disk):
    sum = 0
    for pos, val in enumerate(disk):
        if val == ".":
            continue
        sum += pos * int(val)
    return sum

def defrag(disk):
    defragged = []
    pos = 0
    while pos < len(disk):
        if disk[pos] != ".":
            defragged.append(disk[pos])
        else:
            while disk[-1] == ".":
                disk = disk[:-1]
                if len(disk) == 0:
                    break
            defragged.append(disk[-1])
            disk = disk[:-1]
            if len(disk) == 0:
                break
        pos += 1
    return defragged

def task1():
    """ Task 1 solver """
    disk1 = disk.copy()
    disk1 = defrag(disk1)
    return checksum(disk1)

#print("Task 1:", task1())

def changefilealloc(files):
    newfiles = {}
    for oldpos in reversed(files):
        #if files[oldpos][0] % 100 == 0:
        #    print(files[oldpos])
        newpos = getbest(files[oldpos][1])
        # best position is after current
        if newpos >= oldpos:
            newfiles[oldpos] = files[oldpos]
        # better pos found, move!
        else:
            #print("Move from",oldpos,"to",newpos,"count",files[oldpos][1])
            newfiles[newpos] = files[oldpos]
            # is there space left or does it fit "perfectly"
            spaceleft = freespaces[newpos] - files[oldpos][1]
            if spaceleft > 0:
                freespaces[newpos+files[oldpos][1]] = spaceleft
            # remove old free space entry
            freespaces.pop(newpos)
            # check old position: was there free space after?
            newfreespace = files[oldpos][1]
            afterpos = oldpos+files[oldpos][1]
            if oldpos+files[oldpos][1] in freespaces:
                newfreespace += freespaces[afterpos]
                freespaces.pop(afterpos)
            # check next free space before
            freebefore = oldpos
            while freebefore not in freespaces and freebefore >= 0:
                freebefore -= 1
            if freebefore >= 0:
                # directly before, merge
                if freebefore+freespaces[freebefore] == oldpos:
                    freespaces[freebefore] += newfreespace
                # there's a number in between, so just add new
                freespaces[oldpos] = newfreespace
            # update "best match" indexers
            setnextlowest(files[oldpos][1]+spaceleft)
            if spaceleft != 0:
                setnextlowest(spaceleft)

        # old naive approach - too slow
        # leave for the afterworld i guess!
        """
        newpos = min(freespaces)-9
        unmoved = True
        while newpos < max(freespaces)-1 and newpos < oldpos and unmoved:
            newpos += 1
            if newpos not in freespaces:
                continue
            # found a space for the file
            if freespaces[newpos] >= files[oldpos][1]:
                #print("move",oldpos,"to",newpos,"minfreespaces",min(freespaces),"maxfreespaces",max(freespaces),"loops",max(freespaces)-newpos)
                # move file to new space
                newfiles[newpos] = files[oldpos]
                unmoved = False
                # any space left after the new file location?
                diff = freespaces[newpos] - files[oldpos][1]
                freespaces.pop(newpos)
                if diff > 0:
                    freespaces[newpos+files[oldpos][1]] = diff
                # check old position: was there free space after?
                newfreespace = files[oldpos][1]
                afterpos = oldpos+files[oldpos][1]
                if oldpos+files[oldpos][1] in freespaces:
                    newfreespace += freespaces[afterpos]
                    freespaces.pop(afterpos)
                # check next free space before
                freebefore = oldpos
                while freebefore not in freespaces and freebefore >= 0:
                    freebefore -= 1
                if freebefore >= 0:
                    # directly before, merge
                    if freebefore+freespaces[freebefore] == oldpos:
                        freespaces[freebefore] += newfreespace
                    # there's a number in between, so just add new
                    freespaces[oldpos] = newfreespace
        # didn't move file, keep pos
        if unmoved:
            newfiles[oldpos] = files[oldpos]
        """
    return newfiles

def allocfiles(files):
    newdisk = []
    offset = 0
    while offset < len(disk):
        if offset in files:
            for _ in range(files[offset][1]):
                newdisk.append(files[offset][0])
            offset += files[offset][1]
        else:
            newdisk.append(".")
            offset += 1
    return newdisk

def task2():
    """ Task 2 solver """
    newfiles = changefilealloc(files)
    disk2 = allocfiles(newfiles)
    return checksum(disk2)

print("Task 2:", task2())

print("--- %s seconds ---" % (time.time() - start_time))
