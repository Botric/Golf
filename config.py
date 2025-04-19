import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')
    APP_PASSWORD = os.environ.get('APP_PASSWORD', 'golfer123')
    
    if os.environ.get('FLASK_ENV') == 'development' or os.environ.get('LOCAL_DEV') == '1':
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            'sqlite:///golf.db'
        )
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            'sqlite:////app/data/golf.db'
        )