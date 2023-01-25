import sys, pygame
from pygame.locals import*

vertices_3D = [(2,2,2),
(2,1,2),
(1,1,2),
(1,2,2),
(2,2,1),
(2,1,1),
(1,1,1),
(1,2,1)]

edge_table = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]


width = 1000
height = 500
screen_color = (49, 150, 100)
line_color = (255, 0, 0)
focal_length = 10
vertices_2D = []
for i in vertices_3D:
    x = i[0] * (focal_length/(focal_length+i[2]))
    y = i[1] * (focal_length/(focal_length+i[2]))
    vertices_2D.append((x,y))

vertices_2D = [(x*100,y*100) for x,y in vertices_2D]
print(vertices_2D)
# vertices_2D = [(2,2),(2,1),(1,2)]





def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    pygame.display.flip()
    for i in edge_table:
        # print(i[0],i[1])
        # print(vertices_2D[i[0]])
        pygame.draw.line(screen, line_color, vertices_2D[i[0]],vertices_2D[i[1]])
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
main()