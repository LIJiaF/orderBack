import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from router import url
from config import tornadoConfig

define("port", default=8888, help="run on the given port", type=int)


def make_app(url, config):
    parse_command_line()
    app = tornado.web.Application(url, **config)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    make_app(url, tornadoConfig)
