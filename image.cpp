#include <fstream>
#include "image.h"
using namespace std;

Image::Image(int width, int height)
{
  W = width;
  H = height;

  imgbuf = new char[W*H];

  

}

void Image::load(std::string& in_fname)
{
  ifstream ifp;
  ifp.open(in_fname.c_str(), ios::in|ios::binary);
  ifp.read(imgbuf, W*H*sizeof(char));
  if(ifp.fail())
  {
    cout << "Image " << in_fname << " read fail!" <<endl;
    exit(1);  
  }
  ifp.close();
}

void Image::write_raw(std::string& out_fname)
{
  ofstream ofp;
  ofp.open(out_fname.c_str(), ios::out|ios::binary);
  ofp.write(imgbuf, W*H*sizeof(char));
  if(ofp.fail())
  {
    cout << "Image " << out_fname << " write fail!" <<endl;
    exit(1);  
  }
  ofp.close();
}

void Image::invert()
{
  return;
}
