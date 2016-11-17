#!/usr/bin/env python

import dbus
import dbus.mainloop.glib
import dbus.service
import gobject

BUS_NAME = 'com.example.CounterService'
OBJECT_PATH = '/com/example/CounterObject'
INTERFACE = 'com.example.Counter'


# D-Bus object on the server side
class CounterObject(dbus.service.Object):
    @dbus.service.method(INTERFACE, in_signature="i", out_signature="")
    def SetCount(self, count):
        self.count = count
        print('SetCount called: ' + str(count))

    @dbus.service.method(INTERFACE, in_signature="", out_signature="i")
    def GetCount(self):
        print('GetCount called')
        return self.count


def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    # Create a D-Bus object
    session_bus = dbus.SessionBus()
    bus_name = dbus.service.BusName(BUS_NAME, session_bus)
    counter_object = CounterObject(session_bus, OBJECT_PATH)

    # Run a main loop
    print 'Start mainloop...'
    loop = gobject.MainLoop()
    loop.run()


if __name__ == '__main__':
    main()

