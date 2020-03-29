from tkinter import *
import a_star_logic as logicBoard

root = Tk()
screen = Canvas(root, width=800, height=700, background="#222",highlightthickness=0)
screen.pack()



class gui:
    def __init__(self):
        """
        Creates a new board
        """
        self.new_board()
        self.start_node_bool = True
        self.end_node_bool = True
        self.index_node =[]

    def new_board(self):
        """
        Creates the board_lines for the canvas
        :return:
        """
        # Horizontal Line
        for i in range(0,17):
            screen.create_line(200, 150+i*25,600, 150+i*25,fill = "red")

        for j in range(0,17):
            screen.create_line(200+j*25,150,200+j*25,550,fill = "red")


        self.initial_text =screen.create_text(400, 620, fill ="white", text= " Click on two places, start and end respectively. \n Once down you can draw barriers.")
        screen.update()

    def remove_initial_text(self):
        """
        Removes the text when start and end node have been placed
        """
        #screen.delete(self.initial_text)
        screen.itemconfig(self.initial_text,text = "Press q to quit, C to clear or S to start !")


    def draw_start_end_nodes(self,x_val,y_val):
        """
        Draws the nodes
        :param x_val:
        :param y_val:
        :return:
        """
        if x_val>15 or x_val<0 or y_val>15 or y_val <0:
            return

        if self.start_node_bool:
            #screen.create_rectangle(200, 150, 225, 200,                                    fill="White")
            screen.create_rectangle(200+(x_val*25),150+(y_val*25),225+(x_val*25),175+(y_val*25), fill ="White")
            self.start_node_bool = False
            self.index_node += [(x_val,y_val)]

            board.insert_Nodes(x_val, y_val, 1)




        elif self.end_node_bool:
            ## Cannot override existing start Node
            if (x_val, y_val) not in self.index_node:
                screen.create_rectangle(200 + (x_val * 25), 150 + (y_val * 25), 225 + (x_val * 25), 175 + (y_val * 25),
                                        fill="red")
                self.end_node_bool = False
                self.index_node += [(x_val, y_val)]
                board.insert_Nodes(x_val, y_val, 2)






        else:
            if (x_val,y_val) not in self.index_node:
                screen.create_rectangle(200 + (x_val * 25), 150 + (y_val * 25), 225 + (x_val * 25), 175 + (y_val * 25),
                                        fill="blue")


            board.insert_Nodes(x_val, y_val, 0)
            return

        if not interface.end_node_bool and not interface.start_node_bool:
            interface.remove_initial_text()
    def clear_board(self,):
        screen.delete("all")
        self.new_board()
        self.start_node_bool = True
        self.end_node_bool = True
        self.index_node = []




    def insert_path(self,x_val,y_val,colour):
        screen.create_rectangle(200 + (x_val * 25), 150 + (y_val * 25), 225 + (x_val * 25), 175 + (y_val * 25),
                                fill=colour)


def left_click(event):

    pos_x = event.x
    pos_y = event.y


    rounded_x = (int((pos_x - 200) / 25))
    rounded_y = (int((pos_y - 150) / 25))

    interface.draw_start_end_nodes(rounded_x, rounded_y)




    #print(rounded_x,rounded_y)
    pass
def hold_left_click(event):
    pos_x = event.x
    pos_y = event.y


    rounded_x = (int((pos_x - 200) / 25))
    rounded_y = (int((pos_y - 150) / 25))
    interface.test(rounded_x,rounded_y)

def clear1(event):
    global board
    interface.clear_board()
    board = logicBoard.Logic_AStar_Algo()


# Will remove later
def print_clear(event):
    board.print_neat()



def start_Astar_Algo(event):
    x=board.pathFinding(interface)
    # pop first element and second element
    try:
        x.pop(0)
        x.pop(-1)
    except:
        pass
    for valid_pos in x:
        interface.insert_path(valid_pos[1],valid_pos[0],"orange")


if __name__ == "__main__":
    global board
    board = logicBoard.Logic_AStar_Algo()

    interface = gui()
    # Bind the left click
    screen.bind("<Button-1>", left_click)
    screen.bind('<B1-Motion>', left_click)
    #Make a focus set so users have acces to key with canvas
    screen.focus_set()
    screen.bind("c", clear1)
    screen.bind("p", print_clear)
    screen.bind("s",start_Astar_Algo)


    root.mainloop()
