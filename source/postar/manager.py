class Manager:

    def __init__(self, config):

        self.config = config
        self.worker_pub = {}

class WorkerManager:

    def __init__(self, config):

        self.config = config
        self.pool = []

    def pick(self):
        pass

class Worker:

    def __init__(self, config):
        pass

    def work(self):
        pass

    def release(self):
        pass

class SampleWorker(Worker):

    def __init__(self):
        pass