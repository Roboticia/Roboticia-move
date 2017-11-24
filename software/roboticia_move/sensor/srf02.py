import time
import smbus2 as smbus

from ...robot.sensor import Sensor
from ...utils import StoppableLoopThread


class SRF02(Sensor):
    """
    Define a SRF02 sensor
    """
    registers = Sensor.registers + ['distance']

    def __init__(self, name):
        Sensor.__init__(self, name, sync_freg = 2.0)
		
		i2c = smbus.SMBus(3)
        self._controller = StoppableLoopThread(sync_freq, update=self.update)
        self._controller.start()
       
    def __repr__(self):
        return ('<DistanceSensor name={self.name} '
                'distance={self.distance}>').format(self=self)
    def close(self):
        self._controller.stop()
		
	def start(self):
        self._controller.start()
		
	def update(self):
	    data = []
        for i in range(10):
		   i2c.write_byte_data(0x70, 0, 81)
		   time.sleep(0.02)
		   data.Append(sum(i2c.read_i2c_block_data(0x70, 2,4)))
		self._distance = numpy.median(data)
		numpy.var(data)
		
    @property
    def distance(self):
        return self._distance
