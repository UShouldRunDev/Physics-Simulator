import pygame, pymunk
import tkinter as tk

pygame.init()

root = tk.Tk()
WIDTH = round(root.winfo_screenwidth() * 0.95)
HEIGHT = round(root.winfo_screenheight() * 0.9)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Physics Simulator')

FPS = 60
clock = pygame.time.Clock()

COLORS = {
    'RED': (255,0,0),
    'GREEN': (0,255,0),
    'BLUE': (0,0,255),
    'BLACK': (0,0,0),
    'WHITE': (255,255,255),
    'WHITESMOKE': (245,245,245),
    'DARKCIAN': (0, 79, 79),
    'BUTTON': (47, 79, 79),
    'INTERFACE': (95, 158, 160),
    'BUTTONPRESSED': (102, 205, 170),
    'BUTTONPRESSED2': (170, 205, 102),
    'BACKGROUND': (7, 19, 29),
    'ADDBUTTON': (169, 169, 169)}

# Logo
logo = pygame.image.load('Images/logo.png').convert_alpha()
logoSize = (int(WIDTH/30), int(HEIGHT/9))
pygame.display.set_icon(pygame.transform.scale(logo,(30,70)))

# Simulator Objects and Obstacles
S_SIZE = [7*WIDTH/8, HEIGHT]
S_POS = [WIDTH/8, 0]

# Button Font
letterSizeFactor = 19/1980
letterSize = int(WIDTH * letterSizeFactor)
bFont = pygame.font.SysFont('Times New Roman', letterSize, True)

buttonListX = 10
buttonListStartHeight = HEIGHT/8 + 10
buttonSize = (WIDTH/8 - 2*buttonListX, HEIGHT/16)

buttonListPos = [(buttonListX, int(buttonListStartHeight)),
                (buttonListX, int(buttonListStartHeight + buttonSize[1] + 10)),
                (buttonListX, int(HEIGHT - (buttonSize[1] + 10)))]

bSize = (int(buttonSize[0]*0.8), int(buttonSize[1]*0.8))
buttonSimulationList = [(S_POS[0] + 10, HEIGHT - bSize[1] - 10),
                        (WIDTH - bSize[0] - 10, HEIGHT - bSize[1] - 10),
                        (S_POS[0] + S_SIZE[0]/2 - bSize[0]/2, HEIGHT - bSize[1] - 10)]

buttonLearningList = [(S_POS[0] + 10, HEIGHT - bSize[1] - 10),
                        (WIDTH - bSize[0] - 10, HEIGHT - bSize[1] - 10),
                        (S_POS[0] + S_SIZE[0]/2 - bSize[0]/2, HEIGHT - bSize[1] - 10)]

# Image Function
imageSizeFactorX = 400/1980
imageSizeFactorY = 270/1080
imageSize = (int(WIDTH*imageSizeFactorX), int(HEIGHT*imageSizeFactorY))
def getImage(image, customSize = None):
    '''image = Path to the Image'''
    if customSize == None:
        size = imageSize
    else:
        size = customSize
    return pygame.transform.scale(pygame.image.load('Images/'+image).convert_alpha(), size)

# BackGround Image
bg = pygame.transform.scale(pygame.image.load('Images/background2.jpg').convert_alpha(), S_SIZE)

# Label (Pygame)
titleFontSizeFactor = 50/1980
FontSizeFactor = 20/1980
titleFontSize = int(WIDTH * titleFontSizeFactor)
FontSize = int(WIDTH * FontSizeFactor)
labelHeight = FontSize * 1.05
TITLEFONT = ['Times New Roman', titleFontSize, True, False]
SUBTITLEFONT = ['Times New Roman', int(titleFontSize * 0.60), True, False]
FONT = ['Times New Roman', FontSize, False, False]

