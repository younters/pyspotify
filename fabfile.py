from fabric.api import execute, local, settings, task


@task
def preprocess_header():
    local('cpp -nostdinc spotify/api.h > spotify/api.processed.h || true')


@task
def test():
    local('nosetests')


@task
def autotest():
    while True:
        local('clear')
        with settings(warn_only=True):
            execute(test)
        local(
            'inotifywait -q -e create -e modify -e delete '
            '--exclude ".*\.(pyc|sw.)" -r spotify/ tests/')


@task
def update_authors():
    # Keep authors in the order of appearance and use awk to filter out dupes
    local(
        "git log --format='- %aN <%aE>' --reverse | awk '!x[$0]++' > AUTHORS")