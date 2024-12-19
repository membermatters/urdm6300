# urdm6300

urdm6300 is a simple micro python driver / library that allows you to read RFID cards from an attached RDM6300 board. Several suppliers manufacture these boards, including seeed studio and various Aliexpress sellers.

# Installation

Simply download the `urdm6300` folder and upload it to your micro python board. You can download this entire repository [here](https://github.com/membermatters/urdm6300/archive/refs/heads/main.zip).

# Examples

Using the default UART config (`machine.UART(1, baudrate=9600, timeout=2, timeout_char=10, tx=19, rx=18)`).

```python
from urdm6300 import Rdm6300

rfid_reader = Rfid()

# note that this is not blocking and needs to be called as often as possible to check for new card scans
card_id = rfid_reader.read_card()
```

You can also specify your own UART object if you'd like:

```python
from urdm6300 import Rdm6300
import machine

uart = machine.UART(1, baudrate=9600)
rfid_reader = Rfid(uart)

# note that this is not blocking and needs to be called as often as possible to check for new card scans
card_id = rfid_reader.read_card()
```

You can also add this repo as a git sub module to your project to make keeping it up to date easier.
