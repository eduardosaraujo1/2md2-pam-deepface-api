from src.api import app

if __name__ == '__main__':
    # waitress-serve --host 127.0.0.1 main:app
    app.run(debug=True)