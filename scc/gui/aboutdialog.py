#!/usr/bin/env python2
"""
SC-Controller - About dialog
"""
from __future__ import unicode_literals
from scc.tools import _

from gi.repository import Gtk
from scc.gui.editor import Editor
import os, sys

class AboutDialog(Editor):
	""" Standard looking about dialog """
	GLADE = "about.glade"
	
	def __init__(self, app):
		self.app = app
		self.setup_widgets()
	
	
	def setup_widgets(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(os.path.join(self.app.gladepath, self.GLADE))
		self.window = self.builder.get_object("Dialog")
		self.builder.connect_signals(self)
		
		# Get app version
		app_ver = "unknown"
		try:
			import pkg_resources, scc
			if scc.__file__.startswith(pkg_resources.require("sc-controller")[0].location):
				app_ver = pkg_resources.require("sc-controller")[0].version
		except:
			# pkg_resources is not available or __version__ file missing
			# There is no reason to crash on this.
			pass
		# Display versions in UI
		self.window.set_version(app_ver)
	
	def show(self, modal_for):
		if modal_for:
			self.window.set_transient_for(modal_for)
			self.window.set_modal(True)
		self.window.show()
	
	
	def on_dialog_response(self, *a):
		self.close()
	