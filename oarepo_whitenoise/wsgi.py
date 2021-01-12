import os

from oarepo_micro_api.wsgi import application as application
from whitenoise import WhiteNoise
from whitenoise.string_utils import decode_path_info

static_folder = os.environ.get('WHITENOISE_ROOT', '/whitenoise')

assert os.path.exists(static_folder)


class IndexWhiteNoise(WhiteNoise):

    def find_file(self, url):
        print('Looking for url', url)
        if url.startswith('/api'):
            return None
        ret = super(IndexWhiteNoise, self).find_file(url)
        if not ret:
            ret = super(IndexWhiteNoise, self).find_file('/index.html')
        return ret

    def __call__(self, environ, start_response):
        path = decode_path_info(environ.get("PATH_INFO", ""))
        print('serving path', path)
        if path.startswith('/api'):
            return self.application(environ, start_response)

        if self.autorefresh:
            static_file = self.find_file(path)
        else:
            static_file = self.files.get(path)
        if static_file is None:
            if self.autorefresh:
                static_file = self.find_file('/index.html')
            else:
                static_file = self.files.get('/index.html')

        return self.serve(static_file, environ, start_response)

application.wsgi_app = IndexWhiteNoise(application.wsgi_app, root=static_folder)
