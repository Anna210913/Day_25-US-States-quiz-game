import turtle
import pandas


screen =turtle.Screen()
screen.title("U.S States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

"""this code below is to help us find the x and y position of each state that we click on with our mouse. We don't need
 this for this challenge because DR did the hard work for us (50 states.csv)"""
#def get_mouse_click_coor(x,y):
#    print(x,y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]


while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States Correct",
                                    prompt="Name a state:").title()
    print(answer_state)

    #check to see if answer_state in one of the states in all the states of the 50_states.csv
    if answer_state=="Exit":
        """this line of code below shows how we can combine code in one line using conditional list comprehension"""
        missing_states =[state for state in all_states if state not in guessed_states]

        """the code hashed out below is the long alternative without list comprehension"""
        #missing_states =[]
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


#states_to_learn






screen.exitonclick()