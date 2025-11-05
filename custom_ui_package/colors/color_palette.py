"""
Global color palette for all custom UI components
Define colors once and use them everywhere
"""

# Global color palette for centralized color management
GLOBAL_COLOR_PALETTE = {
    'primary': '#a855f7',
    'secondary': '#e9d5ff',
    'background': '#1a0f2e',
    'surface': '#2d1b4e',
    'text': '#f3e8ff',
    'border': 'rgba(168, 85, 247, 0.3)',
    'border_hover': 'rgba(168, 85, 247, 0.1)',
}


def create_background_style(color_start, color_end=None, gradient_angle=135, gradient_type='linear'):
    """
    Create a background style that supports both single and gradient colors.
    
    Args:
        color_start (str): Single color (hex/rgba) or gradient start color
        color_end (str, optional): Gradient end color. If None, uses single color
        gradient_angle (int): Gradient angle in degrees (0-360). Default: 135
            - 0° = left to right
            - 45° = diagonal (top-left to bottom-right)
            - 90° = top to bottom
            - 135° = diagonal (bottom-left to top-right)
            - 180° = right to left
        gradient_type (str): Type of gradient - 'linear' or 'radial'. Default: 'linear'
        
    Returns:
        str: CSS background style
        
    Examples:
        Single color: create_background_style('#a855f7')
        Linear gradient: create_background_style('#a855f7', '#1a0f2e')
        Vertical gradient: create_background_style('#a855f7', '#1a0f2e', gradient_angle=90)
        Radial gradient: create_background_style('#a855f7', '#1a0f2e', gradient_type='radial')
    """
    if color_end is None:
        # Single color
        return f"background: {color_start};"
    else:
        if gradient_type == 'radial':
            # Radial gradient (center to edges)
            return f"background: qradialgradient(cx:0.5, cy:0.5, radius:0.7, stop:0 {color_start}, stop:1 {color_end});"
        else:
            # Linear gradient with angle support
            import math
            angle_rad = math.radians(gradient_angle)
            x2 = round(math.cos(angle_rad), 2)
            y2 = round(math.sin(angle_rad), 2)
            return f"background: qlineargradient(x1:0, y1:0, x2:{x2}, y2:{y2}, stop:0 {color_start}, stop:1 {color_end});"


def create_multi_stop_gradient(stops, gradient_angle=135, gradient_type='linear'):
    """
    Create a gradient with multiple color stops for advanced effects.
    
    Args:
        stops (list): List of tuples (position, color) where position is 0-1
            Example: [(0, '#ff0000'), (0.5, '#00ff00'), (1, '#0000ff')]
        gradient_angle (int): Gradient angle in degrees (0-360). Default: 135
        gradient_type (str): Type of gradient - 'linear' or 'radial'. Default: 'linear'
        
    Returns:
        str: CSS background style with multiple stops
        
    Examples:
        # Three-color gradient
        stops = [(0, '#ff0000'), (0.5, '#00ff00'), (1, '#0000ff')]
        create_multi_stop_gradient(stops, gradient_angle=90)
        
        # Smooth transition with 4 colors
        stops = [(0, '#a855f7'), (0.33, '#ec4899'), (0.66, '#f97316'), (1, '#1a0f2e')]
        create_multi_stop_gradient(stops)
    """
    if not stops or len(stops) < 2:
        return "background: #ffffff;"
    
    # Build stop string
    stop_str = ', '.join([f"stop:{pos} {color}" for pos, color in stops])
    
    if gradient_type == 'radial':
        return f"background: qradialgradient(cx:0.5, cy:0.5, radius:0.7, {stop_str});"
    else:
        import math
        angle_rad = math.radians(gradient_angle)
        x2 = round(math.cos(angle_rad), 2)
        y2 = round(math.sin(angle_rad), 2)
        return f"background: qlineargradient(x1:0, y1:0, x2:{x2}, y2:{y2}, {stop_str});"


def get_global_color(key, default='#ffffff'):
    """
    Get a color from the global palette.
    
    Args:
        key (str): Color key (e.g., 'primary', 'text', 'border')
        default (str): Default color if key not found
        
    Returns:
        str: Color value (hex or rgba)
    """
    return GLOBAL_COLOR_PALETTE.get(key, default)


def set_global_color_palette(palette):
    """
    Set the global color palette for all UI elements.
    This allows you to define colors once and use them everywhere.
    
    Args:
        palette (dict): Color palette with keys like:
            - primary: Main accent color (hex or rgba)
            - secondary: Secondary accent color (hex or rgba)
            - background: Background color (hex or rgba)
            - surface: Surface color (hex or rgba)
            - text: Text color (hex or rgba)
            - border: Border color (hex or rgba)
            - border_hover: Border hover color (hex or rgba)
    
    Example:
        set_global_color_palette({
            'primary': '#59ff1b',
            'secondary': '#a5f3fc',
            'background': '#0a0e27',
            'surface': '#0f1535',
            'text': '#f3e8ff',
            'border': 'rgba(168, 85, 247, 0.3)',
            'border_hover': 'rgba(168, 85, 247, 0.1)',
        })
    """
    global GLOBAL_COLOR_PALETTE
    GLOBAL_COLOR_PALETTE.update(palette)
