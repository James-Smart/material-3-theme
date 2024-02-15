import anvil.server
from . import TextInput
import anvil.designer
from ...Functions import property_with_callback, italic_property, bold_property, underline_property, font_family_property, font_size_property, color_property
from anvil.property_utils import anvil_property
from ...utils import _m3_icons

"""
Remaining tasks on hold for DEV: 
- property "NONE" enum selection for icons
"""

leading_icon_property = {"name": "leading_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Icon", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         # "none_option_label": "None", 
                         "description": "The icon to display on the right side of this component."}
trailing_icon_property = {"name": "trailing_icon", 
                         "type": "enum", 
                         "options": _m3_icons, 
                         "group": "Icon", 
                         "important": True, 
                         "default_value": "",
                         # "include_none_option": True, 
                         "description": "The icon to display on the left side of this component."}
type_property = {"name": "type", 
                         "type": "enum", 
                         "options": ["text", "number", "email", "tel", "url"], 
                         "group": "Other", 
                         "important": False, 
                         "default_value": "text",
                         "description": "What type of data will be entered into this box?"}
hide_text_property = {"name": "hide_text", 
                         "type": "boolean", 
                         "group": "Other", 
                         "important": False, 
                         "default_value": False,
                         "description": "Display stars instead of the text entered into this component."}
leading_icon_color_property = {"name": "leading_icon_color", 
                               "type": "color", 
                               "group": "Icon", 
                               "important": True, 
                               "default_value": "",
                               # "include_none_option": True, 
                               # "none_option_label": "None", 
                               "description": "The color of the leading icon."}
trailing_icon_color_property = {"name": "trailing_icon_color", 
                               "type": "color", 
                               "group": "Icon", 
                               "important": True, 
                               "default_value": "",
                               # "include_none_option": True, 
                               # "none_option_label": "None", 
                               "description": "The color of the trailing icon."}


click_event = {"name": "click", "defaultEvent": True, "description": "When the trailing icon is clicked."}
pressed_enter_event = {"name": "pressed_enter", "defaultEvent": False, "description": "When the user presses enter in this component."}

