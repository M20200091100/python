# -*- coding: latin1 -*-
import pygtk
import gtk

pygtk.require('2.0')


def helloWorld(widget):
    print("Hello World!")

    button.set_label("I'm clicked...")

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
button = gtk.Button("Click here...")

button.connect('clicked', helloWorld)

window.add(button)
window.show_all()
gtk.main()
