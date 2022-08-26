from .apps import monkeypatch_django


@worker_ready.connect
def config_app(sender=None, conf=None, **kwargs):
    print("django_dbconn_retry worker.ready...")
    monkeypatch_django()
