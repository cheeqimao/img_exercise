#ifndef CONFIG_READER_H
#define CONFIG_READER_H

#include <map>
#include <iostream>

class ConfigReader
{
public:
    ConfigReader(std::string& in_file_path)
        : src_path(in_file_path)
    {
        const char* ifname = in_file_path.c_str();
        FILE* fp = fopen(ifname, "r");
        if (NULL == fp)
        {
            throw std::string("Error opening config file: " + in_file_path); 
        }

        char key[512];
        char value[512];

        while (EOF != fscanf(fp, "%s", key) &&
            EOF != fscanf(fp, "%s", value) )
        {
            Add(std::string(key), std::string(value));
        }
        fclose(fp);
    }


    std::string Get(std::string& in_key)
    {
		std::map<std::string, std::string>::iterator iter = m_map.find(in_key);
		if (iter != m_map.end())
		{
			return iter->second;
		}
		else
		{
			throw std::string("cannot find requested key: "+in_key);
		}
    }

    std::string Get(const char* in_key)
    {
        std::string k(in_key);
        return Get(k);
    }

    int32_t GetInt(const char* in_key)
    {
        std::string s = Get(in_key);
        return atoi(s.c_str());
        // const char* t = s.c_str()
        // return atoi(t);
    }

    void Print()
    {
        std::cerr << "========================" << std::endl;
        std::cerr << "Config file " << src_path << " content: " << std::endl;

		for (std::map<std::string, std::string>::iterator iter = m_map.begin(); iter!=m_map.end(); iter++)
        {
            std::cerr << iter->first << " | " << iter->second << std::endl;
        }
        std::cerr << std::endl << "========================" << std::endl;
    }

private:
    void Add(const std::string& key, const std::string& value)
    {
        m_map.insert(std::pair<std::string, std::string>(key, value));
        std::cout << key << "," << value << std::endl;
    }

private:
    std::map<std::string, std::string> m_map;
    std::string src_path;
};

#endif
