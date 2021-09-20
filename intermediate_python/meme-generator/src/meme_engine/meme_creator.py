"""Meme generator class"""

from PIL import Image, ImageFont, ImageDraw
import random
import textwrap
from pathlib import Path
import os


class MemeEngine:
    """Creates an image with a quote."""
    _font: Path

    def __init__(self, output_dir: str, font: Path):
        self.output_dir = output_dir
        self._font = font

    def make_meme(self, source_img, text: str, author: str, width=500) -> str:
        """Creates an image with a quote on it."""
        try:
            with Image.open(source_img) as image:
                image = self.resize_image(image, width)
                image = self.add_caption(image, text, author)
                path = Path(f'{self.output_dir}/{random.randint(0, 100000000)}.png')
                if not path.parent.exists():
                    os.makedirs(path.parent)
                image.save(path)
            return str(path)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def resize_image(img: Image, new_width: int):
        """Resizes the image according to the given proportions"""

        try:
            width, height = img.size
            proportions = (new_width / (float(width)))
            new_height = (float(height) * float(proportions))
            img = img.resize((new_width, int(new_height)))
            return img
        except Exception:
            raise Exception("Something went wrong while resizing image") from None

    def add_caption(self, img: Image, text: str, author: str):
        """Adds a caption to an image."""

        try:
            caption = "\n".join(textwrap.wrap(text, width=50))
            message = f'{caption} \n         - {author}'
            text = Image.new("RGBA", img.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype(str(self._font), 20)
            caption = ImageDraw.Draw(text)

            caption.text((10, 10), message, font=fnt, fill=(0, 0, 0, 255))

            img = img.convert("RGBA")
            return Image.alpha_composite(img, text)
        except Exception as e:
            raise Exception(f"Something went wrong while captioning image, exception was {str(e)}") from None
