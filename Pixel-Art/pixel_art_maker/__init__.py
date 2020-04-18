import sys
import os
import pygame

package_directory = os.path.dirname(os.path.abspath(__file__))


class PixelArtMaker:
    @classmethod
    def make_my_pixel_art(cls, title, data):
        pixel_size = 25  # every "pixel" in the created pixel art is 25x25 px
        pygame.init()

        try:
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
        except:
            cls.__display_error_message("Something went wrong.\n"
                                        "Check if your code is correct and "
                                        "try again!")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    @classmethod
    def __display_error_message(cls, text):
        pygame.init()
        window = pygame.display.set_mode([400, 400])
        pygame.display.set_caption('Someting went wrong :(')
        window.fill(pygame.Color("white"))
        header_font = pygame.font.Font(
            os.path.join(package_directory, 'fonts', 'mousie', 'Mousie.ttf'),
            60)
        text_font = pygame.font.Font(
            os.path.join(package_directory, 'fonts', 'calibri', 'calibri.ttf'),
            16)

        window.blit(header_font.render("Oh no", 0, pygame.Color("black")),
                    (10, 10))
        for i, l in enumerate(text.splitlines()):
            window.blit(text_font.render(l, 0, pygame.Color("black")),
                        (10, 20 + header_font.get_linesize() +
                         text_font.get_linesize() * i))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
