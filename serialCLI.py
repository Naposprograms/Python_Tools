import sys
import serial
import threading


if __name__ == '__main__':


    try:
        serialPort = str(sys.argv[1])


    except IndexError:
        print('Missing argument: serial port name')


    else:

        serialDevice = serial.Serial('/dev/' + serialPort, 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)

        class KeyboardThread(threading.Thread):
            def __init__(self, textSource=None, type=None):

                self.textSource = textSource
                self.type = type
                
                if type == 'user':
                    name='keyboard-input-thread'
                    super(KeyboardThread, self).__init__(name=name)
                    self.start()

                if type == 'device':
                    name='device-input-thread'
                    super(KeyboardThread, self).__init__(name=name)
                    self.start()

            def run(self):
                if self.type == 'user':
                    while True:
                        self.textSource(input())

                if self.type == 'device':
                    while True:
                        if serialDevice.in_waiting > 0 and serialDevice.out_waiting == 0:
                            read_line = str(serialDevice.readline().decode('utf-8')).replace('\r\n', '')
                            self.textSource(read_line)


        def serialRead(read_line):
            if read_line != '':
                text = "[{}] {}".format(serialPort, read_line)
                print(text)
            
        def serialWrite(inputText):
            comandToSend = inputText + "\r\n"
            serialDevice.write((comandToSend).encode('utf-8'))
            

        userThread = KeyboardThread(serialWrite, type='user')
        deviceThread = KeyboardThread(serialRead, type='device')

        print('- - - Opening Serial CLI - - -')
        print('Type KeyboardInterrupt TWICE to exit.')
        
        while True:
            pass