'''
node -> cost
node -> node 
 find least cost
 
 (0).children = [5, 3, 6]
 (5).parent = 0
'''
def get_cheapest_cost(rootNode):
  children  = rootNode.children # :(

  if children == []: 
    return rootNode.cost
  
  else:
    min_cost = float('inf')
    for child in children:
      cost = get_cheapest_cost(child)
      if cost < min_cost:
        min_cost = cost
      
  return min_cost + rootNode.cost


########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None


def setup_example():
  root = Node(0)
  
  root.children = [Node(5), Node(3), Node(6)]
  root.children[0].children = [Node(4)]
  root.children[1].children = [Node(2), Node(0)]
  root.children[1].children[0].children = [Node(1)]
  root.children[1].children[0].children[0].children = [Node(1)]
  root.children[1].children[1].children = [ Node(10)]
  root.children[2].children = [Node(1), Node(5)]
  
  return root

if __name__ == "__main__":
  root = setup_example()
    
  print(get_cheapest_cost(root) == 7)
   