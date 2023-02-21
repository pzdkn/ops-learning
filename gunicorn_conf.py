from multiprocessing import cpu_count



# Socket Path

bind = 'unix:/var/www/fastapi_demo/gunicorn.sock'



# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/var/www/fastapi_demo/logs/access_log'

errorlog =  '/var/www/fastapi_demo/logs/error_log'
