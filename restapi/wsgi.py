"""Serve WSGI app."""

from run import app

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0:9024')
