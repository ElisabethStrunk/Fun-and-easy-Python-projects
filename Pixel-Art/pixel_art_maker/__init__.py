import sys
import pygame


class PixelArtMaker:
    @classmethod
    def make_my_pixel_art(cls, title, data):

        pixel_size = 25  # every "pixel" in the created pixel art is 25x25 px
        pygame.init()
        picture = pygame.display.set_mode([pixel_size * len(data[0]),
                                           pixel_size * len(data)])

        for y, row in enumerate(data):
            for x, colour in enumerate(row):
                rect = pygame.Rect(x * pixel_size, y * pixel_size,
                                   pixel_size, pixel_size)
                picture.fill(colour, rect=rect)

        pygame.display.set_caption(title)
        pygame.display.update()
        pygame.image.save(picture, "{}.jpeg".format(
            ''.join(c for c in title if c.isalnum())))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
