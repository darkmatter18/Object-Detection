"""
Celery worker main and celery_app for tasks sender.
"""

from celery import Celery

from app.settings.config import settings


class Config:
    """
    https://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration-and-defaults
    """

    task_acks_late = (
        True  # guarantee task completion but the task may be executed twice
    )
    # if the worker crashes mid execution
    result_expires = 600  # A built-in periodic task will delete the results after this time (seconds)
    # assuming that celery beat is enabled. The task runs daily at 4am.
    # task_ignore_result = True  # now we control this per task
    task_compression = "gzip"
    result_compression = "gzip"
    broker_connection_retry = True
    broker_connection_retry_on_startup = True


app = Celery(
    "celery",
    backend=settings.CELERY_BACKEND_URI,
    broker=settings.CELERY_BROKER_URI,
)
app.config_from_object(Config)
print(
    f">>> celery_app: {settings.CELERY_BACKEND_URI}, {settings.CELERY_BROKER_URI}"
)
