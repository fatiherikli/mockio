from StringIO import StringIO

import mock


def mockio(files):
    """
    A decorator that allows you mock `open` method.
    Usage:

        files = {
            "/etc/nginx/sites-enabled/foo": "server {}"
        }

        @mockio(files)
        def test_foo():
            assert open("/etc/nginx/sites-enabled/foo").read(), "server {}"

    """
    fake_storage = dict((k, StringIO(v)) for k, v in files.items())

    def get_file(filename):
        stringio = fake_storage.get(filename)
        if stringio is None:
            raise IOError
        return stringio

    def wrap(func):
        def inner(*args, **kwargs):
            with mock.patch("__builtin__.open") as _open:
                _open.side_effect = get_file
                return func(*args, **kwargs)
        return inner

    return wrap
