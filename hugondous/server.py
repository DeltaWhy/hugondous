from hugondous import __version__
import flask
import subprocess


app = flask.Flask('hugondous')


@app.route('/')
def hello():
    return 'hugondous ' + __version__


@app.route('/rebuild', methods=['POST'])
def rebuild():
    subprocess.call(['git', 'pull'], cwd='site')
    subprocess.call(['hugo'], cwd='site')
    return 'ok'


if __name__ == '__main__':
    app.run()
