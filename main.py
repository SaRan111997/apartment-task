blocks=[
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": True,
"school": False,
"store": False,
},
{
"gym": True,
"school": True,
"store": False,
},
{
"gym": False,
"school": True,
"store": False,
},
{
"gym": False,
"school": False,
"store": False,
}]

reqs=["gym","school","store"]


def apartmentHunting(blocks, reqs):
    optimal_index = 0
    max_distance = 0
    # print(optimal_index)
    for i, block in enumerate(blocks):
        # print(block)
        distance = 0
        for req in reqs:
            # print(block[req])
            if not block[req]:
                distance += 1
        # print(distance)
        if distance > max_distance:
            max_distance = distance
            optimal_index = i
    result = ''' is the farthest you'd have to walk to reach a gym, a school, or a store is ''' + str(optimal_index) + ''' block; at any other index, you'd have to walk farther'''
    return 'index -> '+str(optimal_index) + result

print(apartmentHunting(blocks, reqs))