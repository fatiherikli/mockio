import unittest

from mockio import mockio


class TestMockio(unittest.TestCase):
    files = {
        "/etc/nginx/sites-enabled/foo.conf": "server {}",
        "/etc/nginx/sites-enabled/bar.conf": ""
    }

    @mockio(files)
    def test_read(self):
        self.assertEqual(open("/etc/nginx/sites-enabled/foo.conf").read(),
                         "server {}")

    @mockio(files)
    def test_write(self):
        _file = open("/etc/nginx/sites-enabled/bar.conf")
        _file.write("test")
        _file.close()
        self.assertIn("test", _file.buflist)


if __name__ == "__main__":
    unittest.main()
