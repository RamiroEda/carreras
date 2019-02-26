from sty import fg
import sys


class Log:
    @staticmethod
    def e(tag, msg):
        sys.stdout.write(fg.red+"ERROR/"+str(tag)+"\t\t"+str(msg)+"\n")

    @staticmethod
    def i(tag, msg):
        sys.stdout.write(fg.blue+"INFO /"+str(tag)+"\t\t"+str(msg)+"\n")

    @staticmethod
    def d(tag, msg):
        sys.stdout.write(fg.green+"DEBUG/"+str(tag)+"\t\t"+str(msg)+"\n")
