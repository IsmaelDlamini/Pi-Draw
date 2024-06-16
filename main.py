
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pixel draw")

app_font = pygame.font.Font("freesansbold.ttf", 30)

pressed = False

fps = 2000
software_name = "Pixel_Art V0.1 coded by Ismail"
clock = pygame.time.Clock()


erasing = False
chose_eraser = False
clear_all = False
color = "black"
chosing_color = False
chosing_shape = False


all_pixels = []
shape_list = []

radius = 0

starting = []

all_pixels = []
press_number = 0
current_p_num = 0
all_lines = []
number_of_lines = 0

pixel_world = []
pixel_world2 = []

target = []
eraserPixelCoordinates = []

eraserPixelConnectorLines = []
eraserPixelTempStorage = []
eraser_line_number = 0

blockSize = 5


class Draw:
    
    def __init__(self): 
        self.mouse_pressed = False
        self.new_pixels = [] #The pixels collected on mouse press (volatile)
        self.all_pixels = [] #All the pixels collected since the beginning of program (non-volatile)
        self.sorted_pixels = [] #2Dimensional array containing the separated pixel arrays(new pixels array)
          
    def record_coordinates(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos() 
            new_pixel = mouse_pos + (color,) + (blockSize,) # mouse position(x, y), color and the size of the square
             
            # Add a new pixel to the new_pixel array if it does not exist
            if new_pixel not in self.new_pixels:
                self.new_pixels.append(new_pixel)
                
            # Add a new pixel to the all_pixels array if it does not exist    
            if new_pixel not in self.all_pixels:
                self.all_pixels.append(new_pixel)

        # Check if the mouse if pressed(meaning the user is drawing actively)
        elif not pygame.mouse.get_pressed()[0]:
            if self.new_pixels.len() > 0: 
                self.sorted_pixels.append(self.new_pixels) # If the mouse is not pressed check if there is any new pixels and append the rest
                self.new_pixels = []

        # if press_number != current_p_num:
        #     pixel_world.append(all_pixels)
        #     all_pixels = []
        #     current_p_num = press_number
        
    def test(self):
        if pygame.mouse.get_pressed()[0]:
            print(self.new_pixels)
            print(self.all_pixels)    
            print(self.sorted_pixels)


draw_object = Draw()


class Shapes:

    def __init__(self, current_color):
        self.chosing_shape = False
        self.current_color = current_color
        self.radius = 0
        self.mouse_initial_pos = []
        self.shape_list = []

    def show_menu(self):

        colors = ["black", "white", "black", "black",]
        x_y = [[150, 350], [155, 255], [160, 400], [255, 355]]
        W_H = [[200, 147], [190, 137], [60, 40], [10, 137]]
        count = 0
        for shape in range(4):
            pygame.draw.rect(
                screen, colors[count], (x_y[count][0], x_y[count][1], W_H[count][0], W_H[count][1]))

    def record_shape_coordinates(self): #this one just takes in the coordinates of the circle
                     
        pygame.draw.rect(screen, "black", (150, 350, 200, 147))
        pygame.draw.rect(screen, "white", (155, 355, 190, 137))

        pygame.draw.rect(screen, "black", (160, 400, 60, 40))
        pygame.draw.rect(screen, "black", (255, 355, 10, 137))
        
        self.show_menu()

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] > 50 and mouse_pos[1] < 500:
                
                if len(self.mouse_initial_pos) < 1:
                    self.mouse_initial_pos.append(mouse_pos)

                current_mouse_position = mouse_pos
                distance_x = mouse_pos[0] - self.mouse_initial_pos[0][0]
                distance_y = mouse_pos[1] - self.mouse_initial_pos[0][1]
            
                self.radius = int(
                    round(math.sqrt(distance_x ** 2 + distance_y ** 2), 0))

                shape = pygame.draw.circle(
                    screen, color, (self.mouse_initial_pos[0][0], self.mouse_initial_pos[0][1]), self.radius)
                            
        if not pygame.mouse.get_pressed()[0] and self.radius != 0:
            self.shape_list.append(
                self.mouse_initial_pos[0] + (self.radius, ) + (self.current_color, ))

        if not pygame.mouse.get_pressed()[0]:
            self.mouse_initial_pos = []
            self.radius = 0
        
    def draw_shape_on_screen(self):
        for shape in self.shape_list:
            pygame.draw.circle(screen, shape[3], (shape[0], shape[1]), shape[2])


shape_object = Shapes(color)


def place_pixels_test():

    for pixel in all_pixels:
        pygame.draw.rect(screen, pixel[2], (pixel[0], pixel[1], 5, 5))


