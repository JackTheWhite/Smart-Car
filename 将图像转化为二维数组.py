from PIL import Image
from pylab import *
import re
##from skimage import io,data,color
def write_into_files(imarray):
    imstring=''
    for i in imarray:
        imstring+=str(i)
        imstring+='\n'
    f = open('C:\\Users\\Jack\\Desktop\\write.txt', 'w')
    f.write(imstring)

def turn_graph_into_binery():
    im=Image.open('C:\\Users\\Jack\\Pictures\\TIM图片20171208230246.jpg').convert('L')
    im_name=Image.open('C:\\Users\\Jack\\Pictures\\二值化补线图像\\出十字.jpg')
##    img=io.imread(img_name,as_grey=False)
##    img_gray=color.rgb2gray(img)
    imarray=array((im_name).convert('L'))
    imarray2=array(im)
##    print(imarray[:1])
##    print(imarray.shape)
##    print(imarray.dtype)
    print(len(imarray2[:1]))
    print(imarray2.shape)
    print(imarray2.dtype)
##    imarray.save('C:\\Users\\Jack\\Pictures\\灰度图\\a.jpg')
##    write_into_files(imarray)
turn_graph_into_binery()
