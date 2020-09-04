from flask import Flask

app = Flask(__name__)


@app.route('/events', methods=['POST'])
def events():
    # put webhook logic here
    print("Webhook Received")
    return '', 204


if __name__ == "__main__":
    app.run()
