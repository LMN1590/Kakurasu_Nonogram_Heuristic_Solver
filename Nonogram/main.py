import pygame
def welcome_page():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font0 = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 32)
    heading = font0.render('Welcome to Kukarasu Ultimate Solver',True,(255,255,255))
    heading_rect=heading.get_rect()
    heading_rect.center = (400,50)
    text0 = font.render('Please input the size',True,(255,255,255))
    text0_rect = text0.get_rect()
    text0_rect.center = (400,150)
    input0_rect = pygame.Rect(200,200,0,0)
    text1 = font.render('Please input numbers on column',True,(255,255,255))
    text1_rect = text1.get_rect()
    text1_rect.center = (400,280)
    input1_rect = pygame.Rect(200,200,0,0)
    text2 = font.render('Please input numbers on row',True,(255,255,255))
    text2_rect = text2.get_rect()
    text2_rect.center = (400,410)
    input2_rect = pygame.Rect(200,200,0,0)
    befs = pygame.image.load('./image/befs.png')
    befs = pygame.transform.scale(befs,(130,130))
    befs_rect=befs.get_rect()
    befs_rect.center = (200,550)
    bfs = pygame.image.load('./image/bfs.png')
    bfs = pygame.transform.scale(bfs,(130,130))
    bfs_rect = befs.get_rect()
    bfs_rect.center = (600,550)
    befsdemo = pygame.image.load('./image/befsdemo.png')
    befsdemo = pygame.transform.scale(befsdemo,(130,130))
    befsdemo_rect = befsdemo.get_rect()
    befsdemo_rect.center = (65,550)
    bfsdemo = pygame.image.load('./image/bfsdemo.png')
    bfsdemo = pygame.transform.scale(bfsdemo,(130,130))
    bfsdemo_rect = bfsdemo.get_rect()
    bfsdemo_rect.center = (735,550)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color0 = color_passive
    color1 = color_passive
    color2 = color_passive
    active = [False,False,False]
    user_text0 = ''
    user_text1 = ''
    user_text2 = ''
    check1,check2=True,True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None,None,None,None,False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input0_rect.collidepoint(event.pos): active[0] = True
                else: active[0] = False
                if input1_rect.collidepoint(event.pos): active[1] = True
                else: active[1] = False
                if input2_rect.collidepoint(event.pos): active[2] = True
                else: active[2] = False
                if befs_rect.collidepoint(event.pos):
                    check1,check2 = True,True
                    if len(user_text1.split()) != int(user_text0): check1 = False
                    else: check1 = True
                    if len(user_text2.split()) != int(user_text0): check2 = False
                    else: check2 = True
                    if check1 and check2: return int(user_text0),list(map(int,user_text1.split())),list(map(int,user_text2.split())),0,True
                if bfs_rect.collidepoint(event.pos):
                    if len(user_text1.split()) != int(user_text0): check1 = False
                    else: check1 = True
                    if len(user_text2.split()) != int(user_text0): check2 = False
                    else: check2 = True
                    if check1 and check2: return int(user_text0),list(map(int,user_text1.split())),list(map(int,user_text2.split())),1,True
                if befsdemo_rect.collidepoint(event.pos):
                    if len(user_text1.split()) != int(user_text0): check1 = False
                    else: check1 = True
                    if len(user_text2.split()) != int(user_text0): check2 = False
                    else: check2 = True
                    if check1 and check2: return int(user_text0),list(map(int,user_text1.split())),list(map(int,user_text2.split())),2,True
                if bfsdemo_rect.collidepoint(event.pos):
                    if len(user_text1.split()) != int(user_text0): check1 = False
                    else: check1 = True
                    if len(user_text2.split()) != int(user_text0): check2 = False
                    else: check2 = True
                    if check1 and check2: return int(user_text0),list(map(int,user_text1.split())),list(map(int,user_text2.split())),4,True
            if event.type == pygame.KEYDOWN:
                if active[0]:
                    if event.key == pygame.K_RETURN: active[0] = False
                    elif event.key == pygame.K_BACKSPACE: user_text0 = user_text0[:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]:user_text0 += event.unicode
                elif active[1]:
                    if event.key == pygame.K_RETURN: active[1] = False
                    elif event.key == pygame.K_BACKSPACE: user_text1 = user_text1[:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_SPACE]:user_text1 += event.unicode
                elif active[2]:
                    if event.key == pygame.K_RETURN: active[2] = False
                    elif event.key == pygame.K_BACKSPACE: user_text2 = user_text2[:-1]
                    elif event.key in [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,pygame.K_SPACE]:user_text2 += event.unicode
        screen.fill((0, 0, 0))
        if not check1:
            error1 = font.render('Wrong number of inputs on column',True,(255,0,0))
            error1_rect = error1.get_rect()
            error1_rect.center = (400,370)
            screen.blit(error1,error1_rect)
        if not check2:
            error2 = font.render('Wrong number of inputs on row',True,(255,0,0))
            error2_rect = error2.get_rect()
            error2_rect.center = (400,500)
            screen.blit(error2,error2_rect)
        if active[0]: color0 = color_active
        else: color0 = color_passive
        if active[1]: color1 = color_active
        else: color1 = color_passive
        if active[2]: color2 = color_active
        else: color2 = color_passive
        pygame.draw.rect(screen, color0, input0_rect)
        text0_surface = font.render(user_text0, True, (255, 255, 255))
        screen.blit(text0_surface, input0_rect)
        input0_rect.w = max(50, text0_surface.get_width())
        input0_rect.h = text0_surface.get_height()
        input0_rect.center = (400,200)
        pygame.draw.rect(screen, color1, input1_rect)
        text1_surface = font.render(user_text1, True, (255, 255, 255))
        screen.blit(text1_surface, input1_rect)
        input1_rect.w = max(50, text1_surface.get_width())
        input1_rect.h = text1_surface.get_height()
        input1_rect.center = (400,330)
        pygame.draw.rect(screen, color2, input2_rect)
        text2_surface = font.render(user_text2, True, (255, 255, 255))
        screen.blit(text2_surface, input2_rect)
        input2_rect.w = max(50, text2_surface.get_width())
        input2_rect.h = text2_surface.get_height()
        input2_rect.center = (400,460)
        screen.blit(heading, heading_rect)
        screen.blit(text0, text0_rect)
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(befs, befs_rect)
        screen.blit(bfs, bfs_rect)
        screen.blit(befsdemo, befsdemo_rect)
        screen.blit(bfsdemo, bfsdemo_rect)
        pygame.display.flip()
