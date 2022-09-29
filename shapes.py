import arcade

arcade.open_window(1200,900, "lost of shapes")
arcade.set_background_color(arcade.color.BABY_PINK)

arcade.start_render()
#draw 1
arcade.draw_line_strip([(20,30),(200,30),(200,300),(20,40)], arcade.color.AERO_BLUE)
arcade.draw_lrtb_rectangle_filled(320,420,300,50, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_outline(450,550,300,50, arcade.color.AFRICAN_VIOLET, 12)
arcade.draw_xywh_rectangle_filled(600, 200, 300, 80, arcade.color.ALMOND)
arcade.draw_xywh_rectangle_outline(10, 10, 900, 300, arcade.color.BLACK)
arcade.draw_circle_filled(150,600,75, arcade.color.ANTIQUE_FUCHSIA)
arcade.draw_circle_outline(150,600,155, arcade.color.GRAY,5)
arcade.draw_triangle_filled(960,230,1030,230,450,350, arcade.color.APPLE_GREEN)
arcade.draw_triangle_outline(600,600,490,300,700,700, arcade.color.YELLOW_ROSE, 8 )
arcade.draw_arc_filled()

arcade.finish_render()

arcade.run()
