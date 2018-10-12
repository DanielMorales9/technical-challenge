import sys

from app import app

if __name__ == '__main__':
    app.run()

    if app.config['crashed']:
        print('app crashed, exiting non-zero')
        sys.exit(1)
