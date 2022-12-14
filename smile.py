import arcade

arcade.open_window(800,800, "smily face ")
arcade.set_background_color(arcade.color.DEEP_CARMINE)

arcade.start_render()
arcade.draw_circle_filled(400,400,200, arcade.color.COPPER)
arcade.draw_xywh_rectangle_filled(200,580,400,50, arcade.color.AO)
arcade.draw_xywh_rectangle_filled(300,630,200,80, arcade.color.BLUE)
arcade.draw_arc_filled(325,400,100,150, arcade.color.YELLOW, 0, 180)
arcade.draw_arc_filled(475,400, 100, 150, arcade.color.YELLOW, 0, 180)
arcade.draw_triangle_filled(350,350,450, 350, 400, 400, arcade.color.YELLOW)
arcade.draw_arc_outline(400, 300 , 200, 100, arcade.color.YELLOW, -180,0,  15)

arcade.finish_render()


arcade.run()


