# Celery Configuration

broker_url = "amqp://guest:guest@rabbitmq:5672//"
result_backend = "rpc://"
task_acks_late = True
