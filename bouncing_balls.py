import vpython as vp
import random

vp.scene.width = 800
vp.scene.height = 600

box_thickness = 0.2
box_size = 20
half_size = box_size / 2

vp.box(length=box_thickness, width=box_size, height=box_size, opacity=0.2, pos=vp.vector(half_size, 0, 0))
vp.box(length=box_thickness, width=box_size, height=box_size, opacity=0.2, pos=vp.vector(-half_size, 0, 0))
vp.box(length=box_size, width=box_size, height=box_thickness, opacity=0.2, pos=vp.vector(0, half_size, 0))
vp.box(length=box_size, width=box_size, height=box_thickness, opacity=0.2, pos=vp.vector(0, -half_size, 0))
vp.box(length=box_size, width=box_thickness, height=box_size, opacity=0.2, pos=vp.vector(0, 0, half_size))
vp.box(length=box_size, width=box_thickness, height=box_size, opacity=0.2, pos=vp.vector(0, 0, -half_size))

box_boundary = half_size - box_thickness / 2 - 1

ball_colors = [vp.color.red, vp.color.blue, vp.color.green]
rand_range_start = -box_boundary * 10
rand_range_end = box_boundary * 10


def make_pos():
    return random.randrange(rand_range_start, rand_range_end) / 10.0


def check_ball_bounds(ball, direction):
    ball.pos += direction
    if ball.pos.x >= box_boundary or ball.pos.x <= -box_boundary:
        direction.x = - direction.x
    if ball.pos.y >= box_boundary or ball.pos.y <= -box_boundary:
        direction.y = - direction.y
    if ball.pos.z >= box_boundary or ball.pos.z <= -box_boundary:
        direction.z = - direction.z


speed = 0.9
balls = [
    (
        vp.sphere(
            radius=1,
            color=random.choice(ball_colors),
            pos=vp.vector(make_pos(), make_pos(), make_pos())
        ),
        vp.vector(random.choice([speed, -speed]), random.choice([speed, -speed]), random.choice([speed, -speed]))
    )
    for n in range(139)
]


while True:
    vp.rate(40)
    for ball, direction in balls:
        check_ball_bounds(ball,direction)
