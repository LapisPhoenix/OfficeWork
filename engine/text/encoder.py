from PIL import Image
from numpy import array
from argparse import ArgumentParser
from io import BytesIO


class Encoder:
    def _sanitize_mapping(self, mapping: str) -> str:
        banned = ".;"
        for char in banned:
            mapping = mapping.replace(char, "")
        return mapping

    def encode(self, image: Image, width: int, height: int, mapping: list[str]) -> list[tuple[int, int, int, str]]:
        mapping = self._sanitize_mapping(mapping)
        image = image.convert("RGB")
        image = image.resize((width, height))

        data = []

        data.append(f"{width}.{height};")

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                intensity = (r + g + b) // 3
                char = mapping[intensity * len(mapping) // 256]
                data.append((r, g, b, char))
        return data

    def save(self, data: list[tuple[int, int, int, str]], output: str) -> None:
        with open(output, 'wb') as f:
            # Write header
            f.write(bytes(data[0], encoding="utf-8"))

            # Write pixel data
            for pixel in data[1:]:
                r, g, b, char = pixel
                f.write(bytes(f"{r}.{g}.{b}.{char};", encoding="utf-8"))

    def read(self, path: str) -> Image:
        return Image.open(path)

    def decode(self, input_file: str) -> list:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        header, *pixels = content.split(';')[:-1]
        width, height = map(int, header.split('.'))
        last_y = 0
        data = []
        for i, pixel in enumerate(pixels):
            # x = i % width
            y = i // width
            if y > last_y:
                    last_y  = y
                    print()
            r, g, b, character = pixel.split('.')
            data.append(f"\x1b[38;2;{r};{g};{b}m{character}\x1b[0m")
            print(f"\x1b[38;2;{r};{g};{b}m{character}\x1b[0m", end="")
        print()

        return data


if __name__ == "__main__":
    encoder = Encoder()
    parser = ArgumentParser(
        prog="Image Encoder",
        description="Encodes an image into RGB Ascii."
    )

    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input image.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to output image.")
    parser.add_argument("-m", "--mapping", type=str, required=False, help="Path to mapping file.", default="@%#*+=-:,_")
    parser.add_argument("-w", "--width", type=int, required=False, help="Width of output image.", default=50)
    parser.add_argument("-H", "--height", type=int, required=False, help="Height of output image.", default=30)
    parser.add_argument("-s", "--show", type=bool, required=False, help="Show output image.", default=False)
    args = parser.parse_args()

    base_image = encoder.read(args.input)
    data = encoder.encode(base_image, args.width, args.height, args.mapping)
    encoder.save(data, args.output)

    if args.show:
        encoder.decode(args.output)