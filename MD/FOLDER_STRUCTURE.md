# Folder Structure - custom-ui-pyqt6

Your project has been reorganized with a proper package structure for PyPI distribution.

## Current Structure

```
custom_ui/
│
├── custom_ui_package/              ← Main package folder (NEW)
│   ├── __init__.py                 ← Package initialization & public API
│   ├── custom_dialog.py            ← Message dialog component
│   ├── custom_dropdown.py          ← Dropdown component
│   ├── custom_titlebar.py          ← Title bar component
│   └── custom_ui_styles.qss        ← Stylesheet
│
├── setup.py                        ← Setup configuration
├── pyproject.toml                  ← Modern packaging config
├── MANIFEST.in                     ← File inclusion rules
├── LICENSE                         ← MIT License
├── requirements.txt                ← Dependencies
├── .gitignore                      ← Git ignore patterns
│
├── README.md                       ← User documentation
├── PUBLISHING_GUIDE.md             ← PyPI publishing guide
├── PACKAGE_SETUP.md                ← Setup overview
├── QUICK_REFERENCE.md              ← Quick reference
├── CHANGELOG.md                    ← Version history
├── SETUP_COMPLETE.txt              ← Setup summary
├── FOLDER_STRUCTURE.md             ← This file
│
├── demo.py                         ← Demo application (old location)
├── custom_dialog.py                ← Old location (can be deleted)
├── custom_dropdown.py              ← Old location (can be deleted)
├── custom_titlebar.py              ← Old location (can be deleted)
├── custom_ui_styles.qss            ← Old location (can be deleted)
└── __pycache__/                    ← Python cache
```

## What Changed

### ✅ New Organization
- All component files moved to `custom_ui_package/` folder
- Cleaner project root with only configuration and documentation
- Proper Python package structure for PyPI

### ✅ Benefits
- Professional package layout
- Easy to maintain and scale
- Follows Python packaging best practices
- Ready for PyPI distribution

## Updating Imports

### Before (Old Structure)
```python
from custom_ui.custom_dialog import CustomMessageDialog
from custom_ui.custom_dropdown import CustomDropdown
from custom_ui.custom_titlebar import CustomTitleBar
```

### After (New Structure)
```python
from custom_ui_package import CustomMessageDialog, CustomDropdown, CustomTitleBar
```

Or with full imports:
```python
from custom_ui_package.custom_dialog import CustomMessageDialog
from custom_ui_package.custom_dropdown import CustomDropdown
from custom_ui_package.custom_titlebar import CustomTitleBar
```

## Cleanup (Optional)

You can safely delete the old component files from the root:
- `custom_dialog.py`
- `custom_dropdown.py`
- `custom_titlebar.py`
- `custom_ui_styles.qss`

They are now in `custom_ui_package/` folder.

## Update setup.py

The `setup.py` file already references the correct package:

```python
packages = find_packages(),
package_data = {
    "custom_ui_package": ["*.qss"],
},
```

This automatically finds the `custom_ui_package` folder.

## Update pyproject.toml

The `pyproject.toml` is also configured correctly:

```toml
[tool.setuptools]
packages = ["custom_ui_package"]

[tool.setuptools.package-data]
custom_ui_package = ["*.qss"]
```

## Testing the New Structure

Test that imports work correctly:

```bash
python -c "from custom_ui_package import CustomDropdown, CustomMessageDialog, CustomTitleBar; print('Success!')"
```

## Next Steps

1. **Update demo.py** (if you use it):
   - Change imports to use `custom_ui_package`

2. **Test locally**:
   ```bash
   python -m build
   pip install dist/custom-ui-pyqt6-1.0.0-py3-none-any.whl
   ```

3. **Publish to PyPI**:
   - Follow steps in `PUBLISHING_GUIDE.md`

4. **Clean up** (optional):
   - Delete old component files from root

## File Locations

| Component | Old Location | New Location |
|-----------|--------------|--------------|
| Dialog | `custom_dialog.py` | `custom_ui_package/custom_dialog.py` |
| Dropdown | `custom_dropdown.py` | `custom_ui_package/custom_dropdown.py` |
| Title Bar | `custom_titlebar.py` | `custom_ui_package/custom_titlebar.py` |
| Styles | `custom_ui_styles.qss` | `custom_ui_package/custom_ui_styles.qss` |
| Init | `__init__.py` | `custom_ui_package/__init__.py` |

## Package Name on PyPI

When published to PyPI, users will install with:
```bash
pip install custom-ui-pyqt6
```

And import with:
```python
from custom_ui_package import CustomDropdown
```

---

**Your package is now properly organized and ready for PyPI! 🎉**
