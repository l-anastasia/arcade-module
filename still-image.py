import random

import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Still-image"


def create_screen():
    """Drawing background screen"""
    arcade.draw_rectangle_filled(WINDOW_WIDTH/2,
                                 WINDOW_HEIGHT*2/3,
                                 WINDOW_WIDTH - 1,
                                 WINDOW_HEIGHT*2/3,
                                 arcade.color.SKY_MAGENTA)

    arcade.draw_rectangle_filled(WINDOW_WIDTH/2,
                                 WINDOW_HEIGHT/6,
                                 WINDOW_WIDTH - 1,
                                 WINDOW_HEIGHT/3,
                                 arcade.color.LIGHT_GREEN)


def draw_bird(x, y):
    """Drawing bird"""
    width = 30
    height = 30
    arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, 90, 180, 2)
    arcade.draw_arc_outline(x - width, y, width, height, arcade.color.BLACK, 0, 90, 2)


def draw_tree(x, y):
    """Drawing tree"""
    crown_height = 100
    crown_width = 40
    # draw trunk
    arcade.draw_rectangle_filled(x, y, 20, 40, arcade.color.DARK_BROWN)
    y_base = y + 20
    polygon_list = ((x - crown_width, y_base), (x + crown_width, y_base), (x, y_base + crown_height))
    arcade.draw_polygon_filled(polygon_list, arcade.color.DARK_GREEN)


if __name__ == '__main__':
    # open window
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    arcade.start_render()

    create_screen()

    # draw birds
    for count in range(10):
        x = random.randrange(30, WINDOW_WIDTH - 30)
        y = random.randrange(int(WINDOW_HEIGHT/3), WINDOW_HEIGHT - 20)
        draw_bird(x, y)

    # draw trees - 1st line
    for i in range(45, WINDOW_WIDTH, 90):
        draw_tree(i, WINDOW_HEIGHT/3)

    # draw trees - 2nd line
    for i in range(65, WINDOW_WIDTH, 90):
        draw_tree(i, WINDOW_HEIGHT / 3 - 120)

    # finish render
    arcade.finish_render()

    # run it
    arcade.run()
