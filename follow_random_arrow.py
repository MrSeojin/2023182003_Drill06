from pico2d import*
import random
import math

open_canvas()
back_ground = load_image('TUK_GROUND.png')
boy = load_image('my_character.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def goto_arrow():
    global boy_x, boy_y, direct
    length = math.sqrt( math.pow(arrow_x - 50 - boy_x, 2) + math.pow(arrow_y + 50 - boy_y, 2))
    if -10 < length < 10:
        boy_x = arrow_x - 50
        boy_y = arrow_y + 50
    else:
        boy_x += 10 * (arrow_x - 50 - boy_x) / length
        boy_y += 10 * (arrow_y + 50 - boy_y) / length

    if (arrow_x - 50 - boy_x)*(arrow_x - 50 - boy_x) < (arrow_y + 50 - boy_y)*(arrow_y + 50 - boy_y):
        if boy_y < arrow_y + 50:
            direct = 2
        elif boy_y > arrow_y + 50:
            direct = 3
    else:
        if boy_x < arrow_x - 50:
            direct = 0
        elif boy_x > arrow_x - 50:
            direct = 1

running = True
frame = 1
direct = 0
moving = False
size = 10
boy_x = random.randint(20, 780)
boy_y = random.randint(30,570)
arrow_x = random.randint(50, 750)
arrow_y = random.randint(50, 550)

while running:
    clear_canvas()
    back_ground.draw(400, 300, 800, 600)
    boy.clip_draw(frame * 135, direct * 200, 135, 200, boy_x, boy_y, 40, 6 * size)
    arrow.draw(arrow_x, arrow_y, 100, 100)
    update_canvas()
    handle_events()
    if arrow_x - 50 == boy_x and arrow_y + 50 == boy_y:
        arrow_x = random.randint(50, 750)
        arrow_y = random.randint(50, 550)
    else:
        goto_arrow()
    frame = (frame + 1) % 4
    delay(0.05)

close_canvas()