class TextField(TextInput):
  _anvil_properties_ = [leading_icon_property, trailing_icon_property, type_property, hide_text_property, leading_icon_color_property, trailing_icon_color_property, *TextInput._anvil_properties_]
  _anvil_events_ = [click_event, pressed_enter_event, *TextInput._anvil_events_]
  
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    hiddenInput = self.dom_nodes['textarea']
    self.dom_nodes['input-container'].removeChild(hiddenInput)
    
    self._on_key_down = self._on_key_down
    self._on_change = self._on_change
    self._handle_click = self._handle_click
    self._on_focus = self._on_focus
    self._on_lost_focus = self._on_lost_focus

    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    self.dom_nodes['textfield'].addEventListener("input", self._on_input)
    self.dom_nodes['textfield'].addEventListener("keydown", self._on_key_down)
    self.dom_nodes['textfield'].addEventListener("change", self._on_change)
    self.dom_nodes['trailing-icon'].addEventListener("click", self._handle_click)
    self.dom_nodes['textfield'].addEventListener("focus", self._on_focus)
    self.dom_nodes['textfield'].addEventListener("blur", self._on_lost_focus)
    
  def _on_cleanup(self, **event_args):
    self.dom_nodes['textfield'].removeEventListener("input", self._on_input)
    self.dom_nodes['textfield'].removeEventListener("keydown", self._on_key_down)
    self.dom_nodes['textfield'].removeEventListener("change", self._on_change)
    self.dom_nodes['trailing-icon'].removeEventListener("click", self._handle_click)
    self.dom_nodes['textfield'].removeEventListener("focus", self._on_focus)
    self.dom_nodes['textfield'].removeEventListener("blur", self._on_lost_focus)

  def _on_key_down(self, e):
    if e.key == "Enter":
      self.raise_event("pressed_enter")

  def _set_placeholder(self, value):
    input = self.dom_nodes['textfield']
    if value:
      input.placeholder = value
      input.classList.add('anvil-m3-has-placeholder')
    else:
      input.placeholder = " "
      input.classList.remove('anvil-m3-has-placeholder')
  placeholder = property_with_callback('placeholder', _set_placeholder)

  # def _set_text(self, value):
  #   input = self.dom_nodes['textfield']
  #   if value:
  #     input.text = value
  #   else:
  #     input.text = ""
  #     # input.classList.remove('anvil-m3-has-placeholder')
  # text = property_with_callback('text', _set_text)

  @property
  def text(self):
    return self._props.get('text')

  @text.setter
  def text(self, value):
    self._props['text'] = value
    self.dom_nodes['textfield'].text = value
      
  def _set_label(self, value):
    self.dom_nodes['label-text'].innerText = value or ""
    if value:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', True)
    else:
      self.dom_nodes['textfield'].classList.toggle('has_label_text', anvil.designer.in_designer);
  label_text = property_with_callback("label_text", _set_label)

  def _set_enabled(self, value):
    supporting_text = self.dom_nodes['subcontent']
    if value:
      self.dom_nodes['textfield'].removeAttribute("disabled")
      supporting_text.classList.remove("anvil-m3-textinput-disabled")
    else:
      self.dom_nodes['textfield'].setAttribute("disabled", " ")
      supporting_text.classList.add("anvil-m3-textinput-disabled")
  enabled = property_with_callback("enabled", _set_enabled)
  
  def _set_id(self, value):
    super()._set_id(value)
    self.dom_nodes["textfield"].id = value

  def _set_error(self, value):
    super()._set_error(value)
    icon = "error" if value else self.trailing_icon
    self._set_trailing_icon(icon)
  error = property_with_callback("error", _set_error)

  @anvil_property('enum')
  def leading_icon(self):
    return self._props.get('leading_icon')

  @leading_icon.setter
  def leading_icon(self, value):
    self._props['leading_icon'] = value
    self._set_leading_icon(value)

  @anvil_property('enum')
  def trailing_icon(self):
    return self._props.get('trailing_icon')

  @trailing_icon.setter
  def trailing_icon(self, value):
    self._props['trailing_icon'] = value
    self._set_trailing_icon(value)
    
  def _set_leading_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    leading_icon = self.dom_nodes['leading-icon']
    text_field_input = self.dom_nodes['textfield']
    border_container = self.dom_nodes['border-container']

    if value:
      leading_icon.style.display = "block"
      leading_icon.innerText = value
      icon_container.style.paddingLeft = "12px"
      text_field_input.style.paddingLeft = "48px"
      border_container.classList.add("with-icon")
    else:
      leading_icon.style.display = "none"
      leading_icon.innerText = ""
      icon_container.style.paddingLeft = "16px"
      text_field_input.style.paddingLeft = "16px"
      border_container.classList.remove("with-icon")
  # leading_icon = property_with_callback("leading_icon", set_leading_icon)  
  
  def _set_trailing_icon(self, value):
    icon_container = self.dom_nodes['icon-container']
    trailing_icon = self.dom_nodes['trailing-icon']
    text_field_input = self.dom_nodes['textfield']

    if value:
      trailing_icon.style.display = "block"
      trailing_icon.innerText = value
      text_field_input.style.paddingRight = "48px"
    else:
      trailing_icon.style.display = "none"
      trailing_icon.innerText = ""
      text_field_input.style.paddingRight = "16px"
  # trailing_icon = property_with_callback("trailing_icon", set_trailing_icon)

  italic_display = italic_property('textfield', 'italic_label')
  bold_display = bold_property('textfield', 'bold_display')
  underline_display = underline_property('textfield', 'underline_display')
  display_font_size = font_size_property('textfield', 'display_font_size')
  display_font = font_family_property('textfield', 'display_font')
  display_text_color = color_property('textfield', 'color', 'display_text_color')
  background = color_property('textfield', 'backgroundColor', 'background' )
  leading_icon_color = color_property('leading-icon', 'color', 'leading_icon_color')
  trailing_icon_color = color_property('trailing-icon', 'color', 'trailing_icon_color')

  def _set_character_limit(self, value):
    if value is None or value < 1:
      text_field_input = self.dom_nodes['textfield'].removeAttribute("maxlength")
      self.dom_nodes['character-counter'].style = "display: none";
    else:
      text_field_input = self.dom_nodes['textfield'].setAttribute("maxlength", value)
      self.dom_nodes['character-counter'].style = "display: inline";
      self.dom_nodes['character-limit'].innerText = int(value);
  character_limit = property_with_callback("character_limit", _set_character_limit)

  def _set_type(self, value):
    self.dom_nodes['textfield'].setAttribute("type", value)
  type = property_with_callback("type", _set_type)

  def _set_hide_text(self, value):
    self.dom_nodes['textfield'].setAttribute("type", "password" if value else self.type)
  hide_text = property_with_callback("hide_text", _set_hide_text)

  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")

