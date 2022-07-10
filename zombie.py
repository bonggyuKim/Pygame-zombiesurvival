from typing import NewType
import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constants
IDLE = -1
WIDTH = 1400
HEIGHT = 1000

class FireBall(pygame.sprite.Sprite):
    def __init__(self, position, player_direction):
        super().__init__()
        direct = player_direction
        self.dir = direct
        self.image = pygame.image.load("fireball.png").convert()
        self.image = pygame.transform.scale(self.image, [50,50])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        pos = [0.0, 0.0]
        pos[0] = position[0]
        pos[1] = position[1]
        self.firstPosition = position
        self.dist = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.count = random.randint(50,250)
        self.time = 0
    def update(self):
        self.time+=1
        if(self.time>self.count):
            self.image = pygame.image.load("fireEffect.jpg").convert()
            self.image = pygame.transform.scale(self.image, [100,100])
            self.image.set_colorkey(BLACK)
            self.time+=1
            if(self.time>self.count+400):
                self.kill()
        
        else:
            self.rect.x += self.dir.x*5
            self.rect.y += self.dir.y*5
class Projectile(pygame.sprite.Sprite):
    def __init__(self,position,fire_direction):
        super().__init__()

        #Creates a fireball with the correct direction
        direct = 0
        direct = fire_direction
        self.dir = direct
        self.image = pygame.image.load("bullet.png").convert()
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.flip(self.image,True,True)
        self.rect = self.image.get_rect()
        

            
        # Moves the fireball slightly so that it doesn't
        # fire from Player's head
        pos = [0.0 , 0.0]
        pos[0] = position[0] +7
        pos[1] = position[1] + 20

        self.dist = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def update(self):
        # updates fireball with a speed of 3
        if self.dist == 140:
            # kills the fireball when it reaches a certain distance
            self.kill()
        elif self.dir == 0:
           self.rect.y += 5
        elif self.dir == 1:
            self.rect.x += 5
        elif self.dir == 5:
           self.rect.y -= 5
        elif self.dir == 10:
            self.rect.x -= 5
        self.dist += 3

    #end update()
#end Projectile()

