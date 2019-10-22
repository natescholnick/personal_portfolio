# This is the first file accessed during bootup
# The structure is from the app folder, import the app variable

from app import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
