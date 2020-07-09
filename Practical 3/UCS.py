class Node:
  def __init__(self, state=None, parent=None, total_cost_to_node=None):
    self.state = state
    self.parent = parent
    self.total_cost_to_node = total_cost_to_node

def expandAndReturnChildren(state_space, node):
  children = []
  for [m,n,c] in state_space:
    if m == node.state:
      children.append(Node(n, node.state, node.total_cost_to_node+c))
    elif n == node.state:
      children.append(Node(m, node.state, node.total_cost_to_node+c))
  return children

def ucs(state_space, initial_state, goal_state):
  frontier = []
  explored = []
  goalie = Node()
  solution = []
  # add initial state to frontier
  frontier.append(Node(initial_state, None, 0))
  
  while True:
    # order frontier by cost
    frontier.sort(key=lambda x : x.total_cost_to_node)
    # goal test
    if frontier[0].state == goal_state:
      goalie = frontier[0]
      break

    # expand the first in the frontier
    children = expandAndReturnChildren(state_space, frontier[0])
    
    # remove expanded frontier
    explored.append(frontier[0])
    del frontier[0]

    # add children to the frontier
    for child in children:
      # check if node already exists in frontier 
      if child.state in [f.state for f in frontier]:
        # compare cost of nodes
        for f in frontier:
          if f.state == child.state:
            if f.total_cost_to_node > child.total_cost_to_node:
              node = f
            else:
              node = child
        frontier.append(child)
        frontier.remove(node)
      else:
        frontier.append(child)
    
    print("Explored:", [e.state for e in explored])
    print("Frontier:", [f.state for f in frontier])
    print("Children:", [c.state for c in children])
    print("")
  
  solution = [goalie.state]
  path_cost = 0
  explored.sort(key=lambda x : x.total_cost_to_node)

  while goalie.parent is not None:
    solution.insert(0, goalie.parent)
    for e in explored:
      if e.state == goalie.parent:
        path_cost += getCost(state_space, e.state, goalie.state)
        goalie = e
        break
  return solution, path_cost
  
def getCost(state_space, state0, state1):
  for [m,n,c] in state_space:
    if [state0,state1] == [m,n] or [state1,state0] == [m,n]:
      return c

if __name__ == '__main__':
    state_space = [
        ['Arad', 'Zerind', 75],
        ['Arad', 'Sibiu', 140],
        ['Arad', 'Timisoara', 118],
        ['Timisoara', 'Lugoj', 111],
        ['Lugoj', 'Mehadia', 70],
        ['Mehadia', 'Drobeta', 75],
        ['Drobeta', 'Craiova', 120],
        ['Craiova', 'Pitesti', 138],
        ['Pitesti', 'Bucharest', 101],
        ['Zerind', 'Oradea', 71],
        ['Oradea', 'Sibiu', 151],
        ['Sibiu', 'Rimnicu Vilcea', 80],
        ['Rimnicu Vilcea', 'Craiova', 146],
        ['Rimnicu Vilcea', 'Pitesti', 97],
        ['Sibiu', 'Fagaras', 99],
        ['Fagaras', 'Bucharest', 211],
        ['Bucharest', 'Giurgiu', 90],
        ['Neamt', 'Iasi', 87],
        ['Iasi', 'Vaslui', 92],
        ['Vaslui', 'Urziceni', 142],
        ['Urziceni', 'Bucharest', 85],
        ['Urziceni', 'Hirsova', 98],
        ['Hirsova', 'Eforie', 86]
        ]
  
    initial_state = 'Arad'
    goal_state = 'Bucharest'
  
    [solution, cost] = ucs(state_space, initial_state, goal_state)
    print("Solution:", solution)
    print("Path Cost:", cost)