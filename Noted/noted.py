import sublime
import sublime_plugin
from datetime import date

class NotedCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		noted_view = self.view.window().new_file()
		noted_view.set_name("notes-" + date.today().__str__() + ".noted")