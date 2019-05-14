from twisted.internet.protocol import Protocol


class echo(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
