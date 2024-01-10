from ._anvil_designer import SwitchTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import document, getComputedStyle
from anvil.js import window
from anvil import HtmlTemplate
from ...Functions import theme_color_to_css, enabled_property, style_property, color_property, theme_color_to_css, property_with_callback, margin_property
import anvil.designer


class Switch(SwitchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._props = properties
    self.init_components(**properties)
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)
    

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].addEventListener("change", self.handle_change)
    
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-switch-input'].removeEventListener("change", self.handle_change)

  def handle_change(self, event):
    print('changed')
    if self.enabled:
      print('enabled')
      #self.dom_nodes['anvil-m3-switch-input'].focus()
      print('self.selected before:', self.selected)
      self.selected = not self.selected
      print('self.selected after:', self.selected)
      self.raise_event("change")

  def set_color_styles(self, value=None):
    if self.selected:
      print('setting color styles')
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.selected_background_color) if self.selected_background_color else None
      if self.selected_thumb_color:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-selected-thumb-color', theme_color_to_css(self.selected_thumb_color))
      else:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-selected-thumb-color', 'var(--anvil-m3-on-primary)')
    else:
      self.dom_nodes['anvil-m3-switch-slider'].style.backgroundColor = theme_color_to_css(self.unselected_background_color) if self.unselected_background_color else None
      self.dom_nodes['anvil-m3-switch-slider'].style.borderColor = theme_color_to_css(self.unselected_outline_color) if self.unselected_outline_color else None
      if self.unselected_thumb_color:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-unselected-thumb-color', theme_color_to_css(self.unselected_thumb_color))
      else:
        self.dom_nodes['anvil-m3-switch-slider'].style.setProperty('--anvil-m3-unselected-thumb-color', 'var(--anvil-m3-outline)')
    
  @property
  def selected_icon(self):
    return self._selected_icon

  @selected_icon.setter
  def selected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-enabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._selected_icon = value
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-enabled-icon')
  
  @property
  def unselected_icon(self):
    return self._unselected_icon

  @unselected_icon.setter
  def unselected_icon(self, value):
    link_icon = self.dom_nodes['anvil-m3-disabled-switch-icon']
    switch_slider = self.dom_nodes['anvil-m3-switch-slider']
    self._unselected_icon = value
    
    link_icon.classList.remove("material-symbols-outlined")
    if value:
      link_icon.classList.add("material-symbols-outlined")
      link_icon.innerText = value
      switch_slider.classList.add('anvil-m3-has-disabled-icon')

  @property
  def selected(self):
    return self.dom_nodes['anvil-m3-switch-input'].checked

  @selected.setter
  def selected(self, value):
    print('selected value:', value)
    self.dom_nodes['anvil-m3-switch-input'].checked = value
    self.set_color_styles()
      
  enabled = enabled_property('anvil-m3-switch-input')
  align = style_property('anvil-m3-switch-container', 'justifyContent', 'align')
  selected_background_color = property_with_callback('selected_background_color', set_color_styles)
  unselected_background_color = property_with_callback('unselected_background_color', set_color_styles)
  selected_thumb_color = property_with_callback('selected_thumb_color', set_color_styles)
  unselected_thumb_color = property_with_callback('unselected_thumb_color', set_color_styles)
  unselected_outline_color = property_with_callback('unselected_outline_color', set_color_styles)
  visible = HtmlTemplate.visible
  margin = margin_property('anvil-m3-switch-container')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    print('in the actual component init:', self.selected)

  
  

  
  
