import sys


class Log:
    @staticmethod
    def e(tag, msg):
        sys.stdout.write("ERROR/"+str(tag)+"\t\t"+str(msg)+"\n")

    @staticmethod
    def i(tag, msg):
        sys.stdout.write("INFO /"+str(tag)+"\t\t"+str(msg)+"\n")

    @staticmethod
    def d(tag, msg):
        sys.stdout.write("DEBUG/"+str(tag)+"\t\t"+str(msg)+"\n")

