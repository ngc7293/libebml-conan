from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class LibebmlConan(ConanFile):
    name = "libebml"
    version = "1.4.2"
    license = "LGPL-2.1"
    author = "David Bourgault contact@davidbourgault.ca"
    url = "https://github.com/ngc7293/libebml-conan.git"
    description = "A C++ libary to parse EBML files "
    topics = ("ebml", "matroska")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.compiler == 'gcc' and self.settings.compiler.libcxx == 'libstdc++':
            raise ConanInvalidConfiguration('This library requires the new GCC C++11 ABI')

        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/Matroska-Org/libebml.git --branch release-1.4.2 --depth=1")
        tools.replace_in_file('libebml/CMakeLists.txt')

    def build(self):
        cmake = CMake(self)
        cmake.definitions['DISABLE_PKGCONFIG'] = 'Yes'
        cmake.configure(source_folder="libebml")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libebml.a"] if not self.options.shared else ['libebml.so']

