import arcade
#use this to open the window, width 800, Heigh 600
my_window = arcade.open_window(720,600, "First window Demo")
arcade.set_background_color(arcade.color.BLUEBERRY)

arcade.start_render()
for xloc in range(50, 1000, 80):
    arcade.draw_line(xloc, 50, xloc , 800, arcade.color.BLACK, 5)
for yloc in range(50,900, 80):
    arcade.draw_line(50, yloc, 1000, yloc, arcade.color.AMERICAN_ROSE)
#all of your other drawing goes here

arcade.finish_render()
#you need this to actually see the windown
arcade.run()