def header():

    pygame.draw.rect(screen, "light blue", (0, 0, WIDTH, 50))

    header_text_font = pygame.font.SysFont('system', 30, True, False)
    header_text = header_text_font.render(software_name, False, "black")
    screen.blit(header_text, (WIDTH // 2 - header_text.get_width()//2, 25))


def footer():

    global chosing_color, chosing_shape

    pygame.draw.rect(screen, "light blue", (0, 500, WIDTH, 100))
    pygame.draw.rect(screen, "black", (0, 500, WIDTH, 2))

    current_color_font = pygame.font.Font("freesansbold.ttf", 20)
    current_color_text = current_color_font.render(
        "current color:", False, "black")
    screen.blit(current_color_text, (20, 510))
    pygame.draw.rect(screen, color, (current_color_text.get_width(
    ) + 20, 511, 40, 25), border_radius=5)

    chose_color_font = pygame.font.SysFont('system', 30, True, False)
    chose_color_text = chose_color_font.render('chose color', False, "white")

    chose_color = pygame.draw.rect(
        screen, "black", (20, 540, 155, 36), border_radius=10)
    screen.blit(chose_color_text, (30, 547))

    chose_shape_font = pygame.font.SysFont('system', 30, True, False)
    chose_shape_text = chose_color_font.render('shapes', False, "white")

    chose_shape = pygame.draw.rect(
        screen, "black", (190, 540, 100, 36), border_radius=10)
    screen.blit(chose_shape_text, (200, 547))

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if chose_color.collidepoint(pos):
            chosing_color = True

        if chose_shape.collidepoint(pos):
            chosing_shape = True
            Shapes.chosing_shape = True


def eraser():

    global erasing

    erasing = True

    if erasing:
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            pygame.draw.rect(
                screen, "green", (pos[0] - 20, pos[1] - 20, 40, 40), border_radius=30)

            for erase_pixel in all_pixels:
                if pos[0] - 20 < erase_pixel[0] < pos[0] + 20:
                    if pos[1] - 20 < erase_pixel[1] < pos[1] + 20:
                        all_pixels.remove(erase_pixel)


def color_menu():

    global color, chosing_color, chose_eraser

    block = 0
    block_pos = 0

    x_pos = [20, 80, 140, 20, 80, 140, 20, 80, 140]
    y_pos = [300, 300, 300, 360, 360, 360, 420, 420, 420]
    width = [60, 60, 60, 60, 60, 60, 60, 60, 60]
    height = [60, 60, 60, 60, 60, 60, 60, 60, 60]
    color_list1 = ["yellow", "red", "green", "blue",
                   "brown", "black", "pink", "teal", "grey"]
    rectangles = []
    background = [10, 290, 200, 200, "black"]

    color_list2 = [[color_list1[0], color_list1[1], color_list1[2]],
                   [color_list1[3], color_list1[4], color_list1[5]],
                   [color_list1[6], color_list1[7], color_list1[8]]]

    chosen_color = ""

    pygame.draw.rect(
        screen, background[4], (background[0], background[1], background[2], background[3]))

    for box in range(len(x_pos)):
        pygame.draw.rect(
            screen, color_list1[block], (x_pos[block], y_pos[block], width[block], height[block]))
        rectangle = pygame.draw.rect(
            screen, color_list1[block], (x_pos[block], y_pos[block], width[block], height[block]))
        block += 1
        rectangles.append(rectangle)

    if chosing_color:
        for rectangle in rectangles:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if rectangle.collidepoint(pos):
                    chosen_color = []
                    chosen_color = color_list2[rectangle[1] //
                                               60 - 5][x_pos.index(rectangle[0])]
                    color = chosen_color
                    chosing_color = False
    chose_eraser = False


def cord_record():

    global all_pixels, current_p_num

    if pressed:
        mouse_pos = pygame.mouse.get_pos()
        complete_pixel = mouse_pos + (color,) + (blockSize,)
        if complete_pixel not in all_pixels:
            all_pixels.append(complete_pixel)
        if complete_pixel not in pixel_world2:
            pixel_world2.append(complete_pixel)

    if press_number != current_p_num:
        pixel_world.append(all_pixels)

        all_pixels = []

        current_p_num = press_number


def eraser_and_clear_button():

    global chose_eraser, red, blue, black
    global clear_all, all_pixels, press_number, pixel_world2, pixel_world

    eraser_font = pygame.font.SysFont('system', 30, True, False)
    eraser_text = eraser_font.render('Eraser', False, "black")

    clear_font = pygame.font.SysFont('system', 30, True, False)
    clear_text = eraser_font.render('Clear', False, "black")

    pygame.draw.rect(screen, "green", (300, 540, 100, 36), border_radius=10)
    screen.blit(eraser_text, (315, 550))

    pygame.draw.rect(screen, (255, 0, 0),
                     (425, 540, 100, 36), border_radius=10)
    screen.blit(clear_text, (441, 550))

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if 300 < pos[0] < 400:
            if 540 < pos[1] < 576:
                chose_eraser = True

        if 425 < pos[0] < 525:
            if 540 < pos[1] < 576:
                clear_all = True
                chose_erasor = False

    if chose_eraser:
        pygame.draw.rect(screen, "white", (290, 535,
                         120, 46), border_radius=10)
        pygame.draw.rect(screen, "green", (300, 540,
                         100, 36), border_radius=10)
        screen.blit(eraser_text, (315, 550))

    if clear_all:
        pixel_world = []
        pixel_world2 = []
        all_pixels = []
        press_number = 0
        clear_all = False


def shapes():

    global starting, radius

    pygame.draw.rect(screen, "black", (150, 350, 200, 147))
    pygame.draw.rect(screen, "white", (155, 355, 190, 137))

    pygame.draw.rect(screen, "black", (160, 400, 60, 40))
    pygame.draw.rect(screen, "black", (255, 355, 10, 137))

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if pos[1] > 50 and pos[1] < 500:

            if len(starting) < 1:
                starting.append(pos)

            current = pos

            distance_x = pos[0] - starting[0][0]
            distance_y = pos[1] - starting[0][1]

            radius = int(
                round(math.sqrt(distance_x ** 2 + distance_y ** 2), 0))

            shape = pygame.draw.circle(
                screen, color, (starting[0][0], starting[0][1]), radius)

    if not pygame.mouse.get_pressed()[0] and radius != 0:
        shape_list.append(starting[0] + (radius, ) + (color, ))

    if not pygame.mouse.get_pressed()[0]:
        starting = []
        radius = 0


def place_pixels():

    global number_of_lines, all_lines, pixel_world, pixel_count_1, pixel_count_2, line_number
    global pixel_count_main, line_number_pixel, pixel_count_3, pixel_count_4, blockSize

    pixel_count_1 = 0  # starting position of the line that will be connecting the pixels
    # the ending position (it will take the pixel data after it)
    pixel_count_2 = 1
    line_number = 0  # this controls the number of lines that are drawn on the screen

    pixel_count_main = 0
    line_number_pixel = 0

    pixel_count_3 = 0
    pixel_count_4 = 1

    for pixel in pixel_world2:  # pixelWorld2 is for all the pixels so i can be able to iterate through the list in a straight way
        pygame.draw.rect(
            screen, pixel[2], (pixel[0], pixel[1], pixel[3], pixel[3]), border_radius=10)

    for a in range(press_number):
        for i in range(len(pixel_world[line_number]) - 1):
            line = pygame.draw.line(screen, pixel_world[line_number][pixel_count_1][2], (pixel_world[line_number][pixel_count_1][0], pixel_world[line_number][pixel_count_1][1]), (
                pixel_world[line_number][pixel_count_2][0], pixel_world[line_number][pixel_count_2][1]), width=5 + pixel_world[line_number][pixel_count_1][3])
            # all_lines.append(line)
            pixel_count_1 += 1
            pixel_count_2 += 1

        line_number += 1

        pixel_count_1 = 0
        pixel_count_2 = 1

        if line_number == press_number:
            line_number = 0


    #the current list of all the pixels that are being recorded
    for pixel in all_pixels:
        pygame.draw.rect(
            screen, pixel[2], (pixel[0], pixel[1], pixel[3], pixel[3]), border_radius=10)

    for i in range(len(all_pixels) - 1):
        line = pygame.draw.line(screen, all_pixels[pixel_count_3][2], (all_pixels[pixel_count_3][0], all_pixels[pixel_count_3][1]), (
            all_pixels[pixel_count_4][0], all_pixels[pixel_count_4][1]), width=5 + all_pixels[pixel_count_3][3])
        pixel_count_3 += 1
        pixel_count_4 += 1


def placeEraserPixels():

    global blockSize, color

    blockSize = 20
    color = "white"


running = True

while running:

    screen.fill("white")
    clock.tick(fps)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False
            pos = pygame.mouse.get_pos()

            if pos[1] < 500 and not chosing_color and not clear_all:
                press_number += 1

    mouse_pos1 = pygame.mouse.get_pos()

    if mouse_pos1[1] > 0 and mouse_pos1[1] < 499:
        cord_record()

    place_pixels()
    header()
    footer()
    eraser_and_clear_button()

    if chose_eraser:
        placeEraserPixels()
    if chosing_color:
        color_menu()
    if chosing_shape:
        shape_object.show_menu()
        shape_object.record_shape_coordinates()
       
    shape_object.draw_shape_on_screen()
    #print(shape_object.shape_list)
    # print(pixel_world2)

    press_number = len(pixel_world)
    
    if pygame.mouse.get_pressed()[0]:
        draw_object.record_coordinates()
        draw_object.test()

    pygame.display.update()

pygame.display.quit()
