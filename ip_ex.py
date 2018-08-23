from PIL import Image
import os

# configurable param starts#
img_name = 'brick-house';
img_format = 'png';
source = 'ip_ex.cpp image.cpp';
exe_name = 'ip_exercise';
# configurable param ends #

in_name = img_name + '.'+img_format;
in_raw_name = img_name + '.raw';
out_raw_name = img_name + '_out.raw'
cfg_name = img_name + '.cfg';

#create grayscale raw from input 
in_img_gs = Image.open(in_name).convert('L');
(w,h) = in_img_gs.size;

with open(in_raw_name, 'w+b') as fout:
  for i in range(h):
    for j in range(w):
      pv = in_img_gs.getpixel((j,i));
      fout.write(bytearray([pv]));

#prepare config file
cfgFile = open(cfg_name, 'w');
cfgFile.write('')
with open(cfg_name, 'w') as cfgFile:
  cfgFile.write('InputRawWidth' '\n');
  cfgFile.write( str(w) + '\n');
  cfgFile.write('InputRawHeight' + '\n');
  cfgFile.write( str(h) + '\n');
  cfgFile.write('InputRawFile' + '\n');
  cfgFile.write( in_raw_name + '\n');
  cfgFile.write('OutputRawFile' + '\n');
  cfgFile.write(out_raw_name + '\n');

#compile image process program
os.system('g++ ' + source + ' -o '+ exe_name);

#run image process exe
#>>./exe cfg_name
os.system('./'+exe_name+' ' + cfg_name);

#convert raw output back to png
#TODO 
