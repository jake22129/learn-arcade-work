"""
It's snowing!
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_the_water():
    """ Draw the water for the boats"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.NAVY_BLUE)


def draw_boat(x, y):
    """ Draw the boats on the ocean"""

    # Base of the boat
    arcade.draw_arc_filled(x, y + 50, 300, 100, arcade.color.BOLE, 180, 360)

    # Boat details (staff)
    arcade.draw_rectangle_filled(x, y + 50, 10, 100, arcade.color.BOLE)
    arcade.draw_rectangle_filled(x - 20, y + 50, 10, 50, arcade.color.BOLE)
    arcade.draw_rectangle_filled(x + 20, y + 50, 10, 50, arcade.color.BOLE)


def draw_cloud (x, y):
    """ Draw the clouds in the sky"""

    # Draw left and right sides of the cloud
    arcade.draw_ellipse_filled(x + 50, y + 300, 100, 50, arcade.color.GHOST_WHITE)
    arcade.draw_ellipse_filled(x - 50, y + 300, 100, 50, arcade.color.GHOST_WHITE)

    # Draw up and down sides of the cloud
    arcade.draw_ellipse_filled(x, y + 325, 100, 50, arcade.color.GHOST_WHITE)
    arcade.draw_ellipse_filled(x, y + 275, 100, 50, arcade.color.GHOST_WHITE)


def draw_fish(x, y):
    """ Draw the fish in the ocean"""

    # Draw the body of the fish
    arcade.draw_arc_filled(x, y, 50, 30, arcade.color.YELLOW, 0, 180)
    arcade.draw_arc_filled(x, y, 50, 30, arcade.color.YELLOW, 180, 360)

    # Draw the tail of the fish
    arcade.draw_triangle_filled(x - 40, y + 20, x, y, x - 40, y - 20, arcade.color.YELLOW)


def main():
    """ Draw everything """
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "It's snowing!")
    arcade.set_background_color(arcade.color.PURPLE_NAVY)
    arcade.start_render()

    draw_the_water()
    draw_boat(180, 200)
    draw_boat(550, 200)

    draw_cloud(210, 200)
    draw_cloud(580, 200)

    draw_fish(90, 100)
    draw_fish(350, 100)
    draw_fish(550, 120)
    draw_fish(720, 80)


    # Draw the snowflakes
    arcade.draw_circle_filled(50, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(100, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(150, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(200, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(250, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(300, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(350, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(400, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(450, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(500, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(550, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(600, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(650, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(700, 350, 10, arcade.color.GHOST_WHITE, num_segments= 32)
    arcade.draw_circle_filled(750, 400, 10, arcade.color.GHOST_WHITE, num_segments= 32)

    # Draw ice floating in ocean water
    arcade.draw_rectangle_filled(100, 150, 150, 50, arcade.color.GHOST_WHITE)
    arcade.draw_rectangle_filled(400, 150, 150, 50, arcade.color.GHOST_WHITE)
    arcade.draw_rectangle_filled(700, 150, 150, 50, arcade.color.GHOST_WHITE)
    arcade.draw_rectangle_filled(250, 50, 150, 50, arcade.color.GHOST_WHITE)
    arcade.draw_rectangle_filled(550, 50, 150, 50, arcade.color.GHOST_WHITE)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started
main()