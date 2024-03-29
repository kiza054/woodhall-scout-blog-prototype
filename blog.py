from app import app, db, cli
from app.models import User, Post, Notification, Message

cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)