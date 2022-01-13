import arcade
import math
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BALL_SPIN = 3

WHEEL_SPIN = -8


class Point:
    def __init__(self):
        """This initializes the x and y coordinates"""
        self.x=float(0)
        self.y=float(0)
        
class Velocity:
    def __init__(self):
        """This initializes the x and y velocity"""
        self.dx=float(0)
        self.dy=float(0)


class Wheel:
    def __init__(self):
        self.center = Point()
        self.center.x = 250
        self.center.y = 250
        self.velocity=Velocity()
        self.angle = 0
        self.spin = WHEEL_SPIN
        self.img = "images/roulette_wheel.png"
        self.angle +=self.spin
        
    def draw(self):
        texture = arcade.load_texture(self.img)
        
        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent
        angle = self.angle
        self.angle+=self.spin

        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, angle, alpha)  
        #arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.angle += self.spin


class Ball:
    def __init__(self):
        self.center = Point()
        self.center.x = 250
        self.center.y = 250
        self.velocity=Velocity()
        self.angle = 0
        self.spin = BALL_SPIN
        self.img = "images/roulette_wheel_ball.png"
        
    def draw(self):
        texture = arcade.load_texture(self.img)
        
        width = texture.width
        height = texture.height
        alpha = 255 # For transparency, 1 means not transparent
        angle = self.angle
        self.angle+=self.spin

        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, angle, alpha)  
        #arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
        
        
class Game(arcade.Window):
    
    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        #self.held_keys = set()
        
        self.wheel = Wheel()
        self.ball = Ball()
        
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        
        self.wheel.draw()
        self.ball.draw()
        
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            self.wheel.spin = 0
            self.ball.spin = 0
    
    
# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
    
    