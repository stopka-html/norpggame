
import pygame
pygame.init()

game_font  = pygame.font.Font('font/PixelifySans-Medium.ttf', 10)

SCREEN_HEIGHT, SCREEN_WIDTH = 500,800

image_path= ""
class sector():
    x = 0
    points= []
    y = 0
    number = 0
    def __init__(self, points, number):
        self.points = points
        self.number = number
    def move_left(self):
        for i in range(len(self.points)):
            self.points[i][0] = self.points[i][0] - 1
    def move_right(self):
        for i in range(len(self.points)):
            self.points[i][0] = self.points[i][0] + 1
    def move_up(self):
        for i in range(len(self.points)):
            self.points[i][1] = self.points[i][1] - 1
    def move_down(self):
        for i in range(len(self.points)):
            self.points[i][1] = self.points[i][1] + 1
sector_array = []
class move_button():
    stype = ''
    x , y = 0, 0
    a = 0
    def __init__(self, type, x, y, a):
        self.stype = type
        self.x = x
        self.y = y
        self.a = a
        
    def clickme(self,i):
        if self.stype == 'left':
            sector_array[i].move_left()
        if self.stype == 'right':
            sector_array[i].move_right()
        if self.stype == 'up':
            sector_array[i].move_up()
        if self.stype == 'down':
            sector_array[i].move_down()

class Players_stat:
    avatar = pygame.image.load(image_path+'image/avt.jpeg')
    name = 0
    dmg = 1
    dfn = 0
    lvl = 0
    hp = 100
    mana = 100
    
    def __init__(self, name, avatar):
        self.name = game_font.render(name, True, 'white')
    def draw_stat(self, xn, yn):
        game_hud.blit(self.avatar, (xn, yn))
        pygame.draw.rect(game_hud, 'green', pygame.Rect(xn+40,yn+15, self.hp, 10))
        pygame.draw.rect(game_hud, 'blue', pygame.Rect(xn+40,yn+20, self.mana, 10))
        game_hud.blit(self.name, (xn+45,yn))
        xl = xn+45
        undermen = [ self.dmg, self.dfn, self.lvl]
        for i in range(3):
            game_hud.blit(game_font.render(str(undermen[i]), True, 'white'), (xl+(45*i),yn+30))
            pygame.draw.rect(game_hud, 'white', (xl+(45*i)-5, yn+30, 20,15), 1)
sector_array = []
x1 = 30
y1 = 0 
i = 0
num = 1
c = 0

# init map
for it in range(0,626):
    
    points = [[x1 + (20 * i) -c , y1], [(x1-10) + (20*i) - c, (y1+10)], [(x1-10)+(20*i) - c, (y1+20)], [x1+(20*i)-c, y1+30], [(x1+10)+(20*i)-c, (y1+20)], [(x1+10)+(20*i)-c, (y1+10)]]
    sector_array.append(sector(points, it))
    
    if i == 24:
        i = 0
        
        y1 += 25
    else:
        i += 1

    if num == 25 and c == 0:
        c = 10
        num = 0
    elif num == 25 and c == 10:
        c = 0
        num = 0
    num += 1
    
# init button
move_but = [move_button('left', 40, 400, 25),
            move_button('right', 80, 400,25), 
            move_button('up', 60, 375,25), 
            move_button('down', 60, 425,25)]
# game hud screen
game_hud = pygame.Surface((200,500))
game_hud.fill('black')


scale = 1

screeen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
menu_right = pygame.image.load(image_path+'image/rm.jpg')
menu_font = pygame.font.Font(image_path+'font/PixelifySans-Medium.ttf', 30)
play_button = menu_font.render('Грати', True, 'white')
play_button_rect = play_button.get_rect(topleft=(30,150))
exit_button = menu_font.render('Вихід', True, 'white')
exit_button_rect = exit_button.get_rect(topleft=(30,200))

mime = Players_stat('mime',2)

start_game = False
start_menu = True
running = True
while running:
    
    mouse= pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    if start_menu:

        click = pygame.mouse.get_pressed()[0]


        if play_button_rect.collidepoint(mouse) and not click:
            pygame.draw.circle(screeen, 'white', (150,170), 10 )
        elif play_button_rect.collidepoint(mouse) and click:
            print('грати')
            start_game = True
            start_menu = False
        elif exit_button_rect.collidepoint(mouse) and not click:
            pygame.draw.circle(screeen, 'white', (150,215), 10 )
        elif exit_button_rect.collidepoint(mouse) and click:
            print('вихід')
            running = False
            pygame.quit()
        else:
            screeen.fill('black')
            screeen.blit(menu_right, (290,50))
            screeen.blit(play_button, play_button_rect)
            screeen.blit(exit_button, exit_button_rect)
    elif start_game:
        keys = pygame.key.get_pressed()
        
        print(sector_array[0].points[0])
        screeen.fill('black')
        for i in range(len(sector_array)):
            sectors_array_rect = pygame.draw.polygon(screeen, 'white', sector_array[i].points)
            if sectors_array_rect.collidepoint(pygame.mouse.get_pos()):
                print(sector_array[i].number, sector_array[i].points[0])
        for i in range(len(move_but)):
            move_but_rect = pygame.draw.rect(screeen, 'red', pygame.Rect(move_but[i].x, move_but[i].y, move_but[i].a, move_but[i].a))
            if move_but_rect.collidepoint(pygame.mouse.get_pos()) and click:
                for it in range(len(sector_array)):
                    move_but[i].clickme(it)
        screeen.blit(game_hud, (600,0))
        mime.draw_stat(10,10)
            



        
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()
