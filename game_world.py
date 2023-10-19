
# 2개의 layer를 갖는 게임월드로 구현
objects = [[], []]


def add_object(o, depth):
    objects[depth].append(o)


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError("없다")