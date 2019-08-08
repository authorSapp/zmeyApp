class Worker(QObject):

	# slots
	def action_by_timer(self, jerome, pin, timer):
		jerome.set_pin_high(pin)
		time.sleep(timer)
		jerome.set_pin_low(pin)

	# signal
	# resultReady


class ThreadController(QObject):

	workerThread = QThread()

	def __init__(self):
		super(ThreadController, self).__init__()
		worker = Worker()
		worker.moveToThread(workerThread)
		workerThread.finished.connect(worker.deleteLater)
		self.operate.connect(worker.action_by_timer)
		worker.resultReady.connect(self.handleResults)
		workerThread.start()

	def __del__(self):
        workerThread.quit();
        workerThread.wait();

	# slots
	# handleResults

	# signal
	# operate
