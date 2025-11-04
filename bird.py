from pico2d import load_image, get_time
from random import *
import game_world
import game_framework

TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    def __init__(self):

        self.x, self.y = randint(100,500), randint(400,600)
        self.frame = 0
        self.face_dir = 1
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 183, 325, 183, 163,
                                           self.x, self.y,80,70,0)
        else:
            self.image.clip_draw(int(self.frame) * 183, 163, 12, 20, self.x, self.y)

