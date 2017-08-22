import os
import random
import string

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

password_length = 50
chars = string.ascii_letters + string.digits  # + '!@#$%^&*()'


# TODO: this generation method is NOT cryptographically secure
def generate_password(length=10, charset=string.ascii_letters + string.digits):
    random.seed = (os.urandom(1024))

    return ''.join(random.choice(charset) for _ in xrange(length))


def generate_png(text, padding=10):
    font = ImageFont.truetype("Verdana.ttf", 15)
    # calculate size of image
    text_width, text_height = font.getsize(text)
    img = Image.new('RGB', (text_width + padding, text_height + padding), color='white')
    d = ImageDraw.Draw(img)
    d.text((padding / 2, padding / 2), password, font=font, fill='black')
    img.save('password.png', 'png')


password = generate_password(length=password_length, charset=chars)
print password
generate_png(text=password)
