"""
Comprehensive Demo of Custom UI Components
Showcases all parameters and features of all custom UI components
"""

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from custom_ui_package import (
    CustomMainWindow,
    CustomButton,
    CustomLabel,
    CustomDropdown,
    CustomDropdownCompact,
    CustomDropdownLarge,
    CustomMessageDialog,
    CustomTitleBar,
    CustomMenu,
    CustomScrollBar,
    CustomVerticalScrollBar,
    set_global_color_palette,
    get_global_color,
    create_background_style,
    create_multi_stop_gradient,
)

from auto_live_reload import start_auto_live_reload

start_auto_live_reload(__file__)

# ===================================
# 1. Global Color Palette Setup
# ===================================
set_global_color_palette({
    'primary': '#a855f7',           # Purple - Main accent
    'secondary': '#e9d5ff',         # Light purple
    'background': '#1a0f2e',        # Dark purple-blue
    'surface': '#2d1b4e',           # Medium purple-blue
    'text': '#f3e8ff',              # Light text
    'border': 'rgba(168, 85, 247, 0.3)',      # Purple border
    'border_hover': 'rgba(168, 85, 247, 0.1)', # Subtle border
})


class ShowCase(CustomMainWindow):
    def __init__(self):
        super().__init__(
            title='Custom UI Components - Comprehensive Demo',
            width=1000,
            height=550,
            icon_path=None,
            show_title_bar=True,
            show_minimize=True,
            show_close=True,
            bg_color='#1a0f2e',
            bg_color_end='#2d1b4e',
            gradient_angle=90,
            gradient_type='linear',
            content_margins=(40, 30, 40, 30),
            content_spacing=15,
        )

        # ===================================
        # Customize Title Bar (if enabled)
        # ===================================
        if self.title_bar:
            self.set_titlebar_theme(
                bg_start=get_global_color('primary'),
                bg_end=get_global_color('background'),
                text_color=get_global_color('text'),
                border_color=get_global_color('border'),
                border_bg=get_global_color('border_hover')
            )
        
        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        pass
        # title = QLabel('🎨 Custom UI Components Demo')
        # title.setFont(QFont('Segoe UI', 24, QFont.Weight.Bold))
        # title.setStyleSheet(f"color: {get_global_color('text')};")
        # self.add_content(title)


def main():
    app = QApplication(sys.argv)
    showcase = ShowCase()
    showcase.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()