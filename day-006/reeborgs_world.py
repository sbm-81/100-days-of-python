# As all the code is for specific environment called reeborg's world, so i just comment out the code for each hurdle and project, so that it will be easier to read and understand.

#HURDLE 1
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    
# def unique_movement():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# unique_movement()
# unique_movement()
# unique_movement()
# unique_movement()
# unique_movement()
# unique_movement()




#HURDLE 2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    
# def unique_movement():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while not at_goal():
#     unique_movement()



#HURDLE 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    
# def unique_movement():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         unique_movement()


#HURDLE 4

# i was not noticed the function wall_on_right() already defined in the reeborg's world, so i just do it manually in a noob way by myself. ha ha ha
# reeborg's hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def unique_movement():
#     turn_left()        
#     move()
#     turn_right()
#     while wall_in_front():
#         turn_left()
#         move()
#         turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()
    
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         unique_movement()
        


# THis is the cleaner solution of the same problem HURDLE4 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    

# def jump():
#     turn_left()        
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()






#PROJECT: MAZE
# That was awesome, i solve each corner case one by one , then finally landed to solution alhamdulillah

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     while not wall_on_right():
#         turn_right()
#         if not wall_on_right() and not wall_in_front():
#             move()
#     if wall_on_right() and wall_in_front():
#         turn_left()
#     elif wall_on_right() and not wall_in_front():
#         move()

    
