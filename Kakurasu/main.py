import pygame
import BestFSKakurasu,BFSKakurasu
def welcome_page():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font = [pygame.font.Font(None, 60),pygame.font.Font(None, 32)]
    heading = font[0].render('Welcome to Kukarasu Ultimate Solver',True,(255,255,255))
    heading_rect = heading.get_rect()
    heading_rect.center = (400,50)
    text = []
    text.append(font[1].render('Please input the size',True,(255,255,255)))
    text.append(font[1].render('Please input numbers on column',True,(255,255,255)))
    text.append(font[1].render('Please input numbers on row',True,(255,255,255)))
    text_rect = []
    text_rect.append(text[0].get_rect())
    text_rect.append(text[1].get_rect())
    text_rect.append(text[2].get_rect())
    text_rect[0].center = (400,150)
    text_rect[1].center = (400,280)
    text_rect[2].center = (400,410)
    input_rect = []
    input_rect.append(pygame.Rect(200,200,0,0))
    input_rect.append(pygame.Rect(200,200,0,0))
    input_rect.append(pygame.Rect(200,200,0,0))
    image = []
    image.append(pygame.image.load('./image/befs.png'))
    image.append(pygame.image.load('./image/bfs.png'))
    image.append(pygame.image.load('./image/befsdemo.png'))
    image.append(pygame.image.load('./image/bfsdemo.png'))
    image[0] = pygame.transform.scale(image[0],(130,130))
    image[1] = pygame.transform.scale(image[1],(130,130))
    image[2] = pygame.transform.scale(image[2],(130,130))
    image[3] = pygame.transform.scale(image[3],(130,130))
    image_rect = []
    image_rect.append(image[0].get_rect())
    image_rect.append(image[1].get_rect())
    image_rect.append(image[2].get_rect())
    image_rect.append(image[3].get_rect())
    image_rect[0].center = (200,550)
    image_rect[1].center = (600,550)
    image_rect[2].center = (65,550)
    image_rect[3].center = (735,550)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = [color_passive,color_passive,color_passive]
    active = [False,False,False]
    user_text = ['','','']
    check = [True,True,True]
    maxlength = 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None,None,None,None,False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect[0].collidepoint(event.pos): active[0] = True
                else: active[0] = False
                if input_rect[1].collidepoint(event.pos): active[1] = True
                else: active[1] = False
                if input_rect[2].collidepoint(event.pos): active[2] = True
                else: active[2] = False
                if image_rect[0].collidepoint(event.pos):
                    if user_text[0] == '': check[0]=False
                    else:
                        check[0] = True
                        if len(user_text[1].split()) != int(user_text[0]): check[1] = False
                        else: check[1] = True
                        if len(user_text[2].split()) != int(user_text[0]): check[2] = False
                        else: check[2] = True
                        if check[1] and check[2]: return int(user_text[0]),list(map(int,user_text[1].split())),list(map(int,user_text[2].split())),0,True
                if image_rect[1].collidepoint(event.pos):
                    if user_text[0] == '': check[0]=False
                    else:
                        check[0] = True
                        if len(user_text[1].split()) != int(user_text[0]): check[1] = False
                        else: check[1] = True
                        if len(user_text[2].split()) != int(user_text[0]): check[2] = False
                        else: check[2] = True
                        if check[1] and check[2]: return int(user_text[0]),list(map(int,user_text[1].split())),list(map(int,user_text[2].split())),1,True
                if image_rect[2].collidepoint(event.pos):
                    if user_text[0] == '': check[0]=False
                    else:
                        check[0] = True
                        if len(user_text[1].split()) != int(user_text[0]): check[1] = False
                        else: check[1] = True
                        if len(user_text[2].split()) != int(user_text[0]): check[2] = False
                        else: check[2] = True
                        if check[1] and check[2]: return int(user_text[0]),list(map(int,user_text[1].split())),list(map(int,user_text[2].split())),2,True
                if image_rect[3].collidepoint(event.pos):
                    if user_text[0] == '': check[0]=False
                    else:
                        check[0] = True
                        if len(user_text[1].split()) != int(user_text[0]): check[1] = False
                        else: check[1] = True
                        if len(user_text[2].split()) != int(user_text[0]): check[2] = False
                        else: check[2] = True
                        if check[1] and check[2]: return int(user_text[0]),list(map(int,user_text[1].split())),list(map(int,user_text[2].split())),4,True
            if event.type == pygame.KEYDOWN:
                if active[0]:
                    if event.key == pygame.K_RETURN: active[0] = False
                    elif event.key == pygame.K_BACKSPACE: user_text[0] = user_text[0][:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]:user_text[0] += event.unicode
                elif active[1]:
                    if event.key == pygame.K_RETURN: active[1] = False
                    elif event.key == pygame.K_BACKSPACE: user_text[1] = user_text[1][:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_SPACE]:user_text[1] += event.unicode
                elif active[2]:
                    if event.key == pygame.K_RETURN: active[2] = False
                    elif event.key == pygame.K_BACKSPACE: user_text[2] = user_text[2][:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_SPACE]:user_text[2] += event.unicode
        screen.fill((0, 0, 0))
        if not check[0]:
            error0 = font[1].render('Missing input for size',True,(255,0,0))
            error0_rect = error0.get_rect()
            error0_rect.center = (400,230)
            screen.blit(error0,error0_rect)
        if not check[1]:
            error1 = font[1].render('Wrong number of inputs on column',True,(255,0,0))
            error1_rect = error1.get_rect()
            error1_rect.center = (400,370)
            screen.blit(error1,error1_rect)
        if not check[2]:
            error2 = font[1].render('Wrong number of inputs on row',True,(255,0,0))
            error2_rect = error2.get_rect()
            error2_rect.center = (400,500)
            screen.blit(error2,error2_rect)
        if active[0]: color[0] = color_active
        else: color[0] = color_passive
        if active[1]: color[1] = color_active
        else: color[1] = color_passive
        if active[2]: color[2] = color_active
        else: color[2] = color_passive
        text_surface = []
        if len(user_text[0])>maxlength: text_surface.append(font[1].render(user_text[0][len(user_text[0])-maxlength-1:-1], True, (255, 255, 255)))
        else: text_surface.append(font[1].render(user_text[0], True, (255, 255, 255)))
        if len(user_text[1])>maxlength: text_surface.append(font[1].render(user_text[1][len(user_text[1])-maxlength-1:-1], True, (255, 255, 255)))
        else: text_surface.append(font[1].render(user_text[1], True, (255, 255, 255)))
        if len(user_text[2])>maxlength: text_surface.append(font[1].render(user_text[2][len(user_text[2])-maxlength-1:-1], True, (255, 255, 255)))
        else: text_surface.append(font[1].render(user_text[2], True, (255, 255, 255)))
        pygame.draw.rect(screen, color[0], input_rect[0])
        input_rect[0].w = max(50, text_surface[0].get_width())
        input_rect[0].h = text_surface[0].get_height()
        input_rect[0].center = (400,200)
        pygame.draw.rect(screen, color[1], input_rect[1])
        input_rect[1].w = max(50, text_surface[1].get_width())
        input_rect[1].h = text_surface[1].get_height()
        input_rect[1].center = (400,330)
        pygame.draw.rect(screen, color[2], input_rect[2])
        input_rect[2].w = max(50, text_surface[2].get_width())
        input_rect[2].h = text_surface[2].get_height()
        input_rect[2].center = (400,460)
        screen.blit(text_surface[0], input_rect[0])
        screen.blit(text_surface[1], input_rect[1])
        screen.blit(text_surface[2], input_rect[2])
        screen.blit(heading, heading_rect)
        screen.blit(text[0], text_rect[0])
        screen.blit(text[1], text_rect[1])
        screen.blit(text[2], text_rect[2])
        screen.blit(image[0], image_rect[0])
        screen.blit(image[1], image_rect[1])
        screen.blit(image[2], image_rect[2])
        screen.blit(image[3], image_rect[3])
        pygame.display.flip()
