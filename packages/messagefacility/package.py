from spack import *

class Messagefacility(Package):
    homepage = "https://github.com/drbenmorgan/fnal-messagefacility.git"

    version("dev", git="https://github.com/drbenmorgan/fnal-messagefacility.git", branch="feature/modern-cmake")

    depends_on("cmake@3.3:")
    depends_on("cetbuildtools2")
    depends_on("boost@1.60:")
    depends_on("doxygen@1.8:")
    depends_on("cetlib@dev:")
    depends_on("fhicl-cpp@dev:")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "-DBUILD_TESTING=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

