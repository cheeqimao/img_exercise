#ifndef IMAGE_H
#define IMAGE_H

#include <iostream>

class Image
{
  public:
    Image(int weigth, int height);
    ~Image(){};
    
    void load(std::string& in_fname);
    void invert();
    void write_raw(std::string& out_fname);
  private:
    int W;
    int H;
    char * imgbuf;
};

#endif
