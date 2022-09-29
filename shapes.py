import arcade

arcade.open_window(1200,900, "lost of shapes")
arcade.set_background_color(arcade.color.BABY_PINK)

arcade.start_render()
#draw 1
arcade.draw_line_strip([(20,30),(200,30),(200,300),(20,40)], arcade.color.AERO_BLUE)
#draw 2
arcade.draw_lrtb_rectangle_filled(320,420,300,50, arcade.color.BLUE)
#draw 3
arcade.draw_lrtb_rectangle_outline(450,550,300,50, arcade.color.AFRICAN_VIOLET, 12)
#draw 4
arcade.draw_xywh_rectangle_filled(600, 200, 300, 80, arcade.color.ALMOND)

arcade.finish_render()

arcade.run()
