class NodeBackend(object):
    def __init__(self, environment):
        self.env = environment

    def args(self):
        return ['./bin/node']
