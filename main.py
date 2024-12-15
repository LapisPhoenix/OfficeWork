from curses import wrapper
from officework.officework import OfficeWork


def main(screen):
    of = OfficeWork(screen)
    of.run()


if __name__ == '__main__':
    wrapper(main)
