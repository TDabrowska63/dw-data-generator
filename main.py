from generator import Generator
from generate_csv.create_zgloszenia import generate_zgloszenia


def main():

    generate_zgloszenia(300)
    generator = Generator()


if __name__ == '__main__':
    main()
