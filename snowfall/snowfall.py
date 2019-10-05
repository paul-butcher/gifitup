import sys
from PIL import Image
import numpy


def format_for_gifitup(img):
    """
    Make it small enough to conform to the gifitup rules (450px wide, < 2MB)
    """
    output_width = 400
    wpercent = (output_width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    return img.resize((output_width, hsize), Image.ANTIALIAS)


bg = format_for_gifitup(Image.open(sys.argv[1]))
fg = format_for_gifitup(Image.open(sys.argv[2]))
mask = format_for_gifitup(Image.open(sys.argv[3]).convert('1')) if len(sys.argv) > 3 else None
fgarray = numpy.array(fg)
size = bg.size


def create_frame(offsets, offset):
    pixel_offset = int(fg.size[1] * offset / offsets)
    frame_bg = bg.copy()
    frame_fg = Image.fromarray(numpy.roll(fgarray, pixel_offset, axis=0))
    frame_fg_positioned = Image.new('RGBA', size)
    frame_fg_positioned.paste(frame_fg, mask=mask)
    frame_bg.alpha_composite(frame_fg_positioned)
    return frame_bg


frames = [create_frame(10, offset) for offset in range(10)]

frames[0].save('snowfall.gif', format='GIF', append_images=frames[1:], save_all=True, duration=150, loop=0)