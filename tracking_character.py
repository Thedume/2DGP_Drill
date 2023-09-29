from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
rand_x, rand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
frame = 0
running = True
hide_cursor()


while running:
    rand_x, rand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

    x1, y1 = x, y
    x2, y2 = rand_x, rand_y

    for i in range(1, 100 + 1):
        clear_canvas()

        TUK_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
        hand.draw_now(rand_x, rand_y)

        if rand_x > x:
            character.clip_draw(100 * frame, 100, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

        update_canvas()

        frame = (frame + 1) % 8

        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        delay(0.05)


close_canvas()
