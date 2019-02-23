from sty import fg

class Log:
    @staticmethod
    def e(tag, msg):
        print(fg.red+"ERROR/"+str(tag)+"\t"+str(msg))

    @staticmethod
    def i(tag, msg):
        print(fg.blue+"INFO /"+str(tag)+"\t"+str(msg))

    @staticmethod
    def d(tag, msg):
        print(fg.green+"DEBUG/"+str(tag)+"\t"+str(msg))