# MIT License

# Copyright(c) 2021 Jaimyn Mayer

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import machine
import ubinascii


class Rdm6300:
    uart = None

    def __init__(self, uart=None):
        """[Initialise the UART driver]
        Args:
            uart (UART): The UART object to use.
        """
        if uart:
            self.uart = uart
        else:
            self.uart = machine.UART(
                1, baudrate=9600, timeout=2, timeout_char=10, tx=19, rx=18)
            self.uart.init(9600)

        # sometimes there's unwanted data in the buffer when we boot up
        # read it until it's all gone
        while self.uart.any():
            self.uart.read()

    def _parse_packet(self, packet):
        """Attempts to parse a packet from the RFID chip.

        Args:
            packet (bytes): The packet to try and parse.
        """
        length = 13
        header = 0x02
        stop_byte = 0x03

        # check for the packet length
        if len(packet) != length:
            print("WARNING: RFID packet has an invalid length ({}).".format(len(packet)))
            return None

        # check for the packet header
        if packet[0] != header:
            print("WARNING: RFID packet header is invalid.")
            return None

        # check for the packet stop byte
        if packet[12] != stop_byte:
            print("WARNING: RFID packet stop byte is invalid.")
            return None

        card_data = packet[1:11]  # raw bytes of the card data
        checksum = packet[11]  # checksum sent by RFID reader
        calculated_checksum = 0  # holds the checksum we calculate from the card id

        # loop through each byte in the card data and calculate the checksum by XORing them all
        for x in ubinascii.unhexlify(card_data):
            calculated_checksum = calculated_checksum ^ x

        # check that the calculated checksum matches the one sent by the RFID reader
        if checksum != calculated_checksum:
            print("WARNING: RFID checksum verification failed.")
            return None

        # if we get to here it means we received a valid packet, hurray!
        # lets remove the first byte (not part of the card ID) and convert it to a string
        card_id = card_data[2:].decode('ascii')

        # return a string of the decimal (integer) representation
        return str(int(card_id, 16))

    def read_card(self):
        """Attempts to read a card from the RDM6300 reader.

        Returns:
            string: A string of the card ID as a decimal (normally the value printed on the card)
        """
        # if we have data waiting for us
        if self.uart.any():
            data = self.uart.read()
            if data:
                return self._parse_packet(data)

            return None
