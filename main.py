
blocks = [
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
"school": True,
"store": True,
}
]
reqs = ["gym", "school", "store"]

def find_optimal_block(blocks, reqs):
  # Initialize the minimum distance to be the maximum possible distance
  min_distance = len(blocks)
  # print(min_distance)
  # Initialize the optimal block index to be -1
  optimal_block_index = -1

  # Iterate through each block
  for i, block in enumerate(blocks):
    # Initialize the distance to 0
    # print(i,block)
    distance = 0
    # Iterate through each requirement
    for req in reqs:
      # print(block[req])
      # If the requirement is not in the block, increment the distance
      if not block[req]:
        # print(block[req])
        distance += 1
    # If the distance is smaller than the current minimum distance, update the minimum distance and the optimal block index
    if distance < min_distance:
      min_distance = distance
      optimal_block_index = i

  # Return the optimal block index
  return optimal_block_index
optimal_block_index = find_optimal_block(blocks, reqs)

print(optimal_block_index)
