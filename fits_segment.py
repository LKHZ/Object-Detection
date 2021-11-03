from astropy.io import fits
import os

input = r"D:/A_Postgraduate/SKA_seg/2dbin_data_all/Denoise/"
file_list = os.listdir(input) #列出文件夹下所有的目录与文件

m=0
seg_size=600 #生成图片的尺寸

for i in range(0,len(file_list)):
    path = os.path.join(input,file_list[i])

    if not os.path.exists(path):
        print('file path not exist')

    elif os.path.isfile(path):
        filename = input + os.path.basename(path)

    HUDL = fits.open(filename)
    img = HUDL[0].data

    for i in range(seg_size,1286,seg_size):
        for j in range(seg_size ,1286 ,seg_size):
            new_img = img[j-seg_size:j,i-seg_size:i]
            HUDL[0].data = new_img
            m+=1
            HUDL.writeto(r"D:/A_Postgraduate/SKA_seg/segment600_600/adbin_data_denoise/" + "/" + '2dbin_data_denoise{}.fits'.format(m))

print("It's successful")
