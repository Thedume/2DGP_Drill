from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dirX, dirY

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirX, dirY = 0, 0
frame = 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if 50 <= x <= TUK_WIDTH-50:
        x += dirX * 10
    else:
        if (50 > x and dirX == 1) or (x > TUK_WIDTH-50 and dirX == -1):
            x += dirX * 10
    if 50 <= y <= TUK_HEIGHT-50:
        y += dirY * 10
    else:
        if (50 > y and dirY == 1) or (y > TUK_HEIGHT-50 and dirY == -1):
            y += dirY * 10


    delay(0.05)

close_canvas()
