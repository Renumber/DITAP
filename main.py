from PIL import Image
import numpy as np

im = Image.open('super.bmp')
print(im.format, im.size, im.mode)
pix = np.array(im)
print(pix.shape)
pix = pix / 255
print(pix[:10])

f = open("test.asm", 'w')
f.write("@SCREEN\n")
f.write("D=A\n")
f.write("@i\n")
f.write("M=D\n")
mcnt = 0
for row in pix:
    cnt = 0
    num = 0
    for cell in row:
        if cell[0] == 0:
            num += 2**(cnt)
        if cnt == 15:
            if num != 0:
                f.write("@"+str(mcnt)+"\n")
                f.write("D=A\n")
                f.write("@i\n")
                f.write("M=M+D\n")
                if num >= 2 ** 15:
                    print(num)
                    num = (2**16 - 1) - num + 1;
                    f.write("@" + str(num) + "\n")
                    f.write("D=-A\n")
                    print(num)
                else:
                    f.write("@"+str(num)+"\n")
                    f.write("D=A\n")
                f.write("@i\n")
                f.write("A=M\n")
                f.write("M=D\n")
                mcnt = 1
            else:
                mcnt += 1
            num = 0
            cnt = 0
        else:
            cnt += 1

f.close()