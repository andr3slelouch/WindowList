import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Events():
    def __init__(self):
        pass

    def window_visibility_event(self, widget, event):
        ## if window is obscured
        if event.state == 2:
            self.close()

    def menu_popup(self, widget, event):
        if(event.button == 3):
            widget.menu.popup(None, None, None, None, 0, Gtk.get_current_event_time())

    def on_clicked(self, widget):
        self.switch_window(widget.win_id)

    def switch_window(self,win_id):
        subprocess.Popen(['wmctrl','-i','-a',win_id], stdout=subprocess.PIPE)
        self.close()

    def close(self):
        Gtk.main_quit()

    def on_key_release(self, widget, ev, data=None):
        # IF ESC is pressed
        if ev.keyval == 65307:
            self.close()
