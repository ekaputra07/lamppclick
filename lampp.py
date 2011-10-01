#!/usr/bin/env python

import commands
import gtk
import os

class lampp_gui:

    lampp_start_command = 'gksudo /opt/lampp/lampp start'
    lampp_stop_command = 'gksudo /opt/lampp/lampp stop'

    def __init__(self):
        uifile = '/opt/lamppclick/lampp-gui.glade'
        ui = gtk.Builder()
        ui.add_from_file(uifile)
        ui.connect_signals(self)
        self.window = ui.get_object('window')
        self.start = ui.get_object('start')
        self.stop = ui.get_object('stop')
        self.console = ui.get_object('console')
        self.c_buffer = self.console.get_buffer()
        self.c_buffer.set_text("LAMPP Click V1.0\nby Eka Putra - balitechy.com\nPowered by Python, Gtk, Glade\n\nWorks only if your LAMPP installed at : /opt/lampp\n\nUse this utility to easily start and stop your LAMPP Server. No more typing commands at terminal console. Enjoy!")

    def on_start_clicked(self,widget):
        command_result = commands.getstatusoutput(self.lampp_start_command)
        self.c_buffer.set_text(command_result[1])

    def on_stop_clicked(self, widget):
        command_result = commands.getstatusoutput(self.lampp_stop_command)
        self.c_buffer.set_text(command_result[1])

    def on_window_destroy(self,widget):
        gtk.main_quit()

    def main(self):
        self.window.show_all()
        gtk.main()


if __name__ == '__main__':
    app = lampp_gui()
    app.main()

