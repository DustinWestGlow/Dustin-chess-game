mousedown = False
flag = False
while True:
    mousedown = pygame.MOUSEBUTTONDOWN
    if mousedown and not flag:
        do_action()
        flag = True
    if not mousedown