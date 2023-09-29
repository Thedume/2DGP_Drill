from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
running = True

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)

    character.clip_draw(100 * frame, 100, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    x = x + 1

    delay(0.01)


close_canvas()