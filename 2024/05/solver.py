""" Advent of Code solver class """
with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = [line.strip() for line in file_handle]
    rules = []
    pages = []
    for line in inp:
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            pages.append(line)

errlist = []

def task1():
    """ Task 1 solver """
    result = 0
    for rule in rules:
        for i, page in enumerate(pages):
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    errlist.append(pages.pop(i))
    for page in pages:
        pagelist = page.split(",")
        result += int(pagelist[int((len(pagelist)-1)/2)])
    return result

print("Task 1:", task1())

def task2():
    """ Task 2 solver """
    result = 0
    allall = list(set([r[0] for r in rules]+[r[1] for r in rules]))

    pagelist = [page.split(",") for page in errlist]
    for page in pagelist:
        onerule = []
        rules2 = []
        all = []
        for a in allall:
            if a in page:
                all.append(a)
        for rule in rules:
            if rule[0] in page and rule[1] in page:
                rules2.append(rule)

        while len(all) > 0:
            left = [r[0] for r in rules2]
            for i, candidate in enumerate(all):
                candidate = all[i]
                if candidate not in left:
                    all.pop(i)
                    onerule.insert(0, candidate)
                    for j in range(len(rules2)-1, -1, -1):
                        if rules2[j][1] == candidate:
                            rules2.pop(j)

        mapping = dict()
        i = 0
        for r in onerule:
            mapping[r] = i
            i += 1
        
        plsorted= sorted(page, key=lambda x: mapping[x])
        result += int(plsorted[int((len(plsorted)-1)/2)])
    return result

print("Task 2:", task2())