def solution_page(size,solution):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font0 = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 32)
    heading = font0.render('Solution',True,(255,255,255))
    heading_rect=heading.get_rect()
    heading_rect.center = (400,50)
    home = pygame.image.load('./image/home.png')
    home = pygame.transform.scale(home,(130,130))
    home_rect = home.get_rect()
    home_rect.center = (65,550)
    quit = pygame.image.load('./image/quit.png')
    quit = pygame.transform.scale(quit,(130,130))
    quit_rect = quit.get_rect()
    quit_rect.center = (735,550)
    current_step = 0
    if len(solution)!=0:
        forward = pygame.image.load('./image/forward.png')
        forward = pygame.transform.scale(forward,(130,130))
        forward_rect = forward.get_rect()
        forward_rect.center = (735,300)
        backward = pygame.image.load('./image/backward.png')
        backward = pygame.transform.scale(backward,(130,130))
        backward_rect = forward.get_rect()
        backward_rect.center = (65,300)
        while True:
            screen.fill((0,0,0))
            surface = pygame.Surface((size*35,size*35))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if forward_rect.collidepoint(event.pos):
                        if current_step != len(solution)-1: current_step+=1
                    if backward_rect.collidepoint(event.pos):
                        if current_step != 0: current_step-=1
                    if home_rect.collidepoint(event.pos): return True
                    if quit_rect.collidepoint(event.pos): return False
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
            step_text = font.render('Position number '+str(current_step+1),True,(255,255,255))
            step_text_rect = step_text.get_rect()
            step_text_rect.center = (400,100)
            screen.blit(step_text,step_text_rect)
            surface = pygame.transform.scale(surface,(300,300))
            surface_rect=surface.get_rect()
            surface_rect.center = (400,350)
            if current_step != len(solution)-1: screen.blit(forward,forward_rect)
            if current_step != 0: screen.blit(backward,backward_rect)
            screen.blit(home, home_rect)
            screen.blit(quit, quit_rect)
            screen.blit(surface,surface_rect)
            pygame.display.flip()
    else:
        nosol = font.render("No solution is found",True,(255,255,255))
        nosol_rect = nosol.get_rect()
        nosol_rect.center = (400,300)
        screen.blit(nosol,nosol_rect)
        screen.blit(heading, heading_rect)
        screen.blit(home, home_rect)
        screen.blit(quit, quit_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if home_rect.collidepoint(event.pos): return True
                    if quit_rect.collidepoint(event.pos): return False
def demo_page(size,demo):
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Kukarasu Ultimate Solver')
    font0 = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 32)
    heading = font0.render('Visualization',True,(255,255,255))
    heading_rect=heading.get_rect()
    heading_rect.center = (400,50)
    home = pygame.image.load('./image/home.png')
    home = pygame.transform.scale(home,(130,130))
    home_rect = home.get_rect()
    home_rect.center = (65,550)
    quit = pygame.image.load('./image/quit.png')
    quit = pygame.transform.scale(quit,(130,130))
    quit_rect = quit.get_rect()
    quit_rect.center = (735,550)
    control_theme = pygame.image.load('./image/control.png')
    control_theme = pygame.transform.scale(control_theme,(130,130))
    control_theme_rect = control_theme.get_rect()
    control_theme_rect.center = (400,550)
    current_step = 0
    if len(demo)!=0:
        forward = pygame.image.load('./image/forward.png')
        forward = pygame.transform.scale(forward,(130,130))
        forward_rect = forward.get_rect()
        forward_rect.center = (735,300)
        backward = pygame.image.load('./image/backward.png')
        backward = pygame.transform.scale(backward,(130,130))
        backward_rect = forward.get_rect()
        backward_rect.center = (65,300)
        manual = True
        while True:
            screen.fill((0,0,0))
            surface = pygame.Surface((size*35,size*35))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if forward_rect.collidepoint(event.pos) and manual:
                        if current_step != len(demo)-1: current_step+=1
                    if backward_rect.collidepoint(event.pos) and manual:
                        if current_step != 0: current_step-=1
                    if control_theme_rect.collidepoint(event.pos):
                        manual = not manual
                    if home_rect.collidepoint(event.pos): return True
                    if quit_rect.collidepoint(event.pos): return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and manual:
                        if current_step != len(demo)-1: current_step+=1
                    if event.key == pygame.K_LEFT and manual:
                        if current_step != 0: current_step-=1
            screen.blit(control_theme, control_theme_rect)
            if manual:
                control = font.render('Auto',True,(0,0,0))
                control_rect = control.get_rect()
                control_rect.center = (400,550)
                screen.blit(control,control_rect)
            else:
                control = font.render('Manual',True,(0,0,0))
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
            step_text = font.render('Step number '+str(current_step+1),True,(255,255,255))
            step_text_rect = step_text.get_rect()
            step_text_rect.center = (400,100)
            screen.blit(step_text,step_text_rect)
            surface = pygame.transform.scale(surface,(300,300))
            surface_rect=surface.get_rect()
            surface_rect.center = (400,350)
            if current_step != len(demo)-1: screen.blit(forward,forward_rect)
            if current_step != 0: screen.blit(backward,backward_rect)
            screen.blit(home, home_rect)
            screen.blit(quit, quit_rect)
            screen.blit(surface,surface_rect)
            pygame.display.flip()
            if not manual: pygame.time.delay(min(int(10000/len(demo)),500))
def main():
    pygame.init()
    loop = True
    while loop:
        size,column,row,type,check = welcome_page()
        if not check: break
    print('Thanh you for using our solver!')
main()