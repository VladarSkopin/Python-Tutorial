class Ordering:
    # Subsystem 1

    def order(self):
        print("Ordering")


class Preparing:
    # Subsystem 2

    def prepare(self):
        print("Preparing...")


class Delivering:
    # Subsystem 3

    def deliver(self):
        print("Delivering...")


class Operator:
    """Facade"""

    def __init__(self):
        self.ordering = Ordering()
        self.preparing = Preparing()
        self.delivering = Delivering()

    def complete_order(self):
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()


""" main method """
if __name__ == "__main__":
    op = Operator()
    op.complete_order()
