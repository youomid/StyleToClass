import sublime
import sublime_plugin
from bs4 import BeautifulSoup
from .converters import Converters

def create_new_css_group():
    """
    Create a new view group to the far right for the new css file.

    Args:
      None

    Returns:
      Return the new group number.

    """
    current_window = sublime.active_window()
    layout = current_window.get_layout()

    cols = layout['cols']
    cells = layout['cells']

    last_col = len(cols) - 1
    last_row = len(layout['rows']) - 1

    # width of the new view group as a percentage decimal
    width = 0.5
    scale = 1 - 0.5

    # scale down the width of all the current windows
    for i, col in enumerate(cols):
        if col >= 0:
            cols[i] = col*width

    # add column for the new view group
    cols.append(1)

    # add a new cell to the right of the furthest cell on the right
    newcell = [last_col, 0, last_col + 1, last_row]
    cells.append(newcell)

    # update layout
    groups = current_window.num_groups()
    current_window.run_command("set_layout", layout)

    return (groups + 1)


class StyleToClassCommand(sublime_plugin.TextCommand):

  def run(self, edit, **args):
    converters = Converters()

    html_view = self.view

    # get the html data
    contents = html_view.substr(sublime.Region(0, html_view.size()))

    syntax = 'Packages/CSS/CSS.tmLanguage'

    cssFileContent, newHtml = converters.convertStyleToClass(contents)

    html_view.replace(edit, sublime.Region(0, html_view.size()), newHtml)

    new_group_num = create_new_css_group()

    # create_new_css_group will create a new group and self.view will now point to that
    # group's view
    css_view = self.view

    # create new css file and add new css classes
    new_file_view = css_view.window().new_file()
    new_file_view.set_syntax_file(syntax)
    new_file_view.run_command("append", {"characters": cssFileContent})

