# Quick Setup Guide

## ✅ Setup Complete!

Python and all dependencies are now installed. Here's how to run your tests:

## 🚀 Running Tests

### Using Python Module (Recommended on Windows):
```powershell
# Run all tests
py -m pytest

# Run specific test file
py -m pytest tests/test_validation.py -v

# Run specific test
py -m pytest tests/test_validation.py::TestLoginFieldValidation::test_username_field_exists -v

# Run with markers
py -m pytest -m smoke -v
py -m pytest -m validation -v

# Run with HTML report
py -m pytest --html=report.html --self-contained-html
```

### In VS Code:
1. **Open Testing Panel**: Click the beaker icon 🧪 in left sidebar (or `Ctrl+Shift+T`)
2. **Refresh Tests**: Click the refresh button at the top
3. **Click ▶️ Play Button**: Next to any test to run it
4. **Debug**: Click 🐛 icon to debug with breakpoints

## 📝 Before Running Tests:

1. **Update Configuration**: Edit `config/config.py`
   - URL is already set to: `https://bpholter.stage.bio-beat.cloud`

2. **Update Locators** (if needed): Edit `pages/login_page.py`
   - Locators are already configured for Bio-Beat

## 🔧 Troubleshooting:

If `pytest` command doesn't work, always use:
```powershell
py -m pytest
```

This ensures the correct Python interpreter is used.

## 📊 Useful Commands:

```powershell
# Run only failed tests
py -m pytest --lf

# Run in parallel (faster)
py -m pytest -n auto

# Stop on first failure
py -m pytest -x

# Show print statements
py -m pytest -s

# Verbose output
py -m pytest -v
```

## 🎯 Test Files:
- `tests/test_validation.py` - Field validation tests (29 tests)
- `tests/test_login.py` - Basic login tests
- `tests/test_login_extended.py` - Security and UI tests
