# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

# if __name__ == '__main__':
#     app.run(debug=True)

class PlayerCharacter:
    def __init__(self, name) -> None:
        self.name = name
        
    def run(self):
        print('run')
        
player1 = PlayerCharacter()
