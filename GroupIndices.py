# Group elements of 2+ data structures according to indicies
# Will initially have 2+ lists inside a list. Create 2 new lists, store elements of both at index 0 and 1

datalists = [[10, 20, 30], [40,50,60], [70,80,90]]
groupedlists = []
index = 0

for i in range(len(datalists[0])):
    groupedlists.append([])
    for j in range(len(datalists)):
        groupedlists[index].append(datalists[j][index])
    index = index + 1

a, b, c = groupedlists[0], groupedlists[1], groupedlists[2]
print(a, b, c)
print(groupedlists)
