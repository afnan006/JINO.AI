# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Defaults to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=port)
