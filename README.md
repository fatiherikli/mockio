### Mockio

Mockio is a mini library that allows you to mock open method with StringIO.

Example:

    class TestNginxParser(unittest.TestCase):
        files = {
            "/etc/nginx/sites-enabled/foo.conf": "server foo {}",
            "/etc/nginx/sites-enabled/bar.conf": ""
        }

        @mockio(files)
        def test_read(self):
            conf = open("/etc/nginx/sites-enabled/foo.conf").read()
            self.assertEqual(conf, "server foo {}")
            # ...

