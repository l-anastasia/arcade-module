import arcade

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
WINDOW_TITLE = "SAD FACE"

FACE_RADIUS = 200
EYE_RADIUS = 25
MOUTH_WIDTH = 150
MOUTH_HEIGHT = 150

# open window
arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# set background color
arcade.set_background_color(arcade.color.AERO_BLUE)

# start render - everything after this and before arcade.finish_render will apper on screen
arcade.start_render()

# draw face
arcade.draw_circle_filled(WINDOW_WIDTH/2,
                          WINDOW_HEIGHT/2,
                          FACE_RADIUS,
                          arcade.color.YELLOW)
# draw eyes
arcade.draw_circle_filled(WINDOW_WIDTH/2 - 70, WINDOW_HEIGHT/2 + 50, EYE_RADIUS, arcade.color.BLACK)
arcade.draw_circle_filled(WINDOW_WIDTH/2 + 70, WINDOW_HEIGHT/2 + 50, EYE_RADIUS, arcade.color.BLACK)

# draw mouth
arcade.draw_arc_outline(WINDOW_WIDTH/2,
                        WINDOW_HEIGHT/2 - 100,
                        MOUTH_WIDTH,
                        MOUTH_HEIGHT,
                        arcade.color.BLACK,
                        0,
                        180,
                        20)
# finish render
arcade.finish_render()

# run it
arcade.run()
