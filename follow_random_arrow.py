from pico2d import*

open_canvas()
back_ground = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

running = True

while running:
    clear_canvas()
    back_ground.draw(400, 300, 800, 600)
    boy.clip_draw(0, 0, 100, 100, 300, 400, 40, 60)
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()