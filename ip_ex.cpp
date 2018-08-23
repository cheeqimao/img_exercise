#include "image.h"
#include "configReader.h"
using namespace std;

int main(int argc, char *argv[])
{
  if(argc < 2)
  {
    cout << "invalid param!" <<endl;
    cout << "usage: >>./ip_ex configFile" <<endl;
    return 0;
  }
  
  std::string config_file_path(argv[1]);
  ConfigReader cfg(config_file_path);
  
  cout << "cfg file loaded" << endl;
  const int32_t raw_width = cfg.GetInt("InputRawWidth");
  const int32_t raw_height = cfg.GetInt("InputRawHeight");
  std::string in_fname = cfg.Get("InputRawFile");
  std::string out_fname = cfg.Get("OutputRawFile");

  cout << "before img" << endl;
  
  Image img(raw_width, raw_height);

  img.load(in_fname);
  
  //image manipulation goes here:
  img.invert();

  img.write_raw(out_fname);
}
