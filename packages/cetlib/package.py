from spack import *

class Cetlib(Package):
    homepage = "https://github.com/drbenmorgan/fnal-cetlib.git"

    version("dev", git="https://github.com/drbenmorgan/fnal-cetlib.git", branch="feature/modern-cmake")

    depends_on("cmake@3.3:")
    depends_on("cetbuildtools2")
    depends_on("boost@1.60:")
    depends_on("doxygen@1.8:")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

