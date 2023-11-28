from ._anvil_designer import ButtonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from ...Functions import color_property, font_family_property, font_size_property, style_property, property_with_callback

import anvil.designer

class Button(ButtonTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._text = properties.get('text', '')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-button'].addEventListener("click", self.handle_click)
    
  align = style_property('anvil-m3-button-component', 'justifyContent', 'align') 

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

  def _anvil_get_interactions_(self):
    return [{
      "type": "whole_component",
      "title": "Edit text",
      "icon": "edit",
      "default": True,
      "callbacks": {
        "execute": lambda: anvil.designer.start_inline_editing(self, "text", self.dom_nodes['anvil-m3-button-text'])
      }
    }]

  @property
  def material_icon(self):
    return self._material_icon

  @material_icon.setter
  def material_icon(self, value):
    button = self.dom_nodes['anvil-m3-button']
    button_icon = self.dom_nodes['anvil-m3-button-icon']
    self._material_icon = value
    if value:
      button_icon.innerText = value
      button_icon.style.display = "block"
      button.classList.add('anvil-m3-icon-padding')
    else: 
      button_icon.innerText = ""
      button_icon.style.display = "none"
      button.classList.remove('anvil-m3-icon-padding')

  def set_text(self, value):
    self.dom_nodes['anvil-m3-button-text'].innerHTML = value or ""
  text = property_with_callback("text", set_text)

  def set_enabled(self, value):
    if value:
      self.dom_nodes['anvil-m3-button'].removeAttribute("disabled")
    else:
      self.dom_nodes['anvil-m3-button'].setAttribute("disabled", " ")
  enabled = property_with_callback("enabled", set_enabled)

  @property
  def appearance(self):
    return self._appearance

  def set_appearance
    button = self.dom_nodes['anvil-m3-button']
    button.classList.remove('anvil-m3-elevated')
    button.classList.remove('anvil-m3-filled')
    button.classList.remove('anvil-m3-tonal')
    button.classList.remove('anvil-m3-outlined')
    if value:
      button.classList.add(f"anvil-m3-{value}")

  def form_show(self, **event_args):
      """This method is called when the HTML panel is shown on the screen"""
      if not self.text:
        if anvil.designer.in_designer:
          self.text = anvil.designer.get_design_name(self)
        else:
          self.text = "Button"

  text_color = color_property('anvil-m3-button-text', 'color', 'text_color')
  icon_color = color_property('anvil-m3-button-icon', 'color', 'icon_color')
  font_family = font_family_property('anvil-m3-button-text')
  font_size = font_size_property('anvil-m3-button-text' )
  icon_size = font_size_property('anvil-m3-button-icon', 'icon_size')
  # TODO: Add background color property



  
