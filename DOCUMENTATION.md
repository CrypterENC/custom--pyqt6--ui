# Custom UI Components for PyQt6 - Complete Documentation

[![PyPI version](https://badge.fury.io/py/custom-ui-pyqt6.svg)](https://badge.fury.io/py/custom-ui-pyqt6)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Modern, reusable PyQt6 UI components with glassmorphism effects and smooth animations. Perfect for building beautiful, modern desktop applications.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Component Reference](#component-reference)
   - [CustomMainWindow](#custommainwindow)
   - [CustomTitleBar](#customtitlebar)
   - [CustomButton](#custombutton)
   - [CustomLabel](#customlabel)
   - [CustomDropdown](#customdropdown)
   - [CustomMessageDialog](#custommessagedialog)
   - [CustomMenu](#custommenu)
   - [CustomScrollBar](#customscrollbar)
5. [CustomMainWindow Guide](#custommainwindow-guide)
6. [Gradient System](#gradient-system)
   - [Linear Gradients](#linear-gradients)
   - [Radial Gradients](#radial-gradients)
   - [Multi-Stop Gradients](#multi-stop-gradients)
7. [Theming System](#theming-system)
8. [Color Palette](#color-palette)
9. [Global Color Management](#global-color-management)
10. [Customization](#customization)
   - [CustomMainWindow Customization](#custommainwindow-customization)
   - [CustomTitleBar Customization](#customtitlebar-customization)
   - [CustomDropdown Customization](#customdropdown-customization)
   - [CustomMessageDialog Customization](#custommessagedialog-customization)
11. [Examples](#examples)
12. [Components Overview](#components-overview)
13. [Requirements](#requirements)
14. [Tips & Best Practices](#tips--best-practices)
15. [Contributing](#contributing)
16. [License](#license)

---

## Features

✨ **Modern Design**
- Gradient backgrounds
- Semi-transparent glassmorphism effects
- Smooth hover transitions
- Professional typography

🎯 **User-Friendly**
- Draggable windows
- Clear visual hierarchy
- Intuitive interactions
- Responsive feedback

🔄 **Reusable**
- Easy to integrate into any PyQt6 project
- Customizable colors and styles
- Modular components
- Well-documented

🎨 **Themeable**
- 5 predefined color themes
- Runtime theme switching
- Custom color support
- Flexible styling system

---

## Installation

### From PyPI

```bash
pip install custom-ui-pyqt6
```

### From Source

```bash
git clone https://github.com/yourusername/custom-ui-pyqt6.git
cd custom-ui-pyqt6
pip install -e .
```

---

## Quick Start

### Basic Window Setup

```python
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtGui import QFont
from custom_ui_package import CustomMainWindow

class MyApp(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='My Application',
            width=600,
            height=750,
            # Single color background
            bg_color='#1a0f2e'
        )
        
        # Add content
        title = QLabel('Welcome!')
        title.setFont(QFont('Segoe UI', 20, QFont.Weight.Bold))
        self.add_content(title)
        
        btn = QPushButton('Click Me')
        self.add_content(btn)
        
        self.add_stretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
```

---

## Component Reference

### CustomMainWindow

A frameless main window with custom title bar and customizable styling.

**Constructor Parameters:**
```python
CustomMainWindow(
    title='Custom Window',           # Window title
    width=600,                       # Window width in pixels
    height=750,                      # Window height in pixels
    icon_path=None,                  # Path to window icon
    show_minimize=True,              # Show minimize button
    show_close=True,                 # Show close button
    show_title_bar=True,             # Show custom title bar
    bg_color=None,                   # Background color (single or gradient start)
    bg_color_end=None,               # Gradient end color (if None, uses single color)
    gradient_angle=135,              # Gradient angle in degrees (0-360)
    custom_colors=None               # Custom color overrides
)
```

**Key Methods:**
- `add_content(widget)` - Add widget to content area
- `add_stretch()` - Add stretch to push content to top
- `set_title(title)` - Update window title
- `set_theme(theme_name)` - Change theme
- `set_custom_colors(colors_dict)` - Override colors
- `get_theme_colors()` - Get current colors
- `set_content_margins(left, top, right, bottom)` - Set margins
- `set_content_spacing(spacing)` - Set widget spacing

**Example:**
```python
from custom_ui_package import CustomMainWindow

# Single color background
window = CustomMainWindow(
    title='My App',
    width=700,
    height=600,
    bg_color='#1a0f2e'
)

# Gradient background with custom angle
window = CustomMainWindow(
    title='My App',
    width=700,
    height=600,
    bg_color='#1a0f2e',
    bg_color_end='#2d1b4e',
    gradient_angle=90  # Top to bottom
)

# Without title bar
window = CustomMainWindow(
    title='My App',
    width=700,
    height=600,
    bg_color='#1a0f2e',
    show_title_bar=False
)

# Get current colors
colors = window.get_theme_colors()
print(colors['text_primary'])
```

---

### CustomDropdown

A modern dropdown/combobox widget with glassmorphism effects.

**Features:**
- Smooth animations
- Custom colors
- Icon support
- Multiple size variants

**Variants:**
- `CustomDropdown` - Standard size
- `CustomDropdownCompact` - Compact size
- `CustomDropdownLarge` - Large size

**Key Methods:**
- `add_items_with_icons(items_dict)` - Add items with optional icons
- `get_selected_text()` - Get selected item text
- `get_selected_value()` - Get selected item value
- `set_custom_colors(bg_color, border_color, text_color, hover_color)` - Customize colors

**Example:**
```python
from custom_ui_package import CustomDropdown, CustomDropdownCompact, CustomDropdownLarge

# Standard dropdown
dropdown = CustomDropdown()
dropdown.add_items_with_icons({
    'Option 1': 'value1',
    'Option 2': 'value2',
    'Option 3': 'value3'
})

# Compact version
compact = CustomDropdownCompact()
compact.add_items_with_icons({'A': 'a', 'B': 'b'})

# Large version
large = CustomDropdownLarge()
large.add_items_with_icons({'Item 1': 'i1', 'Item 2': 'i2'})

# Custom colors
dropdown.set_custom_colors(
    bg_color='rgba(20, 25, 50, 0.8)',
    border_color='#7c3aed',
    text_color='#e0e7ff',
    hover_color='#a78bfa'
)

# Get selected value
selected_text = dropdown.get_selected_text()
selected_value = dropdown.get_selected_value()
```

---

### CustomMessageDialog

A modern message dialog with draggable interface and icon support.

**Icon Types:**
- `'info'` - Information icon
- `'warning'` - Warning icon
- `'error'` - Error icon

**Example:**
```python
from custom_ui_package import CustomMessageDialog

# Info dialog
dialog = CustomMessageDialog(
    'Information',
    'This is an info message',
    'info',
    parent_widget
)
dialog.exec()

# Warning dialog
dialog = CustomMessageDialog(
    'Warning',
    'This is a warning message',
    'warning',
    parent_widget
)
dialog.exec()

# Error dialog
dialog = CustomMessageDialog(
    'Error',
    'This is an error message',
    'error',
    parent_widget
)
dialog.exec()
```

---

### CustomTitleBar

A modern custom title bar for frameless windows with configurable colors.

**Features:**
- Draggable window
- Minimize button (optional)
- Close button (optional)
- Icon support
- Custom title
- Configurable single or gradient background colors

**Constructor Parameters:**
```python
CustomTitleBar(
    parent=None,                     # Parent widget
    title="Application",            # Title bar text
    icon_path=None,                  # Path to window icon
    show_minimize=True,              # Show minimize button
    show_close=True,                 # Show close button
    bg_color=None,                   # Background color (single or gradient start)
    bg_color_end=None,               # Gradient end color (if None, uses single color)
    text_color=None,                 # Title text color
    border_color=None,               # Border color
    border_bg=None                   # Button hover background color
)
```

**Example:**
```python
from custom_ui_package import CustomTitleBar
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Create custom title bar with single color
        title_bar = CustomTitleBar(
            parent=self,
            title="My Application",
            icon_path="path/to/icon.png",
            show_minimize=True,
            show_close=True,
            bg_color='#a855f7'
        )
        
        # Or with gradient
        # title_bar = CustomTitleBar(
        #     parent=self,
        #     title="My Application",
        #     bg_color='#a855f7',
        #     bg_color_end='#1a0f2e'
        # )
        
        # Add to layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(title_bar)
        # Add your content here
        self.setCentralWidget(central_widget)
```

---

### CustomButton

A reusable, fully‑configurable button widget.

**Constructor Parameters:**
```python
CustomButton(
    parent=None,
    title="Button",
    size=(100, 30),   # width, height in pixels
    position=(0, 0),   # x, y coordinates (ignored when added via layout)
    font_size=10,
)
```

**Example Usage:**
```python
from custom_ui_package.custom_button import CustomButton

btn = CustomButton(
    parent=self,
    title="Press Me",
    size=(150, 45),
    font_size=12,
)
btn.clicked.connect(lambda: print("Custom button clicked!"))
self.add_content(btn)
```

---

### CustomLabel

A reusable, customizable label widget with global color palette support.

**Constructor Parameters:**
```python
CustomLabel(
    parent=None,
    text="Label",
    size=(100, 30),      # width, height in pixels
    position=(0, 0),     # x, y coordinates
    font_size=10,
    bold=False,
    color=None           # Text color (uses global palette if None)
)
```

**Key Methods:**
- `set_position(x, y)` - Change label position at runtime

**Example Usage:**
```python
from custom_ui_package import CustomLabel

# Basic label
label = CustomLabel(
    parent=self,
    text="Hello World",
    size=(150, 30),
    font_size=12,
    bold=True
)

# With custom color
label = CustomLabel(
    parent=self,
    text="Custom Color Label",
    color='#a855f7',
    font_size=14
)

# Update position at runtime
label.set_position(100, 50)
```

---

### CustomMenu

A modern menu component with glassmorphism effects and smooth animations.

**Constructor Parameters:**
```python
CustomMenu(
    parent=None,
    title='',                          # Menu title
    bg_color=None,                     # Background color (uses global surface)
    text_color=None,                   # Text color (uses global text)
    hover_color=None,                  # Hover color (uses global primary)
    border_color=None,                 # Border color (uses global border)
    border_width=1,                    # Border width in pixels
    border_radius=8,                   # Border radius in pixels
    font_size=11,                      # Font size in pixels
    font_family='Segoe UI',            # Font family
    bold=False,                        # Bold font
    opacity=0.95,                      # Background opacity (0-1)
    icon_size=16,                      # Icon size in pixels
    item_height=32,                    # Menu item height
    item_padding=10,                   # Item padding in pixels
    animation_duration=150             # Animation duration in ms
)
```

**Key Methods:**
- `add_item(text, callback=None, icon_path=None, shortcut=None, enabled=True, checkable=False, checked=False)` - Add menu item
- `add_separator()` - Add separator line
- `add_submenu(title, parent=None)` - Add submenu
- `update_colors(bg_color, text_color, hover_color, border_color)` - Update colors at runtime
- `update_styling(font_size, font_family, bold, border_radius, item_height, item_padding)` - Update styling
- `set_opacity(opacity)` - Set background opacity
- `clear_items()` - Clear all items
- `get_item_by_text(text)` - Get item by text
- `enable_item(text, enabled)` - Enable/disable item
- `check_item(text, checked)` - Check/uncheck item
- `is_item_checked(text)` - Check if item is checked

**Signals:**
- `item_hovered(QAction)` - Emitted when item is hovered
- `item_clicked(QAction)` - Emitted when item is clicked

**Example Usage:**
```python
from custom_ui_package import CustomMenu

# Basic menu
menu = CustomMenu(title='File')
menu.add_item('New', callback=lambda: print('New'))
menu.add_item('Open', callback=lambda: print('Open'))
menu.add_separator()
menu.add_item('Exit', callback=lambda: print('Exit'))

# Custom colors
menu = CustomMenu(
    title='Edit',
    bg_color='#1a0f2e',
    text_color='#f3e8ff',
    hover_color='#a855f7',
    border_color='rgba(168, 85, 247, 0.3)'
)

# With icons and shortcuts
menu.add_item('Copy', icon_path='path/to/copy.png', shortcut='Ctrl+C')
menu.add_item('Paste', icon_path='path/to/paste.png', shortcut='Ctrl+V')

# Submenu
submenu = menu.add_submenu('Recent Files')
submenu.add_item('File 1.txt')
submenu.add_item('File 2.txt')

# Checkable items
menu.add_item('Show Grid', checkable=True, checked=True)

# Connect to signals
menu.item_clicked.connect(lambda action: print(f"Clicked: {action.text()}"))
```

---

### CustomScrollBar

A modern scrollbar component with glassmorphism effects.

**Constructor Parameters:**
```python
CustomScrollBar(
    orientation=Qt.Orientation.Vertical,  # Qt.Vertical or Qt.Horizontal
    parent=None,
    handle_color=None,                    # Handle color (uses global primary)
    handle_hover_color=None,              # Hover color (auto-lightened)
    background_color=None,                # Background color (uses global surface)
    border_color=None,                    # Border color (uses global border)
    border_width=1,                       # Border width in pixels
    border_radius=6,                      # Border radius in pixels
    handle_width=8,                       # Handle width (for vertical)
    handle_height=8,                      # Handle height (for horizontal)
    opacity=0.9,                          # Background opacity (0-1)
    hover_opacity=1.0,                    # Hover opacity (0-1)
    min_handle_size=20                    # Minimum handle size
)
```

**Variants:**
- `CustomScrollBar` - Generic scrollbar
- `CustomVerticalScrollBar` - Vertical scrollbar (convenience class)
- `CustomHorizontalScrollBar` - Horizontal scrollbar (convenience class)

**Key Methods:**
- `update_colors(handle_color, handle_hover_color, background_color, border_color)` - Update colors
- `update_styling(handle_width, handle_height, border_radius, opacity, hover_opacity)` - Update styling
- `set_opacity(opacity)` - Set background opacity
- `set_hover_opacity(opacity)` - Set hover opacity

**Example Usage:**
```python
from custom_ui_package import CustomVerticalScrollBar, CustomHorizontalScrollBar
from PyQt6.QtCore import Qt

# Vertical scrollbar
v_scrollbar = CustomVerticalScrollBar(
    handle_color='#a855f7',
    handle_hover_color='#d946ef',
    background_color='#1a0f2e'
)

# Horizontal scrollbar
h_scrollbar = CustomHorizontalScrollBar(
    handle_color='#a855f7',
    handle_hover_color='#d946ef'
)

# Custom styling
scrollbar = CustomVerticalScrollBar(
    handle_width=12,
    border_radius=8,
    opacity=0.8,
    hover_opacity=1.0
)

# Update colors at runtime
scrollbar.update_colors(
    handle_color='#ec4899',
    background_color='#2d1b4e'
)

# Update styling at runtime
scrollbar.update_styling(
    handle_width=10,
    border_radius=6,
    opacity=0.7
)
```

---

## CustomMainWindow Guide

### Creating a Custom Window

```python
from custom_ui_package import CustomMainWindow
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtGui import QFont
import sys

class MyApp(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='My Application',
            width=600,
            height=750,
            theme='dark_blue'
        )
        
        # Add widgets
        self.setup_ui()
    
    def setup_ui(self):
        title = QLabel('Welcome to My App')
        title.setFont(QFont('Segoe UI', 20, QFont.Weight.Bold))
        self.add_content(title)
        
        btn = QPushButton('Click Me')
        btn.clicked.connect(self.on_button_click)
        self.add_content(btn)
        
        self.add_stretch()
    
    def on_button_click(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
```

### Layout Control

```python
# Set custom margins (left, top, right, bottom)
window.set_content_margins(50, 40, 50, 40)

# Set spacing between widgets
window.set_content_spacing(20)

# Add content
window.add_content(widget)

# Add stretch to push content to top
window.add_stretch()
```

---

## Gradient System

The gradient system provides flexible control over background gradients with support for linear, radial, and multi-stop gradients.

### Linear Gradients

Create smooth directional gradients with angle control:

```python
from custom_ui_package import CustomMainWindow, create_background_style

# Vertical gradient (top to bottom)
window = CustomMainWindow(
    title='My App',
    bg_color='#a855f7',
    bg_color_end='#1a0f2e',
    gradient_angle=90
)

# Horizontal gradient (left to right)
window = CustomMainWindow(
    title='My App',
    bg_color='#a855f7',
    bg_color_end='#1a0f2e',
    gradient_angle=0
)

# Diagonal gradient (45 degrees)
window = CustomMainWindow(
    title='My App',
    bg_color='#a855f7',
    bg_color_end='#1a0f2e',
    gradient_angle=45
)
```

**Gradient Angle Reference:**
- **0°** = left to right (horizontal)
- **45°** = diagonal (top-left to bottom-right)
- **90°** = top to bottom (vertical)
- **135°** = diagonal (bottom-left to top-right)
- **180°** = right to left (horizontal)

### Radial Gradients

Create circular gradients that radiate from the center:

```python
from custom_ui_package import CustomMainWindow

# Radial gradient (circular from center)
window = CustomMainWindow(
    title='My App',
    bg_color='#a855f7',
    bg_color_end='#1a0f2e',
    gradient_type='radial'
)
```

### Multi-Stop Gradients

Create advanced gradients with multiple color stops:

```python
from custom_ui_package import create_multi_stop_gradient

# Three-color gradient
stops = [(0, '#ff0000'), (0.5, '#00ff00'), (1, '#0000ff')]
style = create_multi_stop_gradient(stops, gradient_angle=90)

# Four-color smooth transition
stops = [(0, '#a855f7'), (0.33, '#ec4899'), (0.66, '#f97316'), (1, '#1a0f2e')]
style = create_multi_stop_gradient(stops)

# Radial multi-stop gradient
style = create_multi_stop_gradient(stops, gradient_type='radial')
```

### Using `create_background_style()`

Create background styles with full gradient control:

```python
from custom_ui_package import create_background_style

# Single color
style = create_background_style('#a855f7')

# Linear gradient with angle
style = create_background_style('#a855f7', '#1a0f2e', gradient_angle=90)

# Radial gradient
style = create_background_style('#a855f7', '#1a0f2e', gradient_type='radial')
```

---

## Theming System

### Configurable Colors

Custom UI components now support flexible color configuration:

- **Single Color** - Use a single solid color for backgrounds
- **Gradient Colors** - Use two colors for gradient backgrounds
- **Hex Format** - Standard hex color codes (#RRGGBB)
- **RGBA Format** - RGBA colors with transparency (rgba(r, g, b, a))

### Using Single Color

```python
from custom_ui_package import CustomMainWindow

# Create window with single color background
window = CustomMainWindow(
    title='My App',
    width=600,
    height=750,
    bg_color='#1a0f2e'
)
```

### Using Gradient Colors

```python
from custom_ui_package import CustomMainWindow

# Create window with gradient background
window = CustomMainWindow(
    title='My App',
    width=600,
    height=750,
    bg_color='#1a0f2e',        # Gradient start
    bg_color_end='#2d1b4e'     # Gradient end
)
```

### Custom Color Overrides

You can override specific colors:

```python
# Create with custom color overrides
custom_colors = {
    'button_start': '#ff6b6b',
    'button_end': '#ee5a6f',
    'button_hover_start': '#ff8787',
    'button_hover_end': '#ff6b6b',
}

window = CustomMainWindow(
    title='My App',
    bg_color='#1a1a2e',
    custom_colors=custom_colors
)
```

### Global Color Palette

Define colors once and use them everywhere:

```python
from custom_ui_package import set_global_color_palette, get_global_color

# Set global palette at app startup
set_global_color_palette({
    'primary': '#a855f7',
    'secondary': '#e9d5ff',
    'background': '#1a0f2e',
    'surface': '#2d1b4e',
    'text': '#f3e8ff',
    'border': 'rgba(168, 85, 247, 0.3)',
    'border_hover': 'rgba(168, 85, 247, 0.1)',
})

# Use colors throughout your app
color = get_global_color('primary')
```

### Update Colors at Runtime

```python
# Change colors after window creation
new_colors = {
    'button_start': '#ff1493',
    'button_end': '#ff69b4',
}

window.set_custom_colors(new_colors)
```

### Get Current Theme Colors

```python
# Retrieve current color configuration
current_colors = window.get_theme_colors()
print(current_colors)

# Use colors for child widgets
colors = window.get_theme_colors()
label.setStyleSheet(f"color: {colors['text_primary']};")
```

---

## Color Palette

### Default Color Scheme

| Color | Hex | Usage |
|-------|-----|-------|
| Primary | #6366f1 | Indigo - Main buttons |
| Secondary | #4f46e5 | Purple - Button end gradient |
| Accent | #a5f3fc | Cyan - Secondary text |
| Background | #0a0e27 | Dark Blue - Window background |
| Text Primary | #e8f0ff | Light Blue - Main text |
| Text Secondary | #a5f3fc | Cyan - Secondary text |
| Warning | #eab308 | Yellow - Warning elements |
| Error | #ef4444 | Red - Error elements |
| Success | #10b981 | Green - Success elements |

### Color Keys Reference

All color dictionaries should include these keys:

| Key | Purpose |
|-----|---------|
| `bg_gradient_start` | Background gradient start color |
| `bg_gradient_end` | Background gradient end color |
| `button_start` | Button gradient start color |
| `button_end` | Button gradient end color |
| `button_hover_start` | Button hover gradient start |
| `button_hover_end` | Button hover gradient end |
| `button_pressed_start` | Button pressed gradient start |
| `button_pressed_end` | Button pressed gradient end |
| `text_primary` | Primary text color |
| `text_secondary` | Secondary text color |
| `border_color` | Border color (usually with alpha) |
| `border_bg` | Border background color (usually with alpha) |

---

## Global Color Management

Centralize color management across your entire application using the global color palette system.

### Setting Global Colors

Define your color palette once at application startup:

```python
from custom_ui_package import set_global_color_palette, get_global_color

# Set global palette at app startup
set_global_color_palette({
    'primary': '#a855f7',
    'secondary': '#e9d5ff',
    'background': '#1a0f2e',
    'surface': '#2d1b4e',
    'text': '#f3e8ff',
    'border': 'rgba(168, 85, 247, 0.3)',
    'border_hover': 'rgba(168, 85, 247, 0.1)',
})
```

### Using Global Colors

Access colors throughout your application:

```python
from custom_ui_package import get_global_color

# Get a color from the global palette
primary_color = get_global_color('primary')
text_color = get_global_color('text', default='#ffffff')

# Use in components
label.setStyleSheet(f"color: {get_global_color('text')};")
```

### Benefits

- **Define Once, Use Everywhere** - Set colors once, use in all components
- **Easy Theme Switching** - Change entire theme by updating global palette
- **Consistent Styling** - Ensure color consistency across your app
- **Flexible Format Support** - Supports hex (#RRGGBB) and RGBA colors
- **Default Values** - Provide fallback colors if key not found

### Example: Theme Switching

```python
from custom_ui_package import set_global_color_palette

# Light theme
light_theme = {
    'primary': '#3b82f6',
    'background': '#ffffff',
    'text': '#1f2937',
}

# Dark theme
dark_theme = {
    'primary': '#a855f7',
    'background': '#1a0f2e',
    'text': '#f3e8ff',
}

# Switch themes at runtime
def switch_to_light():
    set_global_color_palette(light_theme)

def switch_to_dark():
    set_global_color_palette(dark_theme)
```

---

## Customization

### CustomMainWindow Customization

```python
from custom_ui_package import CustomMainWindow

window = CustomMainWindow(
    title='My App',
    width=700,
    height=600,
    icon_path='path/to/icon.png',
    show_minimize=True,
    show_close=True,
    show_title_bar=True,
    bg_color='#1a0f2e',
    bg_color_end='#2d1b4e',
    gradient_angle=90,
    gradient_type='linear'
)

# Customize layout
window.set_content_margins(50, 40, 50, 40)
window.set_content_spacing(20)

# Update colors
window.set_custom_colors({'button_end': '#ff69b4'})
```

### CustomTitleBar Customization

```python
from custom_ui_package import CustomTitleBar

title_bar = CustomTitleBar(
    parent=window,
    title='My Window',
    icon_path='path/to/icon.png',
    show_minimize=True,
    show_close=True,
    bg_color='#a855f7',
    bg_color_end='#1a0f2e',
    text_color='#f3e8ff',
    border_color='rgba(168, 85, 247, 0.3)',
    border_bg='rgba(168, 85, 247, 0.1)'
)
```

### CustomDropdown Customization

```python
from custom_ui_package import CustomDropdown

dropdown = CustomDropdown()

# Add items with icons
dropdown.add_items_with_icons({
    'Docker': 'docker',
    'Python': 'python',
    'JavaScript': 'javascript'
})

# Customize colors
dropdown.set_custom_colors(
    bg_color='rgba(20, 25, 50, 0.8)',
    border_color='#7c3aed',
    text_color='#e0e7ff',
    hover_color='#a78bfa'
)

# Connect to selection change
dropdown.currentIndexChanged.connect(lambda: print(dropdown.get_selected_text()))
```

### CustomMessageDialog Customization

```python
from custom_ui_package import CustomMessageDialog

# Create different types of dialogs
info_dialog = CustomMessageDialog('Info', 'Message text', 'info', parent)
warning_dialog = CustomMessageDialog('Warning', 'Message text', 'warning', parent)
error_dialog = CustomMessageDialog('Error', 'Message text', 'error', parent)

# Show dialog
info_dialog.exec()
```

### CustomTitleBar Customization

```python
from custom_ui_package import CustomTitleBar

title_bar = CustomTitleBar(
    parent=window,
    title='My Window',
    icon_path='path/to/icon.png',
    show_minimize=True,
    show_close=True
)
```

### CustomMainWindow Customization

```python
from custom_ui_package import CustomMainWindow

window = CustomMainWindow(
    title='My App',
    width=700,
    height=600,
    icon_path='path/to/icon.png',
    show_minimize=True,
    show_close=True,
    theme='dark_purple',
    custom_colors={'button_start': '#ff6b6b'}
)

# Customize layout
window.set_content_margins(50, 40, 50, 40)
window.set_content_spacing(20)

# Change theme
window.set_theme('dark_green')

# Update colors
window.set_custom_colors({'button_end': '#ff69b4'})
```

---

## Examples

### Example 1: Simple Application with Single Color

```python
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtGui import QFont
from custom_ui_package import CustomMainWindow

class SimpleApp(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='Simple App',
            width=500,
            height=400,
            bg_color='#1a0f2e'
        )
        
        title = QLabel('Hello World!')
        title.setFont(QFont('Segoe UI', 18, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {self.get_theme_colors()['text_primary']};")
        self.add_content(title)
        
        btn = QPushButton('Say Hello')
        btn.clicked.connect(lambda: print('Hello!'))
        self.add_content(btn)
        
        self.add_stretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())
```

### Example 2: Gradient Background

```python
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtGui import QFont
from custom_ui_package import CustomMainWindow

class GradientApp(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='Gradient App',
            width=600,
            height=500,
            bg_color='#1a0f2e',
            bg_color_end='#2d1b4e'
        )
        
        title = QLabel('Beautiful Gradient Background')
        title.setFont(QFont('Segoe UI', 16, QFont.Weight.Bold))
        self.add_content(title)
        
        description = QLabel('This window uses a gradient background')
        description.setStyleSheet(f"color: {self.get_theme_colors()['text_secondary']};")
        self.add_content(description)
        
        btn = QPushButton('Click Me')
        btn.clicked.connect(lambda: print('Button clicked!'))
        self.add_content(btn)
        
        self.add_stretch()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GradientApp()
    window.show()
    sys.exit(app.exec())
```

### Example 3: Complete Application with Custom Colors

```python
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel
from PyQt6.QtGui import QFont
from custom_ui_package import CustomMainWindow, CustomDropdown, CustomMessageDialog, set_global_color_palette

# Set global color palette
set_global_color_palette({
    'primary': '#a855f7',
    'secondary': '#e9d5ff',
    'background': '#1a0f2e',
    'surface': '#2d1b4e',
    'text': '#f3e8ff',
    'border': 'rgba(168, 85, 247, 0.3)',
    'border_hover': 'rgba(168, 85, 247, 0.1)',
})

class CompleteApp(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='Complete App',
            width=600,
            height=700,
            bg_color='#1a0f2e',
            bg_color_end='#2d1b4e'
        )
        
        # Title
        title = QLabel('Select Your Options')
        title.setFont(QFont('Segoe UI', 20, QFont.Weight.Bold))
        self.add_content(title)
        
        # Dropdown 1
        label1 = QLabel('Programming Language:')
        label1.setStyleSheet(f"color: {self.get_theme_colors()['text_secondary']};")
        self.add_content(label1)
        
        dropdown1 = CustomDropdown()
        dropdown1.add_items_with_icons({
            'Python': 'python',
            'JavaScript': 'javascript',
            'Go': 'go'
        })
        self.add_content(dropdown1)
        
        # Dropdown 2
        label2 = QLabel('Framework:')
        label2.setStyleSheet(f"color: {self.get_theme_colors()['text_secondary']};")
        self.add_content(label2)
        
        dropdown2 = CustomDropdown()
        dropdown2.add_items_with_icons({
            'Django': 'django',
            'Flask': 'flask',
            'FastAPI': 'fastapi'
        })
        self.add_content(dropdown2)
        
        # Submit button
        submit_btn = QPushButton('Submit')
        submit_btn.clicked.connect(
            lambda: self.show_selection(dropdown1, dropdown2)
        )
        self.add_content(submit_btn)
        
        self.add_stretch()
    
    def show_selection(self, dd1, dd2):
        msg = f"Language: {dd1.get_selected_text()}\nFramework: {dd2.get_selected_text()}"
        dialog = CustomMessageDialog('Selection', msg, 'info', self)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompleteApp()
    window.show()
    sys.exit(app.exec())
```

---

## Components Overview

| Component | Purpose | Features |
|-----------|---------|----------|
| `CustomMainWindow` | Main application window | Frameless, custom title bar, themeable, draggable |
| `CustomTitleBar` | Window title bar | Minimize/close buttons, draggable, icon support |
| `CustomButton` | Reusable button widget | Configurable size, font, position, global color support |
| `CustomLabel` | Reusable label widget | Configurable text, size, position, bold, global color support |
| `CustomDropdown` | Standard dropdown | Glassmorphism, smooth animations, custom colors |
| `CustomDropdownCompact` | Compact dropdown | Smaller height variant |
| `CustomDropdownLarge` | Large dropdown | Larger height variant |
| `CustomMessageDialog` | Message dialog | Frameless, draggable, icon support |
| `CustomMenu` | Context/application menu | Glassmorphism, icons, submenus, checkable items, custom colors |
| `CustomScrollBar` | Custom scrollbar | Glassmorphism, smooth animations, vertical/horizontal |
| `CustomVerticalScrollBar` | Vertical scrollbar | Convenience class for vertical orientation |
| `CustomHorizontalScrollBar` | Horizontal scrollbar | Convenience class for horizontal orientation |

---

## Requirements

- Python 3.8+
- PyQt6 >= 6.0.0

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/yourusername/custom-ui-pyqt6/issues).

---

## Tips & Best Practices

- Use `get_theme_colors()` to access current colors for styling child widgets
- Use `set_global_color_palette()` at app startup to define colors once
- Color values support both hex (#RRGGBB) and rgba() formats
- For gradient backgrounds, provide both `bg_color` and `bg_color_end`
- For single color backgrounds, only provide `bg_color`
- Custom colors override default colors without replacing the entire theme
- For better UX, use consistent spacing and margins across your application
- Consider using the same color palette throughout your application for visual consistency
- Test your custom colors with different lighting conditions
- Use RGBA colors for transparency effects (e.g., borders with alpha channel)
