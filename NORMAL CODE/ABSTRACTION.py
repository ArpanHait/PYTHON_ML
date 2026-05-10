class car:
    def __init__(self):
        self.brk=False
        self.cluth=False
        self.acc=False

    def start(self):
        self.cluth=True
        self.acc=True
        print("car started")

object=car()
object.start()

