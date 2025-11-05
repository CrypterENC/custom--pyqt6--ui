# Color System Usage Guide

## Overview

All colors are now centralized in the `colors/color_palette.py` module. This makes it easy to define colors once and use them everywhere.

## File Structure

```
custom_ui_package/
├── colors/
│   ├── __init__.py
│   └── color_palette.py      # All color definitions and utilities
├── custom_main_window.py
├── custom_label.py
├── custom_button.py
├── custom_titlebar.py
├── custom_dialog.py
├── custom_dropdown.py
└── __init__.py
```

## How to Use Colors in Your App

### 1. Set Global Colors (in demo.py or your main file)

```python
from custom_ui_package import set_global_color_palette

# Define your color palette once at app startup
set_global_color_palette({
    'primary': '#a855f7',           # Main accent color
    'secondary': '#e9d5ff',         # Secondary accent color
    'background': '#1a0f2e',        # Background color
    'surface': '#2d1b4e',           # Surface color
    'text': '#f3e8ff',              # Text color
    'border': 'rgba(168, 85, 247, 0.3)',      # Border color
    'border_hover': 'rgba(168, 85, 247, 0.1)', # Border hover
})
```

### 2. Get Colors in Your Components

```python
from custom_ui_package import get_global_color

# Get a single color
primary_color = get_global_color('primary')
text_color = get_global_color('text')

# With default fallback
color = get_global_color('custom_key', default='#ffffff')
```

### 3. Create Backgrounds (Single or Gradient)

```python
from custom_ui_package import create_background_style

# Single color background
single_bg = create_background_style('#a855f7')
# Result: "background: #a855f7;"

# Gradient background
gradient_bg = create_background_style('#a855f7', '#1a0f2e')
# Result: "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #a855f7, stop:1 #1a0f2e);"
```

## Example: Using in demo.py

```python
from custom_ui_package import (
    CustomMainWindow, 
    set_global_color_palette,
    get_global_color,
    create_background_style
)

# Set colors once
set_global_color_palette({
    'primary': '#a855f7',
    'secondary': '#e9d5ff',
    'background': '#1a0f2e',
    'surface': '#2d1b4e',
    'text': '#f3e8ff',
    'border': 'rgba(168, 85, 247, 0.3)',
    'border_hover': 'rgba(168, 85, 247, 0.1)',
})

class DemoWindow(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='Custom UI Demo',
            width=600,
            height=850,
        )

        # Use colors from global palette
        self.set_titlebar_theme(
            bg_start=self.get_global_color('primary'),
            bg_end=self.get_global_color('background'),
            text_color=self.get_global_color('text'),
            border_color=self.get_global_color('border'),
            border_bg=self.get_global_color('border_hover')
        )

        # Create label with custom color
        self.create_custom_label(
            text='Custom UI Components',
            size=(310, 30),
            position=(30, 100),
            font_size=20,
            bold=True,
            color=self.get_global_color('text')  # Use global color
        )
```

## Supported Color Formats

- **Hex**: `'#a855f7'`
- **RGBA**: `'rgba(168, 85, 247, 0.3)'`
- **RGB**: `'rgb(168, 85, 247)'`

## Default Color Palette

```python
{
    'primary': '#a855f7',           # Vibrant purple
    'secondary': '#e9d5ff',         # Light lavender
    'background': '#1a0f2e',        # Dark purple
    'surface': '#2d1b4e',           # Medium dark purple
    'text': '#f3e8ff',              # Very light purple/white
    'border': 'rgba(168, 85, 247, 0.3)',      # Purple with 30% opacity
    'border_hover': 'rgba(168, 85, 247, 0.1)', # Purple with 10% opacity
}
```

## Key Functions

### `set_global_color_palette(palette)`
Set the global color palette for all UI elements.

**Args:**
- `palette` (dict): Color palette dictionary

**Example:**
```python
set_global_color_palette({'primary': '#ff0000'})
```

### `get_global_color(key, default='#ffffff')`
Get a color from the global palette.

**Args:**
- `key` (str): Color key (e.g., 'primary', 'text')
- `default` (str): Default color if key not found

**Returns:**
- str: Color value (hex or rgba)

**Example:**
```python
color = get_global_color('primary')
```

### `create_background_style(color_start, color_end=None)`
Create a background style supporting single or gradient colors.

**Args:**
- `color_start` (str): Single color or gradient start color
- `color_end` (str, optional): Gradient end color

**Returns:**
- str: CSS background style

**Examples:**
```python
# Single color
style = create_background_style('#a855f7')

# Gradient
style = create_background_style('#a855f7', '#1a0f2e')
```

## Benefits

✅ Define colors once, use everywhere  
✅ Easy to change theme globally  
✅ Supports hex, rgba, and rgb formats  
✅ All components automatically use global palette  
✅ Centralized color management  
✅ Support for both single and gradient colors  
✅ No color code scattered across components  
