"""
This is my house
"""

import arcade

arcade.open_window(800, 600, "My house")

# Set background color
arcade.set_background_color(arcade.color.SKY_BLUE)

# Ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.AO)

# Draw the base of my house
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 100, arcade.color.ALABAMA_CRIMSON)

# Draw the roof of my house
arcade.draw_triangle_filled(10, 350, 190, 500, 370, 350, arcade.color.ALABAMA_CRIMSON)

# Draw my front door
arcade.draw_lrtb_rectangle_filled(80, 120, 180, 100, arcade.color.GHOST_WHITE)

# Draw the window of my front door
arcade.draw_circle_filled(100, 160, 12, arcade.color.ASH_GREY)

# Draw bedroom windows
arcade.draw_rectangle_filled(290, 300, 60, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(290, 300, 50, 40, arcade.color.ASH_GREY)
arcade.draw_rectangle_filled(190, 300, 60, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(190, 300, 50, 40, arcade.color.ASH_GREY)

# Draw garage door
arcade.draw_lrtb_rectangle_filled(160, 320, 250, 100, arcade.color.GHOST_WHITE)

# Draw driveway
arcade.draw_rectangle_filled(190, 49, 310, 100, arcade.color.COOL_GREY)

# Draw flag pole
arcade.draw_rectangle_filled(600, 200, 15, 200, arcade.color.SILVER)
arcade.draw_circle_filled(600, 305, 10, arcade.color.GOLD)

# Draw flag
arcade.draw_rectangle_filled(700, 290, 190, 10, arcade.color.RED)
arcade.draw_rectangle_filled(700, 280, 190, 10, arcade.color.GHOST_WHITE)
arcade.draw_rectangle_filled(700, 270, 190, 10, arcade.color.RED)
arcade.draw_rectangle_filled(700, 260, 190, 10, arcade.color.GHOST_WHITE)
arcade.draw_rectangle_filled(700, 250, 190, 10, arcade.color.RED)
arcade.draw_rectangle_filled(700, 240, 190, 10, arcade.color.GHOST_WHITE)
arcade.draw_rectangle_filled(700, 230, 190, 10, arcade.color.RED)
arcade.draw_rectangle_filled(700, 220, 190, 10, arcade.color.GHOST_WHITE)
arcade.draw_rectangle_filled(700, 210, 190, 10, arcade.color.RED)
arcade.draw_rectangle_filled(640, 270, 70, 50, arcade.color.BLUE)

# Draw front yard tree
arcade.draw_rectangle_filled(475, 150, 40, 100, arcade.color.BROWN_NOSE)
arcade.draw_arc_filled(475, 200, 150, 300, arcade.color.DARK_GREEN, 0, 180)

# Draw a big cloud in the sky
arcade.draw_ellipse_filled(350, 520, 220, 100, arcade.color.GHOST_WHITE)
arcade.draw_ellipse_filled(500, 520, 220, 100, arcade.color.GHOST_WHITE)

# Draw a text at (310, 430) with a font size of 26 pts.)
arcade.draw_text("Welcome to Sheeder Farms", 310, 430, arcade.color.BLACK, 26)

# Finished drawing
arcade.finish_render()

arcade.run()
