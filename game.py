import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("사람만 잡아라!")

cong_img = pygame.image.load("images/cong.jpg")
cong_img = pygame.transform.scale(cong_img, (350, 500))

man_img = pygame.image.load("images/run.jpg")
man_img = pygame.transform.scale(man_img, (50, 50))

fifa_img = pygame.image.load("images/fifa.jpg")
fifa_img = pygame.transform.scale(fifa_img, (60, 60))

lol_img = pygame.image.load("images/lol.jpg")
lol_img = pygame.transform.scale(lol_img, (60, 60))

maple_img = pygame.image.load("images/maple.jpg")
maple_img = pygame.transform.scale(maple_img, (60, 60))

star_img = pygame.image.load("images/star.jpg")
star_img = pygame.transform.scale(star_img, (60, 60))

sudden_img = pygame.image.load("images/sudden.jpg")
sudden_img = pygame.transform.scale(sudden_img, (60, 60))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

vrx_pos = random.randint(25, screen_width - 25)
vry_pos = random.randint(25, screen_height - 25)

fifa_xpos = random.randint(25, screen_width - 25)
fifa_ypos = random.randint(25, screen_height - 25)

lol_xpos = random.randint(25, screen_width - 25)
lol_ypos = random.randint(25, screen_height - 25)

maple_xpos = random.randint(25, screen_width - 25)
maple_ypos = random.randint(25, screen_height - 25)

star_xpos = random.randint(25, screen_width - 25)
star_ypos = random.randint(25, screen_height - 25)

sudden_xpos = random.randint(25, screen_width - 25)
sudden_ypos = random.randint(25, screen_height - 25)

starttime = pygame.time.get_ticks()
gameduration = 15300


def xposypos(xpos, ypos):
    if xpos < 25:
        xpos = 25
    elif xpos > (screen_width - 25):
        xpos = screen_width - 25
    if ypos < 50:
        ypos = 50
    elif ypos > (screen_height - 25):
        ypos = screen_height - 25
    return xpos, ypos


score = 0


def ranmove(x, y):
    x += random.randint(-30, 30)
    y += random.randint(-30, 30)
    x += random.randint(-20, 20)
    y += random.randint(-20, 20)
    return x, y


def clickdistance(x, y):
    return ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5


def ranposition(xpos, ypos):
    xpos = random.randint(50, 750)
    ypos = random.randint(50, 550)
    return xpos, ypos


def scr_blit(x, y, img):
    screen.blit(
        img,
        (
            x - img.get_width() // 2,
            y - img.get_height() // 2,
        ),
    )


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            distance = clickdistance(vrx_pos, vry_pos)
            d2 = clickdistance(fifa_xpos, fifa_ypos)
            d3 = clickdistance(lol_xpos, lol_ypos)
            d4 = clickdistance(maple_xpos, maple_ypos)
            d5 = clickdistance(star_xpos, star_ypos)
            d6 = clickdistance(sudden_xpos, sudden_ypos)

            if distance <= 30:
                score += 5
                vrx_pos, vry_pos = ranposition(vrx_pos, vry_pos)
                if timeover // 1000 > 10:
                    score += 5

            if d2 <= 25:
                score -= 5
                fifa_xpos, fifa_ypos = ranposition(fifa_xpos, fifa_ypos)

            if d3 <= 25:
                score -= 5
                lol_xpos, lol_ypos = ranposition(lol_xpos, lol_ypos)

            if d4 <= 25:
                score -= 5
                maple_xpos, maple_ypos = ranposition(maple_xpos, maple_ypos)

            if d5 <= 25:
                score -= 5
                star_xpos, star_ypos = ranposition(star_xpos, star_ypos)

            if d6 <= 25:
                score -= 5
                sudden_xpos, sudden_ypos = ranposition(sudden_xpos, sudden_ypos)

    vrx_pos, vry_pos = ranmove(vrx_pos, vry_pos)
    fifa_xpos, fifa_ypos = ranmove(fifa_xpos, fifa_ypos)
    lol_xpos, lol_ypos = ranmove(lol_xpos, lol_ypos)
    maple_xpos, maple_ypos = ranmove(maple_xpos, maple_ypos)
    star_xpos, star_ypos = ranmove(star_xpos, star_ypos)
    sudden_xpos, sudden_ypos = ranmove(sudden_xpos, sudden_ypos)

    screen.fill(white)

    vrx_pos, vry_pos = xposypos(vrx_pos, vry_pos)
    fifa_xpos, fifa_ypos = xposypos(fifa_xpos, fifa_ypos)
    lol_xpos, lol_ypos = xposypos(lol_xpos, lol_ypos)
    maple_xpos, maple_ypos = xposypos(maple_xpos, maple_ypos)
    star_xpos, star_ypos = xposypos(star_xpos, star_ypos)
    sudden_xpos, sudden_ypos = xposypos(sudden_xpos, sudden_ypos)

    font = pygame.font.Font(None, 36)
    font2 = pygame.font.SysFont("undotum", 100)
    font3 = pygame.font.SysFont("undotum", 70)
    lastscore = font3.render(f"{score} 점", True, red)

    if score < 40:
        text = font.render(f"score : {score}", True, red)
    if score >= 40:
        text = font.render(f"score : {score}", True, green)
    timeover = pygame.time.get_ticks() - starttime
    if (timeover // 1000) <= 10:
        time_output = font.render(f" 15 / {timeover//1000}", True, blue)
    if (timeover // 1000) > 10:
        time_output = font.render(f" 15 / {timeover//1000}", True, red)
        fevertime = font.render(f"FEVER TIME!!", True, red)
        screen.blit(fevertime, (screen_width // 2 - 40, 30))

    screen.blit(text, (10, 10))
    screen.blit(time_output, (screen_width // 2 - 20, 10))

    scr_blit(vrx_pos, vry_pos, man_img)
    scr_blit(fifa_xpos, fifa_ypos, fifa_img)
    scr_blit(lol_xpos, lol_ypos, lol_img)
    scr_blit(maple_xpos, maple_ypos, maple_img)
    scr_blit(star_xpos, star_ypos, star_img)
    scr_blit(sudden_xpos, sudden_ypos, sudden_img)

    pygame.display.flip()
    pygame.time.delay(100)  # 100ms
    if timeover >= gameduration:
        screen.fill(black)
        running = False
        if score >= 60:
            scr_blit(screen_width // 2, screen_height // 2, cong_img)
            test_result = font2.render(f"축하합니다", True, blue)
            screen.blit(test_result, (screen_width // 5, screen_height - 200))
            screen.blit(lastscore, (screen_width // 2 - 50, 200))
        else:
            screen.fill(black)
            test_result = font2.render(f"불 합 격", True, red)
            screen.blit(test_result, (screen_width // 4, screen_height // 3))
            screen.blit(lastscore, (screen_width // 2 - 50, 100))

    if score >= 100:
        screen.fill(black)
        running = False
        scr_blit(screen_width // 2, screen_height // 2, cong_img)
        test_result = font2.render(f"만점입니다!", True, blue)
        screen.blit(test_result, (screen_width // 5, screen_height - 200))
        screen.blit(lastscore, (screen_width // 2 - 50, 200))

    if not running:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            pygame.time.delay(100)
