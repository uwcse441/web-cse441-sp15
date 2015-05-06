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

    # Configure the deployment directory to be group writable, inherit group permissions on subdirectories
    if fabric.api.run('whoami') == fabric.api.run("stat -c '%U' /cse/web/courses/cse441/15sp/"):
        fabric.api.run('chmod g+s /cse/web/courses/cse441/15sp/')

    # Overwrite our current files
    fabric.api.run('rm -rf /cse/web/courses/cse441/15sp/* && cp -r --no-preserve=all ~/fabric_staging/web-cse441-sp15/* /cse/web/courses/cse441/15sp')

    # After writing, we now own a bunch of files, ensure they are group writable for the next person
    fabric.api.run('chmod -R g+w /cse/web/courses/cse441/15sp/*')

def serve():
    fabric.api.local('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')


# We cannot have a test because Fabric requires Python 2.7 but our tests use Python 3.4.
# It might be possible to fix this by moving to invoke, the Python 3 descendant of Fabric.
#
# def test():
#    fabric.api.local('nosetests')