def solution_page(size,solution):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font = [pygame.font.Font(None, 60),pygame.font.Font(None, 32)]
    heading = font[0].render('Solution',True,(255,255,255))
    heading_rect=heading.get_rect()
    heading_rect.center = (400,50)
    image = []
    image.append(pygame.image.load('./image/home.png'))
    image.append(pygame.image.load('./image/quit.png'))
    image.append(pygame.image.load('./image/forward.png'))
    image.append(pygame.image.load('./image/backward.png'))
    image[0] = pygame.transform.scale(image[0],(130,130))
    image[1] = pygame.transform.scale(image[1],(130,130))
    image[2] = pygame.transform.scale(image[2],(130,130))
    image[3] = pygame.transform.scale(image[3],(130,130))
    image_rect = []
    image_rect.append(image[0].get_rect())
    image_rect.append(image[1].get_rect())
    image_rect.append(image[2].get_rect())
    image_rect.append(image[3].get_rect())
    image_rect[0].center = (65,550)
    image_rect[1].center = (735,550)
    image_rect[2].center = (735,300)
    image_rect[3].center = (65,300)
    current_step = 0
    if len(solution)!=0:
        while True:
            screen.fill((0,0,0))
            surface = pygame.Surface((size*35,size*35))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_rect[0].collidepoint(event.pos): return True
                    if image_rect[1].collidepoint(event.pos): return False
                    if image_rect[2].collidepoint(event.pos):
                        if current_step != len(solution)-1: current_step+=1
                    if image_rect[3].collidepoint(event.pos):
                        if current_step != 0: current_step-=1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if current_step != len(solution)-1: current_step+=1
                    if event.key == pygame.K_LEFT:
                        if current_step != 0: current_step-=1
            for row in range(size):
                for col in range(size):
                    color=(255,255,255)
                    if solution[current_step][row][col]==0: color=(0,0,0)
                    pygame.draw.rect(surface,color,pygame.Rect(35*col+5,35*row+5,25,25))
                    if col!=size-1: pygame.draw.line(surface,(255,255,255),(35*col+35,35*row),(35*col+35,35*row+35))
                if row!=size-1: pygame.draw.line(surface,(255,255,255),(0,35*row+35),(35*size,35*row+35))
            screen.blit(heading,heading_rect)
            step_text = font[1].render('Position number '+str(current_step+1),True,(255,255,255))
            step_text_rect = step_text.get_rect()
            step_text_rect.center = (400,100)
            screen.blit(step_text,step_text_rect)
            surface = pygame.transform.scale(surface,(300,300))
            surface_rect=surface.get_rect()
            surface_rect.center = (400,350)
            screen.blit(image[0], image_rect[0])
            screen.blit(image[1], image_rect[1])
            if current_step != len(solution)-1: screen.blit(image[2], image_rect[2])
            if current_step != 0: screen.blit(image[3], image_rect[3])
            screen.blit(surface,surface_rect)
            pygame.display.flip()
    else:
        nosol = font.render("No solution is found",True,(255,255,255))
        nosol_rect = nosol.get_rect()
        nosol_rect.center = (400,300)
        screen.blit(nosol,nosol_rect)
        screen.blit(heading, heading_rect)
        screen.blit(image[0], image_rect[0])
        screen.blit(image[1], image_rect[1])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_rect[0].collidepoint(event.pos): return True
                    if image_rect[1].collidepoint(event.pos): return False
