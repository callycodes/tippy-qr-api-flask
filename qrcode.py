import qrlib
from PIL import Image
import cairosvg
from io import BytesIO
import base64

def createQR(url, style, colour, inner_eye_style, inner_eye_colour, outer_eye_style, outer_eye_colour, bg_colour):
  one_qr = qrlib.generate_custom_qr_file(url, language='en', qr_format='PNG',
                  size='1000', ec_level='H', instructions=False,
                  style=style, style_color='#' + colour,
                  inner_eye_style=inner_eye_style, inner_eye_color='#' + inner_eye_colour,
                  outer_eye_style=outer_eye_style, outer_eye_color='#' + outer_eye_colour,
                  bg_color='#' + bg_colour)

  qr = Image.open(one_qr).convert('RGBA')

  file_o = open('tippy.svg')

  out = BytesIO()
  cairosvg.svg2png(file_obj=file_o, write_to=out)
  image = Image.open(out).convert('RGBA').resize((250, 150))

  qr.paste(image, (380, 410), image)
  byte_arr = BytesIO()
  qr.save(byte_arr, format='PNG')
  
  out = "data:image/png;base64," + base64.b64encode(byte_arr.getvalue()).decode('ascii')
  return out