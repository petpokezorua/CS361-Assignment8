import time

artifactList = []
with open("./stats.txt", "r", encoding = "utf-8-sig") as statFile:
    for artifact in statFile:
        artifactList.append(artifact)
    
def rollDistribution(artifact): 
    obj = artifact.split(',')                                                       # Now, the stats will be at index 1, 3, 5, 7
    statIndex = [1, 3, 5, 7]                                                        # And it's value will be at index 2, 4, 6, 8
    statValIndex = [2, 4, 6, 8]
    statList = ["HP", "HP%", "DEF", "DEF%", "ATK", "ATK%", "EM", "ER", "CR", "CD"]
    statName = ""
    statValue = 0
    rollCount = 0
    for i in range(4):
        statName = obj[statIndex[i]]
        statValue = float(obj[statValIndex[i]])
        rollCount = rollCount + (statValue / maxRollValue((statName)))
    return "Roll for this artifact: " + str(rollCount) + " / 9.0"
    
    
def maxRollValue(stat):
    if stat == "HP":
        return 298.75
    if stat == "HP%":
        return 5.83
    if stat == "DEF":
        return 23.15
    if stat == "DEF%":
        return 7.29
    if stat == "ATK":
        return 19.45
    if stat == "ATK%":
        return 5.83
    if stat == "EM":
        return 23.31
    if stat == "ER":
        return 6.48
    if stat == "CR":
        return 3.89
    if stat == "CD":
        return 7.77
    
    
    
    
while True:
    time.sleep(1)
    with open("./request.txt", "r") as request:
        artifactChoice = request.read()
        chosenArtifact = []
        output = ""
        
        if (artifactChoice == ""):          # Placeholder
            output == "Still waiting for an input..."
            with open("./request.txt", "w") as request:
                request.write(output)
            time.sleep(3)
        elif (artifactChoice != ""):
            choice = int(artifactChoice)
            if (choice > len(artifactList) - 1):
                output = ("Error: We only have " + str(len(artifactList) - 1) + " artifacts currently available.")
                with open("./request.txt", "w") as request:
                    request.write(output)
                    break
            else:
                chosenArtifact = artifactList[choice]
                output = rollDistribution(chosenArtifact)
                with open("./request.txt", "w") as request:
                    request.write(output)
                break
                