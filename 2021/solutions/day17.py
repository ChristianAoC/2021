def step(values, hits):
  values["x"] += values["xv"]
  values["y"] += values["yv"]
  if values["xv"] > 0:
    values["xv"] -= 1
  elif values["xv"] < 0:
    values["xv"] += 1
  values["yv"] -= 1
  hits.append([values["x"],values["y"]])
  if values["x"]>=values["txmin"] and values["x"]<=values["txmax"] and values["y"]<=values["tymax"] and values["y"]>=values["tymin"]:
    global hit
    hit[str(values["initxv"])+","+str(values["inityv"])] = "1"
    for pair in hits:
      global ymax
      if pair[1] > ymax:
        ymax = pair[1]
  elif values["y"]>=values["tymin"] and values["x"]<=values["txmax"]:
    step(values, hits)    

ymax = -100
hit = {}

for x in range(400):
  for y in range(-200,200):
    values = {
#      "txmin": 20,
#      "txmax": 30,
#      "tymin": -10,
#      "tymax": -5,
      "txmin": 257,
      "txmax": 286,
      "tymin": -101,
      "tymax": -57,
      "x": 0,
      "y": 0,
      "xv": x,
      "yv": y,
      "initxv": x,
      "inityv": y
    }
    hits = []
    step(values, hits)
print(f"Task 1: {ymax}")
print("Task 2: "+str(len(hit)))
