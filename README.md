# urdm6300

urdm6300 is a simple micro python driver / library that allows you to read RFID cards from an attached RDM6300 board. Several suppliers manufacture these boards, including seeed studio and various Aliexpress sellers.

# Installation

Simply download the `urdm6300` folder and upload it to your micro python board. You can download this entire repository [here](https://github.com/membermatters/urdm6300/archive/refs/heads/main.zip).

# Examples

Using the default UART config (`machine.UART(1, baudrate=9600, timeout=2, timeout_char=10, tx=19, rx=18)`).

```python
from urdm6300 import Rfid

rfid_reader = Rfid()

# note that this is not blocking and needs to be called as often as possible to check for new card scans
card_id = rfid_reader.read_card()
```

You can also specify your own UART object if you'd like:

```python
from urdm6300 import Rfid
import machine

uart = machine.UART(1, baudrate=9600)
rfid_reader = Rfid(uart)

# note that this is not blocking and needs to be called as often as possible to check for new card scans
card_id = rfid_reader.read_card()
```

# Licence

MIT License

Copyright(c) 2021 Jaimyn Mayer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
