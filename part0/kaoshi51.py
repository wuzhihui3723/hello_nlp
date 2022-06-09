class Server:

    def __init__(self, CPU, Memory, Disk, OS):
        self.CPU = CPU
        self.Memory = Memory
        self.Disk = Disk
        self.__OS = OS

    def server_info(self):
        print("{0}核CPU，{1}G内存，{2}G磁盘空间，{3}系统".format(self.CPU, self.Memory, self.Disk, self.__OS))


if __name__ == "__main__":
    server = Server(8, 40, 150, "Linux")
    server.server_info()

