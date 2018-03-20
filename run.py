#This is the application's entry point. We'll run this file to start the Flask server and launch our application.


from app import create_app

config_name = 'development'
app = create_app(config_name)

if __name__ == '__main__':
    app.run()