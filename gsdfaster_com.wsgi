import logging, sys

# redirect logs to stderr
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/gsdfaster_com')

from gsdfaster_com import app as application
