from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
from conan.tools.microsoft import is_msvc
from conan.tools.scm import Version
import os


class ConfuAlgorithm(ConanFile):
    name = "confu_algorithm"
    license = "BSL-1.0"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True


    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)


    def package(self):
        copy(self, "*.h*", src=os.path.join(self.source_folder, "confu_algorithm"),
             dst=os.path.join(self.package_folder, "include", "confu_algorithm"))

