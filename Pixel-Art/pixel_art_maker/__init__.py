import sys
import os
import pygame

package_directory = os.path.dirname(os.path.abspath(__file__))


class PixelArtMaker:
    pixel_size = 25  # every "pixel" in the created pixel art is 25x25 px

    @classmethod
    def make_my_pixel_art(cls, title, data):
        pygame.init()

        try:
            picture = pygame.display.set_mode([cls.pixel_size * len(data[0]),
                                               cls.pixel_size * len(data)])
            pygame.display.set_caption(title)

            cls.__draw_data(picture, data)

            pygame.display.update()
            pygame.image.save(picture, "{}.jpeg".format(
                ''.join(c for c in title if c.isalnum())))
        except:
            r = pygame.Color("#fd7a3d")
            w = pygame.Color("#ffffff")

            data = [
                [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                [w, w, r, r, r, w, r, w, r, w, w, w, r, w, w, r, w, r, r, r, w, w, r, w, w],
                [w, w, r, w, r, w, r, w, r, w, w, w, r, r, w, r, w, r, w, r, w, w, r, w, w],
                [w, w, r, w, r, w, r, r, r, w, w, w, r, w, r, r, w, r, w, r, w, w, r, w, w],
                [w, w, r, w, r, w, r, w, r, w, w, w, r, w, r, r, w, r, w, r, w, w, w, w, w],
                [w, w, r, r, r, w, r, w, r, w, w, w, r, w, w, r, w, r, r, r, w, w, r, w, w],
                [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]
            ]

            picture = pygame.display.set_mode(
                [cls.pixel_size * len(data[0]),
                 cls.pixel_size * len(data) + 200])
            pygame.display.set_caption('Someting went wrong :(')
            picture.fill(pygame.Color("white"))

            cls.__draw_data(picture, data)

            font = pygame.font.Font(
                os.path.join(package_directory, 'fonts', 'calibri.ttf'),
                16)
            text = "Something went wrong.\n" \
                   "Check if your code is correct and try again!"
            for i, l in enumerate(text.splitlines()):
                picture.blit(font.render(l, 0, pygame.Color("black")),
                             (2 * cls.pixel_size,
                              20 + len(data) * cls.pixel_size +
                             font.get_linesize() * i))

            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    @classmethod
    def __draw_data(cls, picture, data):
        for y, row in enumerate(data):
            for x, colour in enumerate(row):
                rect = pygame.Rect(x * cls.pixel_size, y * cls.pixel_size,
                                   cls.pixel_size, cls.pixel_size)
                picture.fill(colour, rect=rect)
