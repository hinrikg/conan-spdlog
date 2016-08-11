from conans import ConanFile
from conans.tools import get


class SpdlogConan(ConanFile):
    name = 'spdlog'
    version = '0.9.0'
    author = 'Hinrik Gylfason (hinrikg@gmail.com)'
    url = 'http://github.com/hinrikg/conan-spdlog'
    license = 'MIT'

    settings = None
    generators = 'cmake'

    def source(self):
        get('https://github.com/gabime/spdlog/archive/v0.9.0.zip')

    def package(self):
        self.copy('*.h', dst='include', src='spdlog-0.9.0/include', keep_path=True)
        self.copy('*.cc', dst='include', src='spdlog-0.9.0/include', keep_path=True)
        self.copy('LICENSE', dst='.', src='spdlog-0.9.0')
