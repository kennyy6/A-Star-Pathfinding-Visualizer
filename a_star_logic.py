class Node:
    def __init__(self, parent = None,position = None):
        """
        Nodes that have been checked
        """
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0


class Logic_AStar_Algo:

    def __init__(self):
        """
        Makes a new List of List that  is act as a board
        """
        self.val_list = []
        for i in range(16):
            a_list = []
            for j in range(16):
                a_list +=[0]
            #print(a_list)
            self.val_list += [a_list]

    def print_neat(self):
        """
        Prints out the board as a console
        :return:
        """
        for i in self.val_list:
            print(i)
        return None
    def insert_Nodes(self,x,y,mode):
        """
        Mode: 3 = Barriers, 1= Start , 2= End
        :param x:
        :param y:
        :param mode:
        :return:
        """
        if mode == 1:
            self.val_list[y][x] = 1 # 1 Represents start
            self.start_node = Node(None,(y,x))
        elif mode == 2:
            #print(x,y)
            self.val_list[y][x] = 2
            self.end_node = Node(None, (y, x))
        else:
            self.val_list[y][x] = 3

    def pathFinding(self,gui_reference):
        """
        Utlizes the A* pathfinding algorithm
        :param gui_reference: Reference to the gui so we can place the nodes in the canvas
        :return:
        """
        # Using gui reference here so we can map out the calculations it performs


        #Intialize open and closed list
        open_list = []
        close_list = []

        open_list.append(self.start_node)
        #Aslong as the open_list is greater than zero
        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            # Finds the smallest f value within the open_list and moves it into  close list
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)

            close_list.append(current_node)

            if current_node.position == self.end_node.position:
                path  = []
                while current_node is not None:
                    path.append(current_node.position)
                    current_node = current_node.parent


                gui_reference.insert_path(self.start_node.position[1],self.start_node.position[0],"white")
                gui_reference.insert_path(self.end_node.position[1],self.end_node.position[0],"red")


                return path[::-1]  # Return reversed path

            #Neightbours of current node
            neighbours = []
            for i in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                #each node position
                node_neighbout_index = (current_node.position[0]+i[0], current_node.position[1] + i[1])

                # see if its valid
                if node_neighbout_index[0] > 15 or node_neighbout_index[0] < 0 or node_neighbout_index[1] > 15 or node_neighbout_index[1] < 0:
                    continue
                # if the value and the index = 3 it means that its not a valid move
                if self.val_list[node_neighbout_index[0]][node_neighbout_index[1]] == 3:
                    continue

                # Create new node
                new_node = Node(current_node, node_neighbout_index)

                # Append
                neighbours.append(new_node)

            # see if neighbouts exist either in open list or close list
            for neighbour in neighbours:
                cancel_below_line = False


                # colour in the selected neighbours it searching
                gui_reference.insert_path(neighbour.position[1],neighbour.position[0],"green")

                for close_neighbours in close_list:
                    if neighbour.position == close_neighbours.position:
                        cancel_below_line = True
                        break
                if not cancel_below_line:
                    # create f,g,h
                    neighbour.g = neighbour.parent.g + 1  # since we are next to it
                    neighbour.h = ((neighbour.position[0] - self.end_node.position[0]) ** 2 + (
                                neighbour.position[1] - self.end_node.position[1]) ** 2)
                    neighbour.f = neighbour.h + neighbour.g
                    # Child is already in the open list
                    for open_node in open_list:
                        if neighbour.position == open_node.position and neighbour.g > open_node.g:
                            #continue
                            break
                    # Add the child to the open list
                    open_list.append(neighbour)




        pass


if __name__ == "__main__":
    test = Logic_AStar_Algo()
    test.print_neat()