from scapy.all import *
import sys
import optparse
import threading
import termcolor
from scapy.layers.inet import TCP, IP


class DDOSDetect:
    def __init__(self) -> None:
        self.interface = self.get_params()[0]
        self.threshold = self.get_params()[1]
        self.packet_stream = {}  # 该字段存储每个流以及对应的包数
        self.interval = 5
        self.banner()

    def banner(self):
        banner = """
                **************************************************

                ***DDOS ATTACK Detection Tool by Jason Wong*******

                **************************************************
        """
        print(banner)

    def get_params(self):
        parser = optparse.OptionParser('Usage: <Program> -i interface -t threshold')
        parser.add_option('-i', '--interface', dest='interface', type='string', help='Specify interface to listen')
        parser.add_option('-t', '--threshold', dest='threshold', type='int',
                          help='Specify threshold of packets quantity')
        options, args = parser.parse_args()
        if options.interface is None or options.threshold is None:
            print(parser.usage)
            sys.exit(0)
        return options.interface, options.threshold

    def packet_handler(self, pkt):
        if pkt.haslayer(TCP):
            src = pkt.getlayer(IP).src
            dst = pkt.getlayer(IP).dst
            dport = pkt.getlayer(TCP).dport
            stream = str(src) + ":" + str(dst) + ":" + str(dport)

            if stream in self.packet_stream.keys():
                self.packet_stream[stream] = self.packet_stream[stream] + 1
            else:
                self.packet_stream[stream] = 1

    def packet_stream_display(self):  # 定时将packet_stream的数据打印出来
        # print(self.packet_stream)
        print("Captured Packets Statistics: \n")
        if len(self.packet_stream) > 0:
            for k, v in self.packet_stream.items():
                if v > self.threshold:
                    print("DDOS attack found: \n%s times: %d" % (k, v))
                print(k, '\t', v)
        t = threading.Timer(self.interval, self.packet_stream_display)
        t.start()

    def run(self):
        try:
            sniff(iface=self.interface, prn=self.packet_handler, store=False)
        except KeyboardInterrupt:
            print("Exit program now!")
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(0)

    def start_total(self):
        self.packet_stream_display()
        t = threading.Thread(target=self.run)
        t.start()


if __name__ == '__main__':
    ddos = DDOSDetect()
    ddos.start_total()
