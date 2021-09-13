from PIL import Image, ImageFont, ImageDraw


def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """

    with Image.open(in_path) as im:
        width, height = im.size
        left = 450
        top = 900
        right = 850
        bottom = 1275
        im_crop = im.crop((left, top, right, bottom))
        width, height = im_crop.size
        im_resize = im_crop.resize((width*2, height*2))

        txt = Image.new("RGBA", im_resize.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", 40)
        d = ImageDraw.Draw(txt)

        d.text((10,10), message, font=fnt, fill=(0, 0, 0, 255))

        im_resize = im_resize.convert("RGBA")
        out = Image.alpha_composite(im_resize, txt)

        out.save(out_path)
        a = 10
    raise Exception('generate_postcard not implemented')


if __name__ == '__main__':
    print(generate_postcard('./imgs/img.jpg', './imgs/cropped_img.png', message="This is a cute dog"))