class Zombie(pygame.sprite.Sprite):
    def __init__(self, zombieKind,x,y):
        super().__init__()
        self.pos = [0.0 , 0.0]
        self.kind = zombieKind
        self.speed = 0.0
        #spawns zombie in random location within map
        self.pos[0] = x  # x
        self.pos[1] = y # y
        self.time = 0
        #creates the zombie
        if(self.kind == 0):
            self.image = pygame.image.load("zombie1-f.png").convert()
            self.image = pygame.transform.scale(self.image,[30,50])
            self.image.set_colorkey(WHITE)
            self.speed = 1.0
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
        elif(self.kind == 1):
            self.image = pygame.image.load("zombie2-f.png").convert()
            self.image = pygame.transform.scale(self.image,[30,50])
            self.image.set_colorkey(WHITE)
            self.speed1 = 1.5
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
        elif(self.kind == 2):
            self.image = pygame.image.load("bose1-f.png").convert()
            self.image = pygame.transform.scale(self.image,[150,100])
            self.image.set_colorkey(WHITE)
            self.speed2 = 0.3
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
        elif(self.kind == 3):
            self.image = pygame.image.load("bose2-f.png").convert()
            self.image = pygame.transform.scale(self.image,[50,75])
            self.image.set_colorkey(WHITE)
            self.speed2 = 0.3
            self.rect = self.image.get_rect()
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
        
        if(self.kind == 0):
            self.hp = 2
        elif(self.kind == 1):
            self.hp = 1
        elif(self.kind == 2):
            self.hp = 50
        elif(self.kind ==3):
            self.hp = 5
        
    def zombieHp(self):
        return self.hp
    def zombieHpM(self, m):
        self.hp-=m
    def zombieKind(self):
        return self.kind
    # end ctor()

    # loses precision if speed is not an integer
    def update(self,num):
        if(self.kind == 0):
            if self.rect.x < num.x:
                self.rect.x += self.speed
                self.image = pygame.image.load("zombie1-r.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.x > num.x:
                self.rect.x -= self.speed
                self.image = pygame.image.load("zombie1-l.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.y < num.y:
                self.rect.y += self.speed
                self.image = pygame.image.load("zombie1-f.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.y > num.y:
                self.rect.y -= self.speed
                self.image = pygame.image.load("zombie1-b.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
        elif(self.kind == 1):
            if self.rect.x < num.x-1:
                self.rect.x += self.speed1*1.4
                self.image = pygame.image.load("zombie2-r.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.x > num.x+1:
                self.rect.x -= self.speed1
                self.image = pygame.image.load("zombie2-l.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.y < num.y-1:
                self.rect.y += self.speed1*1.4
                self.image = pygame.image.load("zombie2-f.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
            if self.rect.y > num.y+1:
                self.rect.y -= self.speed1
                self.image = pygame.image.load("zombie2-b.png").convert()
                self.image = pygame.transform.scale(self.image,[30,50])
                self.image.set_colorkey(WHITE)
        elif(self.kind == 2):
            if self.rect.x < num.x-45:
                self.rect.x = self.rect.x+ 1.0
                self.image = pygame.image.load("bose1-r.png").convert()
                self.image = pygame.transform.scale(self.image,[100,150])
                self.image.set_colorkey(WHITE)
            if self.rect.x > num.x-45:
                self.rect.x = self.rect.x - self.speed2
                self.image = pygame.image.load("bose1-l.png").convert()
                self.image = pygame.transform.scale(self.image,[100,150])
                self.image.set_colorkey(WHITE)
            if self.rect.y < num.y-45:
                self.rect.y = self.rect.y+ 1.0
                self.image = pygame.image.load("bose1-f.png").convert()
                self.image = pygame.transform.scale(self.image,[100,150])
                self.image.set_colorkey(WHITE)
            if self.rect.y > num.y+45:
                self.rect.y = self.rect.y- self.speed2
                self.image = pygame.image.load("bose1-b.png").convert()
                self.image = pygame.transform.scale(self.image,[100,150])
                self.image.set_colorkey(WHITE)
        elif(self.kind == 3):
            if self.rect.x < num.x-25:
                self.rect.x = self.rect.x+ 1.0
                self.image = pygame.image.load("bose2-r.png").convert()
                self.image = pygame.transform.scale(self.image,[50,75])
                self.image.set_colorkey(WHITE)
            if self.rect.x > num.x+25:
                self.rect.x = self.rect.x - self.speed2
                self.image = pygame.image.load("bose2-l.png").convert()
                self.image = pygame.transform.scale(self.image,[50,75])
                self.image.set_colorkey(WHITE)
            if self.rect.y < num.y-25:
                self.rect.y = self.rect.y+ 1.0
                self.image = pygame.image.load("bose2-f.png").convert()
                self.image = pygame.transform.scale(self.image,[50,75])
                self.image.set_colorkey(WHITE)
            if self.rect.y > num.y+25:
                self.rect.y = self.rect.y- self.speed2
                self.image = pygame.image.load("bose2-b.png").convert()
                self.image = pygame.transform.scale(self.image,[50,75])
                self.image.set_colorkey(WHITE)
            
        else:
            return
    #end update()
#end Zombie()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.timer = 0

    #spin is used for char select screen
    def spin(self,screen):
        if self.timer < 20:
            screen.blit(self.image,[700, 700])
        elif self.timer >= 20 and self.timer < 40:
            screen.blit(self.char_right,[700, 700])
        elif self.timer >= 40 and self.timer < 60:
            screen.blit(self.char_back,[700, 700])
        elif self.timer >= 60 and self.timer < 80:
            screen.blit(self.char_left,[700, 700])
        else:
            self.timer = 0
            screen.blit(self.image,[700, 700])
        self.timer += 1
        return
    # end spin()
# end Player()

class Albert(Player):
    def __init__(self):
        super().__init__()
        self.name = "Alby"

        #loads the 4 directions of Alby
        self.image = pygame.image.load("f_albwhite.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, [30,50])
        self.rect = self.image.get_rect()

        self.cahr_idle = pygame.image.load("f_albwhite.png").convert()
        self.cahr_idle.set_colorkey(WHITE)
        self.cahr_idle = pygame.transform.scale(self.image, [30,50])

        

        
        self.char_left = pygame.image.load("rl_alb.png").convert()
        self.char_left.set_colorkey(WHITE)
        self.char_left = pygame.transform.scale(self.char_left,[30,50])

        self.char_right = pygame.transform.flip(self.char_left,True,False)

        self.char_back = pygame.image.load("b_alb.png").convert()
        self.char_back.set_colorkey(BLACK)
        self.char_back = pygame.transform.scale(self.char_back,[30, 50])
        
        self.prev = 0
        #Alby spawns at loc. x = 250, y = 250
        self.rect.x = 700
        self.rect.y = 700
        
        # -1 is a key to remember prev (for idle)
        # 0 for down
        # 1 for right
        # 2 for up
        # 3 for left
        self.direction = 0
    #end ctor()

    def update_pos(self,screen,keys_pressed):
        #For movemen
        if keys_pressed[pygame.K_s]:
            
            if self.rect.y + 2 < HEIGHT - 50:
                # Conditions create boundaries for map
                self.rect.y += 3.0
                self.prev = 0
            #screen.blit(self.image, self.rect)
                self.image = self.cahr_idle
        if keys_pressed[pygame.K_d]:
            
            if self.rect.x + 2 < WIDTH - 50:
                self.rect.x += 3.0
                self.prev = 1
                self.image = self.char_right
           # screen.blit(self.char_right, self.rect)
        if keys_pressed[pygame.K_w]:
           
            if self.rect.y - 2 > 0:
                self.rect.y -= 3.0
                self.prev = 5
                self.image = self.char_back
           # screen.blit(self.char_back, self.rect)
        if keys_pressed[pygame.K_a]:
            
            if self.rect.x - 2 > 0:
                self.rect.x -= 3.0
                self.prev = 10
                self.image = self.char_left
            #screen.blit(self.char_left, self.rect)
        
            
        screen.blit(self.image, self.rect)
        if self.direction == IDLE:
            
            #If no direction
            if self.prev == 0:
                screen.blit(self.cahr_idle, self.rect)
            elif self.prev == 1:
                screen.blit(self.char_right, self.rect)
            elif self.prev == 5:
                screen.blit(self.char_back, self.rect)
            elif self.prev == 10:
                screen.blit(self.char_left,self.rect)  
            
    # end update_pos()
#end Albert()
      
    
def main():
    pygame.init()
    test_sound = pygame.mixer.Sound("C:/Users/rlaqhdrb/Desktop/Zombie/Enemy.mp3")
    test_sound.set_volume(0.5)
    test_sound.play(-1)
    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Zombie Survival")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Intro_Trigger is true until the player hits play
    intro_trigger = True
    choose_character = False
    flickr_count = 0

    #fonts
    Titlefont =  pygame.font.SysFont('Calibri',50,True,False)
    Authorfont = pygame.font.SysFont('Calibri',30,False,True)
    Namefont = pygame.font.SysFont('Calibri', 20, False,False)
    Startfont = pygame.font.SysFont('Arial', 30, True, False)

    #background img
    finish_img = pygame.image.load("victory.png").convert()
    finish_img = pygame.transform.scale(finish_img,(1400,1000))
    background_img = pygame.image.load("zombie.jpg").convert()
    background_img = pygame.transform.scale(background_img,(1400,1000))
    gameplaybackground_img = pygame.image.load("background.png").convert()
    gameplaybackground_img = pygame.transform.scale(gameplaybackground_img,(1400,1000))
    #init the sprite groups
    Alby = Albert()
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(Alby)
    fire_list = pygame.sprite.Group()
    zombie_list = pygame.sprite.Group()
    zombieFire_list = pygame.sprite.Group()
    #Any variables for indexing
    indexer = 1
    time_indexer = 0
    level = 1
    zombieCount = 20
    end_scene = False
    finish_game = False
    kind = 0
    isBossOccur = False
    points = 0
    num_fired = 0
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            # extracts player actions from keyboard
            # and stores within keys_pressed
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.KEYUP:
                Alby.direction = IDLE
            if event.type == pygame.KEYDOWN:
                if choose_character == True and event.key == pygame.K_RETURN:
                    choose_character = False
                if intro_trigger == True and event.key == pygame.K_RETURN:
                    intro_trigger = False
                    choose_character = True
                if event.key == pygame.K_s:
                    Alby.direction = 0
                elif event.key == pygame.K_d:
                    Alby.direction = 1
                elif event.key == pygame.K_w:
                    Alby.direction = 5
                elif event.key == pygame.K_a:
                    Alby.direction = 10
                elif event.key == pygame.K_SPACE:
                    if (not end_scene):
                        num_fired += 1
                    if Alby.direction == IDLE:
                        fire = Projectile(Alby.rect,Alby.prev)
                        fire_list.add(fire)
                    else:    
                        fire = Projectile(Alby.rect,Alby.direction)
                        fire_list.add(fire)
                    

            keys_pressed = pygame.key.get_pressed()      

        if intro_trigger:
            # Intro Page
            screen.blit(background_img, [0,0])
            #flickr is used to control how fast the text flashes
            if flickr_count < 20:
                start = Startfont.render("Enter Start to Play", True, RED) 
                screen.blit(start,[75,400])
                flickr_count += 1
            else:
                flickr_count +=1
                if flickr_count > 30:
                    flickr_count = 0

            # Title page text
            title = Titlefont.render("Alive",True, BLACK)
            screen.blit(title, [60, 100])
            authors = Authorfont.render("KimBongGyu", True, BLACK)
            
            screen.blit(authors, [60,150])
            
        elif choose_character:
            # Choose character screen

            #Background color
            screen.fill(RED)

            #text
            instruct = Authorfont.render("Instructions: ",True, BLACK)
            instructions = Namefont.render("Use the arrows keys to move and spacebar to fire",True,BLACK)
            start = Startfont.render("Enter Start to Play",True, BLACK) 

            #display text to screen
            screen.blit(instruct, [10,10])
            screen.blit(instructions, [10,40])
            screen.blit(start,[400,400])


            # spins the character
            Alby.spin(screen)
        elif(finish_game == True):
            screen.blit(finish_img,[0,0])
        elif(end_scene):
            #end scene  
            screen.fill(RED)

            restart_print = Namefont.render("Hit enter to try again", True, WHITE)
            point_print = Namefont.render("Number of zombies killed: " + str(points), True, BLACK)
            lose_print = Titlefont.render("YOU LOSE!", True, BLACK)

            screen.blit(lose_print, [250,200])
            screen.blit(point_print, [250, 250])
            screen.blit(restart_print, [250, 300])

            # Restarts the game
            if keys_pressed[pygame.K_RETURN]:
                intro_trigger = True
                choose_character = False
                zombie_list = pygame.sprite.Group()
                end_scene = False
                fire_list = pygame.sprite.Group()
                zombieFire_list = pygame.sprite.Group()
                indexer = 1
                time_indexer = 0
                points = 0
                level = 1
                zombieCount = 20
                kind = 0
                isBossOccur = False
                continue
        else:
            score_print = Namefont.render("Score : "+str(points),True,WHITE)
            zombie_print = Namefont.render("Remaing Zombies : "+str(zombieCount),True,WHITE)
            level_print = Namefont.render("Level : "+str(level),True,WHITE)
            # Regular gameplay
            if(isBossOccur == False):
                if (time_indexer == 0):
                    # Creates zombies only when time_indexer is 0
                    
                    for i in range(indexer):
                        kind = random.randint(0,1)
                        x = random.uniform(0.0,1400)
                        y = random.uniform(0.0,1000)
                        test = Zombie(kind,x,y)
                        while(abs(Alby.rect.x- test.rect.x)<200 and abs(Alby.rect.y - test.rect.y)<200):
                            # If zombie spawns within 200 units of character
                            test.rect.x = random.uniform(0.0,1400) # x
                            test.rect.y = random.uniform(0.0,1000) # y
                        if(zombieCount==0):
                            indexer = 0
                            isBossOccur = True
                            break
                        zombie_list.add(test)
                        zombieCount-=1
                    #increase the capacity of zombies spawned for next round
                    if(indexer<6):
                        indexer += 2
                    
                time_indexer += 1
                if(time_indexer > 200):
                    #time_indexer controls how much time is between zombie spawns
                    time_indexer = 0
            else:
                if(level==1):
                    if(time_indexer == 1):
                        kind = 2
                        boss = Zombie(kind,700,0.0)
                        zombie_list.add(boss)
                    time_indexer+=1
                    if(time_indexer>100):
                        kind = 1
                        x1 = random.uniform(boss.rect.x-200,boss.rect.x+200)
                        y1 = random.uniform(boss.rect.y-200,boss.rect.y+200)
                        test = Zombie(kind,x1,y1)
                        zombie_list.add(test)
                        x1 = random.uniform(boss.rect.x-200,boss.rect.x+200)
                        y1 = random.uniform(boss.rect.y-200,boss.rect.y+200)
                        test = Zombie(kind,x1,y1)
                        zombie_list.add(test)
                        time_indexer = 2
                elif(level==2):
                    if(time_indexer == 1):
                        kind = 3
                        boss = Zombie(kind,700,0.0)
                        zombie_list.add(boss)
                    time_indexer+=1
                    if(time_indexer>50):
                        dx, dy = Alby.rect.x - boss.rect.x, Alby.rect.y - boss.rect.y
                        distBA = math.hypot(dx,dy)
                        dx, dy = dx/distBA, dy/distBA
                        vectorB = pygame.Vector2(dx,dy)
                        fire = FireBall(boss.rect,vectorB)
                        zombieFire_list.add(fire)
                        time_indexer = 2
                        print(boss.zombieHp())
                        if(boss.zombieHp()==1):
                            finish_game = True
                            time_indexer = 0
                    
                


            screen.blit(gameplaybackground_img, [0,0])
            screen.blit(level_print,[30,10])
            screen.blit(score_print,[30,30])
            screen.blit(zombie_print,[30,50])
            Alby.update_pos(screen,keys_pressed)
            fire_list.update()
            fire_list.draw(screen)
            zombie_list.update(Alby.rect)
            zombie_list.draw(screen)
            zombieFire_list.update()
            zombieFire_list.draw(screen)

            #kills zombies if they collide with projectiles
            for zombie in zombie_list:
                if pygame.sprite.spritecollide(zombie, fire_list,True):
                    if zombie.zombieHp()==1 and zombie.zombieKind()!=2:
                        isKill = True
                        zombie_list.remove(zombie)
                        points+=1
                    elif zombie.zombieHp()==1 and zombie.zombieKind()==2:
                        isKill = True
                        zombie_list.remove(zombie)
                        points+=10
                        isBossOccur = False
                        zombieCount+=30
                        level+=1
                    elif zombie.zombieHp()==1 and zombie.zombieKind()==3:
                        isKill = True
                        zombie_list.remove(zombie)
                        points+=50
                        isBossOccur = False
                        finish_game = True
                        
                    else:
                        zombie.zombieHpM(1)
            
            #hit_list = pygame.sprite.groupcollide(zombie_list, fire_list,isKill,True)

            
            #increment points if zombie hit
            #for i in hit_list:
            #    points += 1
            
            for zombie in zombie_list:
                if Alby.rect.colliderect(zombie):
                    end_scene = True
                    continue
            for fire in zombieFire_list:
                if Alby.rect.colliderect(fire):
                    end_scene = True
                    continue
                

     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
# end main()

if __name__ == "__main__":
    main()