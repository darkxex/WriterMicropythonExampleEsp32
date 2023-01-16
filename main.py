
import machine
from ssd1306_setup import ssd
from writer import Writer

# Font
import arial20esp as arial20
ssd.fill(0)
wri = Writer(ssd, arial20, False)
wri.set_clip(False, False, False)
Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output
wri.printstring('Sábado\n')
wri.printstring('16 Dic 2023\n')
wri.printstring('10.30am')
ssd.show()