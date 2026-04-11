class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)

    def __str__(self):
        return self.name

class MySequence(object):
    def __init__(self, *args):
        self.members = []
        for member in args:
            self.members.append(member)

    def __or__(self, other):
        self.members.append(other)
        return self

    def invoke(self):
        for member in self.members:
            print(member)


if __name__ == "__main__":
    a = Test("a")
    b = Test("b")
    c = Test("c")
    chain = a | b | c
    chain.invoke()

