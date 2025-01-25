import os

class Config:
    """Base configuration."""
    ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = ENV == 'development'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://identifies_user:identifies_password@db:5432/identifies_db')
    API_KEY = os.getenv('API_KEY', 'default-api-key')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

# Configuration mapping
config_mapping = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

def get_config():
    """Retrieve the appropriate configuration class based on the environment."""
    env = os.getenv('FLASK_ENV', 'production')
    return config_mapping.get(env, ProductionConfig)
