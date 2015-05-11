import fabric
import fabric.api


def build():
    fabric.api.local('jekyll build --config _config.yml')


def serve():
    fabric.api.local('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')
