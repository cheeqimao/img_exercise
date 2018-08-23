from PIL import Image
import numpy as np 
import sys,getopt,os

# configurable param starts#
source = 'ip_ex.cpp image.cpp';
exe_name = 'ip_exercise';
# configurable param ends #


scpt_name = 'ip_ex.py';
img_name = '';
img_format = '';
compileFlag = 'false';

def usage():
  print scpt_name + ' -n <filename> -t <filetype i.e png> -c <compile cpp program  if true>'
  
try:
  opts, args = getopt.getopt(sys.argv[1:], "n:t:c:", ["name=","type=","compile="]);
except getopt.GetoptError:
  usage();
  sys.exit(2);
print opts;
for opt, arg in opts:
  if opt in ('-n',"--name"):
    img_name = arg;
  elif opt in ('-t', "--type"):
    img_format = arg;
  elif opt in ('-c', "--compile"):
    compileFlag = arg;
  else:
    usage();
    sys.exit(2);

print 'img name: ' + img_name;
print 'img type: ' + img_format;
print 'compile code? (true/false): ' + compileFlag;

in_name = img_name + '.'+img_format;
in_raw_name = img_name + '.raw';
out_raw_name = img_name + '_out.raw'
out_name = img_name + '_out.' + img_format; 
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
if compileFlag=='true':
  print 'compile program!!'
  os.system('g++ ' + source + ' -o '+ exe_name);

#run image process exe
#>>./exe cfg_name
os.system('./'+exe_name+' ' + cfg_name);

#convert raw output back to png
out_raw_array = np.fromfile(out_raw_name, dtype=np.uint8, count=(w*h));
out_raw_array = np.reshape(out_raw_array, (h,w));
out_img = Image.fromarray(out_raw_array);
out_img.save(out_name);

