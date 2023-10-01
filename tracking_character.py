from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global x, y
    global click_x, click_y
    global pointList

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            pointList.append([event.x, TUK_HEIGHT - event.y])


x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
click_x, click_y = 0, 0
pointList = []

frame = 0
running = True


while running:
    handle_events()
    if len(pointList) > 0:
        x1, y1 = x, y
        x2, y2 = pointList[0][0], pointList[0][1]

        for i in range(1, 100 + 1):
            clear_canvas()

            TUK_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
            hand.draw_now(click_x, click_y)

            if x2 > x:
                character.clip_draw(100 * frame, 100, 100, 100, x, y)
            else:
                character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

            update_canvas()

            frame = (frame + 1) % 8

            t = i / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2

            delay(0.05)
        pointList.pop(0)
    else:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()

        frame = (frame + 1) % 8

close_canvas()
