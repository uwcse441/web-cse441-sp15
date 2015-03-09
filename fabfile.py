import fabric
import fabric.api

# For now, we'll specify host/user interactively.
#
# Run `fab deploy`, you'll be prompted for a host string.
#
# Enter a string like `jfogarty@barb.cs.washington.edu`


def build():
    fabric.api.local('jekyll build --config _config.yml')


def deploy():
    # Locally build the website
    fabric.api.local('jekyll build --config _config.yml')

    # Ensure the server has our staging directory
    fabric.api.run('mkdir -p ~/fabric_staging/web-cse441-sp15/')

    # Ensure the staging directory is empty
    fabric.api.run('rm -rf ~/fabric_staging/web-cse441-sp15/*')

    # Push up to the server staging directory
    fabric.api.put('_site/*', '~/fabric_staging/web-cse441-sp15/')

    # And sync into the deployment directory
    fabric.api.run('rsync -r -c --delete ~/fabric_staging/web-cse441-sp15/ /cse/web/courses/cse441/15sp/')

    # Set group write permissions
    fabric.api.run('chmod -R g+w /cse/web/courses/cse441/15sp/')


def serve():
    fabric.api.local('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')


# We cannot have a test because Fabric requires Python 2.7 but our tests use Python 3.4.
# It might be possible to fix this by moving to invoke, the Python 3 descendant of Fabric.
#
# def test():
#    fabric.api.local('nosetests')





