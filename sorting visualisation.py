import pygame
import random

pygame.init()

#Create a screen
screen = pygame.display.set_mode((900,650))

#Setting the title and logo
pygame.display.set_caption('Insertion Sort Visualization')
icon = pygame.image.load('swap.png')
pygame.display.set_icon(icon)

#Printing the text
def text_render():

    font = pygame.font.Font('freesansbold.ttf' , 15)

    txt3 = font.render('DEMONSTRATION OF INSERTION SORT' , True , (0 , 0 , 0))
    screen .blit(txt3 , (20 , 5))
    
    txt1 = font.render('PRESS "ENTER" TO SORT' , True , (0,0,0))
    screen.blit(txt1 , (20, 30))

    txt2 = font.render('PRESS "SPACE" KEY TO GENERATE AN ARRAY' , True , (0,0,0))
    screen.blit(txt2 , (20 , 55))

#Creating array and giving them the colors
arr = [0]*100
arr_clr =[(0, 204, 102)]*100
clr =[(0, 204, 102), (255, 0, 0),  (0, 0, 153), (255, 102, 0)] 

#Method to generate random array of size 100
def generate_array():
    for i in range(1 , 100):
        arr_clr[i] = clr[0]
        arr[i] = random.randrange(1 , 100)

generate_array()

#Screen variables
width = 900
length = 600



#Method to draw the array on the screen
def draw():
    
    element_width =(width-100)//100
    boundry_arr = 900/100
    boundry = 550 / 100

    text_render()
    pygame.draw.line(screen , (0 , 0 , 0) , (15 , 90) , (785 , 90) , 1)
    for i in range(1, 100): 
        pygame.draw.line(screen , arr_clr[i] , (boundry_arr * i-3, 100) , (boundry_arr * i-3, arr[i]*boundry + 100) , element_width)



#Method to refill the screen while sorting , kind of the frames
def refill(): 
    screen.fill((255, 255, 255)) 
    draw() 
    pygame.display.update() 
    pygame.time.delay(20)


#Algorithm of insertion sort
def insertion_sort(arr):
    pygame.event.pump()
    for i in range (2 , len(arr)):
        value = arr[i]
        hole = i
        arr_clr[i] = clr[2]
        while hole > 0 and arr[hole-1] > value:
            arr_clr[hole-1]  = clr[1]
            arr[hole] = arr[hole-1]
            hole = hole - 1
        refill()
        arr[hole] = value    
    refill()    


#Running the application
run = True
while run:

    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generate_array()
                
            if event.key == pygame.K_RETURN:
                insertion_sort(arr)
            
    draw()
    pygame.display.update()        