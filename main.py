import time
import datetime
import pygame
import sys
import os
import subprocess
import threading
import random
import math
import numpy as np # I didn't use some of these modules, Github Copilot imported them by 'random'


from pygame.locals import *
from pygame.color import THECOLORS
from pygame.font import *
from pygame.time import *
from pygame.event import *
from pygame.display import *
from pygame.image import *
from pygame.mixer import *
from pygame.mixer_music import *
from pygame.mixer_music import *

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
pygame.display.set_caption("Digital Clock")
pygame.font.init()
font = pygame.font.Font(None, 100)


def get_time():
    return time.strftime("%H:%M:%S")


def get_date():
    return time.strftime("%d/%m/%Y")


def get_day():
    return time.strftime("%A")


def get_month():
    return time.strftime("%B")


def get_year():
    return time.strftime("%Y")


def main():
    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(THECOLORS["black"])
        time = screen.blit(font.render(get_time(), True, THECOLORS["white"]), (10, 100))
        date = screen.blit(font.render(get_date(), True, THECOLORS["white"]), (10, 200))
        day = screen.blit(font.render(get_day(), True, THECOLORS["white"]), (10, 300))
        month = screen.blit(font.render(get_month(), True, THECOLORS["white"]), (10, 400))
        year = screen.blit(font.render(get_year(), True, THECOLORS["white"]), (10, 500))

        pygame.draw.rect(screen, THECOLORS["red"], time, 2)
        pygame.draw.rect(screen, THECOLORS["orange"], date, 2)
        pygame.draw.rect(screen, THECOLORS["yellow"], day, 2)
        pygame.draw.rect(screen, THECOLORS["green"], month, 2)
        pygame.draw.rect(screen, THECOLORS["blue"], year, 2)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


main()

