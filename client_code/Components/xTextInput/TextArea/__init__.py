from ._anvil_designer import TextAreaTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import TextInput

class TextArea(TextInput):
  def __init__(self, **properties):
    self._props = properties
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
