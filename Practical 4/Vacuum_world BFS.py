class Node:
  def __init__(self, vacuum=None, dirt=None, parent=None, prev_action=None):
    # String vacuum = "left" / "right"
    self.vacuum = vacuum
    # List dirt = ["left", "right"] / ["left"] / ["right"], [ ]
    self.dirt = dirt

    self.parent = parent

    self.prev_action = prev_action

def expandAndReturnChildren(node):
  children = []
  # try going left
  if node.vacuum == "right":
    children.append(Node("left", node.dirt, node, "left"))
  
  # try going right
  if node.vacuum == "left":
    children.append(Node("right", node.dirt, node, "right"))

  # try suck
  if node.vacuum in node.dirt:
    children.append(Node(node.vacuum, list(set(node.dirt) - set([node.vacuum])), node, "suck"))

  return children

def bfs(initial_state):
  frontier = []
  explored = []
  goalie = Node()
  solution = []
  # add initial state to frontier
  frontier.append(Node(initial_state[0], initial_state[1], None, "Initial State"))
  
  # empty list returns False
  while frontier[0].dirt:
    # expand the first in the frontier
    children = expandAndReturnChildren(frontier[0])
    # add to the explored list
    explored.append(frontier[0])
    # remove the expanded frontier
    del frontier[0]
    # add children to the frontier
    for child in children:
      # check if a node was expanded or generated previously
      if not ([child.vacuum, child.dirt] in [[e.vacuum, e.dirt] for e in explored] or [child.vacuum, child.dirt] in [[f.vacuum, f.dirt] for f in frontier]):
        frontier.append(child)
    print("Explored:", [[e.vacuum, e.dirt] for e in explored])
    print("Frontier:", [[f.vacuum, f.dirt] for f in frontier])
    print("Children:", [[c.vacuum, c.dirt] for c in children])
    print("")
  
  # frontier[0] is a goal state
  goalie = frontier[0]
  solution = [[goalie.vacuum, goalie.dirt]]
  moves = [goalie.prev_action]
  while goalie.parent is not None:
    solution.insert(0, [goalie.parent.vacuum, goalie.parent.dirt])
    moves.insert(0, goalie.parent.prev_action)
    for e in explored:
      if [e.vacuum, e.dirt] == [goalie.parent.vacuum, goalie.parent.dirt]:
        goalie = e
        break
  return solution, moves
  
if __name__ == '__main__':
  initial_state = ["left", ["left", "right"]]
  
  solution, moves = bfs(initial_state)
  print("Solution:", solution)
  print("Moves:", moves)