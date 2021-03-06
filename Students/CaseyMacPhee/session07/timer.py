
import time
class Timer(object):

	def __init__(self, handle_error):
		self.handle_error = handle_error
	def __enter__(self):
		self.start = time.time()
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.end = time.time()
		print "Took: {} seconds".format(self.end - self.start)
		return self.handle_error