def demo_page(size,demo):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font = [pygame.font.Font(None, 60),pygame.font.Font(None, 32)]
    heading = font[0].render('Visualization',True,(255,255,255))
    heading_rect=heading.get_rect()
    heading_rect.center = (400,50)
    image = []
    image.append(pygame.image.load('./image/home.png'))
    image.append(pygame.image.load('./image/quit.png'))
    image.append(pygame.image.load('./image/forward.png'))
    image.append(pygame.image.load('./image/backward.png'))
    image.append(pygame.image.load('./image/control.png'))
    image[0] = pygame.transform.scale(image[0],(130,130))
    image[1] = pygame.transform.scale(image[1],(130,130))
    image[2] = pygame.transform.scale(image[2],(130,130))
    image[3] = pygame.transform.scale(image[3],(130,130))
    image[4] = pygame.transform.scale(image[4],(130,130))
    image_rect = []
    image_rect.append(image[0].get_rect())
    image_rect.append(image[1].get_rect())
    image_rect.append(image[2].get_rect())
    image_rect.append(image[3].get_rect())
    image_rect.append(image[4].get_rect())
    image_rect[0].center = (65,550)
    image_rect[1].center = (735,550)
    image_rect[2].center = (735,300)
    image_rect[3].center = (65,300)
    image_rect[4].center = (400,550)
    current_step = 0
    if len(demo)!=0:
        manual = True
        while True:
            screen.fill((0,0,0))
            surface = pygame.Surface((size*35,size*35))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_rect[0].collidepoint(event.pos): return True
                    if image_rect[1].collidepoint(event.pos): return False
                    if image_rect[2].collidepoint(event.pos) and manual:
                        if current_step != len(demo)-1: current_step+=1
                    if image_rect[3].collidepoint(event.pos) and manual:
                        if current_step != 0: current_step-=1
                    if image_rect[4].collidepoint(event.pos):
                        manual = not manual
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and manual:
                        if current_step != len(demo)-1: current_step+=1
                    if event.key == pygame.K_LEFT and manual:
                        if current_step != 0: current_step-=1
            screen.blit(image[4], image_rect[4])
            if manual:
                control = font[1].render('Auto',True,(0,0,0))
                control_rect = control.get_rect()
                control_rect.center = (400,550)
                screen.blit(control,control_rect)
            else:
                control = font[1].render('Manual',True,(0,0,0))
                control_rect = control.get_rect()
                control_rect.center = (400,550)
                screen.blit(control,control_rect)
                if current_step != len(demo)-1: current_step+=1
            for row in range(size):
                for col in range(size):
                    color=(255,255,255)
                    if demo[current_step][row][col]==0: color=(0,0,0)
                    pygame.draw.rect(surface,color,pygame.Rect(35*col+5,35*row+5,25,25))
                    if col!=size-1: pygame.draw.line(surface,(255,255,255),(35*col+35,35*row),(35*col+35,35*row+35))
                if row!=size-1: pygame.draw.line(surface,(255,255,255),(0,35*row+35),(35*size,35*row+35))
            screen.blit(heading,heading_rect)
            step_text = font[1].render('Step number '+str(current_step+1),True,(255,255,255))
            step_text_rect = step_text.get_rect()
            step_text_rect.center = (400,100)
            screen.blit(step_text,step_text_rect)
            surface = pygame.transform.scale(surface,(300,300))
            surface_rect=surface.get_rect()
            surface_rect.center = (400,350)
            screen.blit(image[0], image_rect[0])
            screen.blit(image[1], image_rect[1])
            if current_step != len(demo)-1: screen.blit(image[2], image_rect[2])
            if current_step != 0: screen.blit(image[3], image_rect[3])
            screen.blit(surface,surface_rect)
            pygame.display.flip()
            if not manual: pygame.time.delay(min(int(10000/len(demo)),500))
    else:
        nosol = font.render("No solution is found",True,(255,255,255))
        nosol_rect = nosol.get_rect()
        nosol_rect.center = (400,300)
        screen.blit(nosol,nosol_rect)
        screen.blit(heading, heading_rect)
        screen.blit(image[0], image_rect[0])
        screen.blit(image[1], image_rect[1])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_rect[0].collidepoint(event.pos): return True
                    if image_rect[1].collidepoint(event.pos): return False
def main():
    pygame.init()
    loop = True
    while loop:
        size,column,row,type,check = welcome_page()
        if not check: break
        elif type==0:
            solution,demo = BestFSKakurasu.main(size,column,row)
            loop = solution_page(size,solution)
        elif type==1:
            solution,demo = BFSKakurasu.main(size,column,row)
            loop = solution_page(size,solution)
        elif type==2:
            solution,demo = BestFSKakurasu.main(size,column,row)
            loop = demo_page(size,demo)
        else:
            solution,demo = BFSKakurasu.main(size,column,row)
            loop = demo_page(size,demo)
    print('Thanh you for using our solver!')
    print('Give us 10 point!')
main()