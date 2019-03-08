import PIL
from PIL import Image

im = Image.open('./video/[insert directory here]/deepfake/deepfake.gif')

def iter_frames(im):
    try:
        i = 0
        while 1:
            im.seek(i)
            im.frame = im.copy()
            if i == 0:
                palette = im.frame.getpalette()
            else:
                im.frame.putpalette(palette)
            yield im.frame
            i += 1
    except EOFError:
        pass

for i, frame in enumerate(iter_frames(im)):
    frame.save('./deepfake/[insert directory here]/frames/fake0%d.png' % i, **frame.info)
