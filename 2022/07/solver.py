""" Advent of Code solver class """
from pprint import pprint
import sys

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]

def add_dir(name, cur):
    """ add new directory """
    cur.append({ "name": name, "type": "dir", "size": 0, name: [] })
    return cur

def add_file(size, name, cur):
    """ add file of size to dir """
    cur.append({ "name": name, "type": "file", "size": int(size) })
    return cur

def calc_size(cur):
    """ calc directory size """
    for item in cur[cur['name']]:
        if item['type'] == 'file':
            cur['size'] += item['size']
        else:
            folder_size = calc_size(item)
            cur['size'] += folder_size
    return cur['size']

def get_sum(cur, limit=sys.maxsize):
    """ get sum of all dirs with size < limit """
    size = 0
    for item in cur[cur['name']]:
        if item['type'] == 'dir':
            if item['size'] < limit:
                size += item['size']
            size += get_sum(item, limit)
    return size

def find_dir(cur, need, found):
    """ find smallest directory larger than what we need """
    found = found
    for item in cur[cur['name']]:
        if item['type'] == 'dir':
            if item['size'] >= need and item['size'] < found:
                found = find_dir(item, need, item['size'])
            else:
                found = find_dir(item, need, found)
    return found

def solver():
    """ Task 1 solver """
    # initiate file system
    fs = { "name": "/", "type": "dir", "size": 0, "/": [] }
    cur = []
    cur.append(fs['/'])

    # populate file system
    for line in inp:
        #print("Line:", line)
        # command
        if line[0:1] == "$":
            # ls
            if line[2:4] == "ls":
                pass # list dir contents... nothing to do
            # go up a dir
            elif line[2:7] == "cd ..":
                cur.pop()
            # enter dir
            else:
                for contents in cur[-1]:
                    if contents['name'] == line[5:]:
                        cur.append(contents[line[5:]])
        # add subdir
        elif line[0:3] == "dir":
            cur[-1] = add_dir(line[4:], cur[-1])
        # add file
        else:
            cur[-1] = add_file(line.split()[0], line.split()[1], cur[-1])

    calc_size(fs)
    result = get_sum(fs, 100000)

    print("Task 1:", result)

    """ Task 2 solver - today in same method """
    disk = 70000000
    update = 30000000
    need = (disk-update-fs['size'])*-1
    result = find_dir(fs, need, found = sys.maxsize)

    print("Task 2:", result)

solver()