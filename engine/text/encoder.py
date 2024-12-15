import struct
from PIL import Image
from argparse import ArgumentParser
from io import BytesIO


class Encoder:
    def encode(self, image: Image, width: int, height: int, verbose: bool = False) -> BytesIO:
        image = image.convert("RGB")
        image = image.resize((width, height))

        final_image = BytesIO()

        header = struct.pack(">HH", width, height)
        final_image.write(header)

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                intensity = (r + g + b) // 3
                pixel = struct.pack(">HHHH", r, g, b, intensity)
                final_image.write(pixel)

        return final_image

    def decode(self, input_file: str, mapping: str):
        with open(input_file, 'rb') as f:
            header = f.read(4)
            width, height = struct.unpack(">HH", header)
            x = 0
            line = []

            # TODO: Add this to a separate render class
            while pixel := f.read(8):
                if x >= width:
                    # Reset
                    x = 0
                    print(''.join(line))
                    line = []

                r, g, b, i = struct.unpack(">HHHH", pixel)  # RGBI (Intensity)
                char = mapping[i * len(mapping) // 256]

                yield r, g, b, char
                x += 1

    def save(self, data: BytesIO, output: str) -> None:
        with open(output, 'wb') as f:
            f.write(data.getbuffer())

    def read(self, path: str) -> Image:
        return Image.open(path)


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
    parser.add_argument("-v", "--verbose", type=bool, required=False, help="Print Extra Information", default=False)
    args = parser.parse_args()

    if args.width > 255 or args.height > 255:
        print("Sorry, max size supported is 255x255.")
        exit()

    base_image = encoder.read(args.input)
    data = encoder.encode(base_image, args.width, args.height, args.verbose)
    encoder.save(data, args.output)

    if args.show:
        encoder.decode(args.output, args.mapping)

    # Target res:
    # 144x28
    # image:
    # 31x16
    # (2, 2)