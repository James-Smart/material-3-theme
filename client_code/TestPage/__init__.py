from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def navigation_link_1_click(self, **event_args):
    """This method is called when the component is clicked"""
    alert(title="Alert", content="You're on the home page!", buttons=["Continue", "Cancel"], role="")

