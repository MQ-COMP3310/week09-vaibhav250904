from project import create_app
import os 

if __name__ == '__main__':
  app = create_app()
  debug_mode = os.getenv('FLASK_ENV', 'production') == 'development'
  app.run(host='127.0.0.1', port=8001, debug=debug_mode) 

