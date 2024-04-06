import lvgl as lv
from ili9XXX import st7789
from ili9XXX import REVERSE_PORTRAIT
import axp202c
from ft6x36 import ft6x36
import pcf8563
import machine
import esp32

class KBD:
  def setHardware (self):
    print("LVGL version:"+str(lv.version_major())+"."+str(lv.version_minor()))
    self.axp=axp202c.PMU()
    self.axp.enableADC(axp202c.AXP202_ADC1,axp202c.AXP202_BATT_VOL_ADC1) # https://github.com/lewisxhe/MicroPython-for-TTGO-T-Watch?tab=readme-ov-file#axp202-power-example
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_BATT_CUR_ADC1)
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_VOL_ADC1)
    self.axp.enableADC(axp202c.AXP202_ADC1, axp202c.AXP202_VBUS_CUR_ADC1)
    self.axp.enablePower(axp202c.AXP202_LDO2) # this line from lilly.LILY()
    self.axp.enablePower(axp202c.AXP202_LDO3) # turn something on
    self.axp.enablePower(axp202c.AXP202_LDO4) # turn audio on
    self.axp.enablePower(axp202c.AXP202_DCDC2) # turn something on
    self.axp.enablePower(axp202c.AXP202_EXTEN) # turn something on
    self.disp = st7789(
      mosi=19, clk=18, cs=5, dc=27, rst=-1, backlight=12, power=-1,
      width=240, height=240, factor=4, invert=True, rot=REVERSE_PORTRAIT, start_x=0, start_y=80)
    # got REVERSE_PORTRAIT to work!
    self.touch = ft6x36(sda=23, scl=32, width=240, height=240)
    self.hwrtc=pcf8563.PCF8563(self.axp.bus)

  def drawCustomKbd (self):
    actscr=lv.screen_active()
    lv.obj.clean(actscr)
    # from https://baxterbuilds.com/micropython-lvgl-keyboard-examples/
    #list of button texts
    customMap = [ '34', 'hi', '\n', 'welcome', '']
    #list of button sizes and settings
    customCtrl = [ 2 | lv.buttonmatrix.CTRL.CHECKABLE, lv.buttonmatrix.CTRL.POPOVER, 1]
    kyb = lv.keyboard( lv.screen_active() )
    kyb.add_event_cb( self.handler, lv.EVENT.VALUE_CHANGED, None )
    #add key map were the lower case one used to be
    kyb.set_map( lv.keyboard.MODE.TEXT_LOWER, customMap, customCtrl )

  #function to print keypresses
  def handler( data ):
    tar = data.get_target()
    btn = tar.get_selected_btn()
    value = tar.get_btn_text( btn )
    print( value )
