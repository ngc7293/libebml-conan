#include <iostream>

#include <ebml/EbmlVersion.h>

int main(int argc, const char* argv[])
{
    const std::string expected = "1.4.2";

    if (libebml::EbmlCodeVersion != expected) {
        std::cerr << "Invalid EbmlCodeVersion (expected '" << expected << "' got '" << libebml::EbmlCodeVersion << "')" << std::endl;
        return -1;
    }
}
