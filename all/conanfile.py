from conan import ConanFile
from conan.tools.files import copy, get
import os
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get



class ConfuAlgorithm(ConanFile):
    name = "confu_algorithm"
    license = "BSL-1.0"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def requirements(self):
        self.requires("boost/1.86.0")

    def layout(self):
        cmake_layout(self, src_folder=self.name+"-"+str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.components[self.name].requires = ["boost::headers"]
