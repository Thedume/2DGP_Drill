from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Smallball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(3, 10)
        self.move = True

    def update(self):
        if self.y >= 56 + 11 and self.move:
            self.y -= self.speed
        else:
            self.y = 67
            self.move = False

    def draw(self):
        self.image.draw(self.x, self.y)


class Bigball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(3, 10)
        self.move = True

    def update(self):
        if self.y >= 56 + 20 and self.move:
            self.y -= self.speed
        else:
            self.y = 76
            self.move = False

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global ball
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)
    team = [Boy() for _ in range(11)]
    world += team

    ball = [Bigball() if random.randint(0, 1) == 0 else Smallball() for _ in range(20)]
    world += ball
    # big = Bigball()
    # world.append(big)
    #
    # small = Smallball()
    # world.append(small)


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()

    delay(0.05)

# finalization code

close_canvas()
# fin
