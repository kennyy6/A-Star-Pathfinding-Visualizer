from tkinter import *

root = Tk()
screen = Canvas(root, width=800, height=700, background="#222",highlightthickness=0)
screen.pack()

class gui:
    def __init__(self):
        """
        Creates a new board
        """
        self.new_board()
        self.start_node = True
        self.end_node = True

    def new_board(self):
        # Horizontal Line

        screen.create_line(200, 150, 600, 150, fill="red")
        screen.create_line(200, 200, 600, 200, fill="red")
        screen.create_line(200, 250, 600, 250, fill="red")
        screen.create_line(200, 300, 600, 300, fill="red")
        screen.create_line(200, 350, 600, 350, fill="red")
        screen.create_line(200, 400, 600, 400, fill="red")
        screen.create_line(200, 450, 600, 450, fill="red")
        screen.create_line(200, 500, 600, 500, fill="red")
        screen.create_line(200, 550, 600, 550, fill="red")

        # Vertical Line

        screen.create_line(200, 150, 200, 550, fill="red")
        screen.create_line(250, 150, 250, 550, fill="red")
        screen.create_line(300, 150, 300, 550, fill="red")
        screen.create_line(350, 150, 350, 550, fill="red")
        screen.create_line(400, 150, 400, 550, fill="red")
        screen.create_line(450, 150, 450, 550, fill="red")
        screen.create_line(500, 150, 500, 550, fill="red")
        screen.create_line(550, 150, 550, 550, fill="red")
        screen.create_line(600, 150, 600, 550, fill="red")

        # new Addition Vertival
        screen.create_line(225, 150, 225, 550, fill="red")
        screen.create_line(275, 150, 275, 550, fill="red")
        screen.create_line(325, 150, 325, 550, fill="red")
        screen.create_line(375, 150, 375, 550, fill="red")
        screen.create_line(425, 150, 425, 550, fill="red")
        screen.create_line(475, 150, 475, 550, fill="red")
        screen.create_line(525, 150, 525, 550, fill="red")
        screen.create_line(575, 150, 575, 550, fill="red")

        screen.create_line(200, 175, 600, 175, fill="red")
        screen.create_line(200, 225, 600, 225, fill="red")
        screen.create_line(200, 275, 600, 275, fill="red")
        screen.create_line(200, 325, 600, 325, fill="red")
        screen.create_line(200, 375, 600, 375, fill="red")
        screen.create_line(200, 425, 600, 425, fill="red")
        screen.create_line(200, 475, 600, 475, fill="red")
        screen.create_line(200, 525, 600, 525, fill="red")

        self.initial_text =screen.create_text(400, 620, fill ="white", text= " Click on two places, start and end respectively.")
        screen.update()

    def remove_initial_text(self):
        #screen.delete(self.initial_text)
        screen.itemconfig(self.initial_text,text = "Press q to quit, C to clear or S to start !")


    def draw_start_end_nodes(self,x_val,y_val):
        if x_val>15 or x_val<0 or y_val>15 or y_val <0:
            return

        if self.start_node:
            print("test2")
            #screen.create_rectangle(200, 150, 225, 200,                                    fill="White")
            screen.create_rectangle(200+(x_val*25),150+(y_val*25),225+(x_val*25),175+(y_val*25), fill ="White")
            self.start_node = False

        elif self.end_node:
            screen.create_rectangle(200 + (x_val * 25), 150 + (y_val * 25), 225 + (x_val * 25), 175 + (y_val * 25),
                                    fill="red")
            self.end_node = False
        else:
            screen.create_rectangle(200 + (x_val * 25), 150 + (y_val * 25), 225 + (x_val * 25), 175 + (y_val * 25),
                                    fill="blue")
            return

        if not interface.end_node and not interface.start_node:
            interface.remove_initial_text()
    def clear_board(self,):
        screen.delete("all")
        self.new_board()
        self.start_node = True
        self.end_node = True

    # def test(self,x,y):
    #     print(x>15 or x<15 or y>15 or y <15)
    #     if x>15 or x<0 or y>15 or y <0:
    #         return
    #
    #     screen.create_rectangle(200 + (x* 25), 150 + (y * 25), 225 + (x * 25), 175 + (y * 25),
    #                             fill="blue")



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
    print(rounded_x, rounded_y)
def clear1(event):
    print("test")
    interface.clear_board()

if __name__ == "__main__":

    interface = gui()
    # Bind the left click
    screen.bind("<Button-1>", left_click)
    screen.bind('<B1-Motion>', left_click)
    #Make a focus set so users have acces to key with canvas
    screen.focus_set()
    screen.bind("c", clear1)


    root.mainloop()
