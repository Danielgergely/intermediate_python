"""Meme generator class"""

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """Creates an image with a quote."""

    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def make_meme(self, source_img, text: str, author: str, width=500) -> str:
        """Creates an image with a quote on it."""
        try:
            with Image.open(source_img) as image:
                image = resize_image(image, width)
                image = add_caption(image, text, author)
                path = f'{self.output_dir}/img.png'
                image.save(path)
            return path
        except:
            raise


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


def add_caption(img: Image, text: str, author: str):
    """Adds a caption to an image."""

    try:
        message = f'"{text}" - {author}'
        text = Image.new("RGBA", img.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", 20)
        caption = ImageDraw.Draw(text)

        caption.text((10, 10), message, font=fnt, fill=(0, 0, 0, 255))

        img = img.convert("RGBA")
        return Image.alpha_composite(img, text)
    except Exception:
        raise Exception("Something went wrong while captioning image") from None
