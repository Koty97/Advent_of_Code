class Node:
    neighbors = []

    def __init__(self,value, coords):
        self.value=value
        self.coords = coords
    def __str__(self):
        return "{} at {}".format(self.value,self.coords)
    def set_neighbors(self,neighbors):
        self.neighbors=neighbors

file = open("18.input", "r")
sizex=7
sizey=7
board=[[0 for i in range(sizex)] for j in range(sizey)]
bits_to_simulate=12
for i,line in enumerate(file):
    board[int(line.split(",")[1])][int(line.split(",")[0])]=1
    if i==bits_to_simulate-1:
        break

possible_moves=[(0,1),(1,0),(0,-1),(-1,0)]
nodes={}

for i,line in enumerate(board):
    for j,field in enumerate(line):
        neighbors=[]
        for move in possible_moves:
            neighbor_coords=(i+move[0],j+move[1])
            if neighbor_coords[0]>=0 and neighbor_coords[1]>=0:
                try:
                    neighbors.append(Node(board[neighbor_coords[0]][neighbor_coords[1]],neighbor_coords))
                except:
                    pass
        #print("Neighbors of {} at {} are {}".format(board[i][j],(i,j),neighbors))
        n=Node(board[i][j],(i,j))
        n.set_neighbors(neighbors)
        nodes[n.coords]=n
start_pos=(0,0)
end_pos=(7,7)
frontier=[]
visited=[]
bfs=[]
frontier.append(nodes[(start_pos[0],start_pos[1])])
while len(frontier)!=0:
    curr_node=frontier.pop()
    for neighbor in curr_node.neighbors:
        frontier.append(nodes[neighbor.coords])
    visited.append(curr_node)
    bfs.append(curr_node)
    # print("Frontier: {}".format(frontier))
    # print("Visited: {}".format(visited))
    # print("bfs: {}".format(bfs))
    # print()
print()