from s3 import app
from s3.api import *

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)