import qrlib
from PIL import Image
import cairosvg
from io import BytesIO

text = 'rebeka hi'

one_qr = qrlib.generate_custom_qr_file(text, language='en', qr_format='PNG',
                 size='1000', ec_level='H', instructions=False,
                 style='sieve', style_color='#000000',
                 inner_eye_style='leaf', inner_eye_color='#000000',
                 outer_eye_style='left_eye', outer_eye_color='#000000',
                 bg_color='#FFFFFF')

qr = Image.open(one_qr).convert('RGBA')


file_o = open('tippy.svg')

out = BytesIO()
cairosvg.svg2png(file_obj=file_o, write_to=out)
image = Image.open(out).convert('RGBA').resize((250, 150))

qr.paste(image, (380, 410), image)
qr.show()