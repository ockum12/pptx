# Quick Start Guide: Installing Hangul on Raspberry Pi

This guide provides step-by-step instructions to install Korean (Hangul) language support on your Raspberry Pi.

## Prerequisites

- Raspberry Pi running Raspberry Pi OS (or any Debian-based Linux distribution)
- Internet connection
- Terminal access (SSH or direct)

## Installation Steps

### Option 1: Automated Installation (Recommended)

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/ockum12/pptx.git
   cd pptx
   ```

2. **Run the installation script:**
   ```bash
   chmod +x install_korean_fonts.sh
   ./install_korean_fonts.sh
   ```

3. **Wait for installation to complete** (may take 2-5 minutes depending on your internet speed)

4. **Verify installation:**
   ```bash
   fc-list :lang=ko | grep Nanum
   ```
   
   You should see several NanumGothic and related fonts listed.

### Option 2: Manual Installation

If you prefer to install components individually:

```bash
# Update system
sudo apt-get update

# Install Korean fonts
sudo apt-get install -y fonts-nanum fonts-nanum-coding fonts-nanum-extra
sudo apt-get install -y fonts-unfonts-core fonts-baekmuk

# Install Korean language support
sudo apt-get install -y language-pack-ko language-pack-ko-base

# Update font cache
sudo fc-cache -fv
```

## Testing the Installation

### Quick Test
```bash
# List all Korean fonts
fc-list :lang=ko
```

### Python-pptx Test
If you're using this for PowerPoint generation:

```bash
# Install python-pptx if not already installed
pip3 install python-pptx

# Run the test script
python3 test_korean_fonts.py
```

This will create `korean_font_test.pptx` with Korean text samples in different fonts.

## Fonts Installed

After installation, you'll have access to these Korean fonts:

| Font Family | Font Name | Usage |
|------------|-----------|-------|
| Nanum | NanumGothic | General purpose sans-serif |
| Nanum | NanumMyeongjo | Serif font for formal documents |
| Nanum | NanumBarunGothic | Clean, modern sans-serif |
| Nanum | NanumGothicCoding | Monospace for code |
| Baekmuk | Baekmuk Gulim | Traditional Gothic |
| Baekmuk | Baekmuk Batang | Traditional Myeongjo |
| UnFonts | UnDotum | Clean sans-serif |
| UnFonts | UnBatang | Classic serif |

## Using Korean Fonts in Your Applications

### In python-pptx

```python
from pptx import Presentation
from pptx.util import Pt

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])

# Use Korean font
title = slide.shapes.title
title.text = "안녕하세요"
title.text_frame.paragraphs[0].font.name = 'NanumGothic'
title.text_frame.paragraphs[0].font.size = Pt(44)

prs.save('korean_presentation.pptx')
```

### Font Substitution for Existing Scripts

If you have existing scripts that use Windows fonts like '맑은 고딕' (Malgun Gothic), replace them with 'NanumGothic' for Raspberry Pi compatibility:

```python
# Before (Windows only)
p.font.name = '맑은 고딕'

# After (Raspberry Pi compatible)
p.font.name = 'NanumGothic'
```

## Common Issues and Solutions

### Issue: "Font not found" error

**Solution:** Make sure font cache is updated:
```bash
sudo fc-cache -fv
```

### Issue: Korean text shows as boxes □□□

**Solution:** 
1. Verify fonts are installed: `fc-list :lang=ko`
2. Check the exact font name you're using matches available fonts
3. Try using 'NanumGothic' which is guaranteed to be installed

### Issue: Installation script fails

**Solution:**
1. Update your system: `sudo apt-get update && sudo apt-get upgrade`
2. Check internet connection
3. Try manual installation steps instead

### Issue: Script runs but no Korean text in PowerPoint

**Solution:** The font name must be exact. Use:
- 'NanumGothic' (not '나눔고딕')
- 'NanumMyeongjo' (not '나눔명조')
- Font names are case-sensitive

## Next Steps

1. **Test your installation** using `test_korean_fonts.py`
2. **Read the detailed documentation** in [KOREAN_SETUP.md](KOREAN_SETUP.md)
3. **Modify existing scripts** to use Raspberry Pi-compatible fonts
4. **Create your PowerPoint presentations** with Korean text support

## Getting Help

If you encounter problems:

1. Check the [detailed documentation](KOREAN_SETUP.md)
2. Verify your system is up to date: `sudo apt-get update && sudo apt-get upgrade`
3. List available fonts: `fc-list :lang=ko`
4. Open an issue on GitHub with error details

## Additional Resources

- [Nanum Fonts Official Site](https://hangeul.naver.com/font)
- [python-pptx Documentation](https://python-pptx.readthedocs.io/)
- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)

---

**Success Indicators:**

✅ Running `fc-list :lang=ko` shows multiple fonts  
✅ `test_korean_fonts.py` creates a PowerPoint file successfully  
✅ Opening the PowerPoint shows Korean characters (not boxes)  
✅ Your applications can use 'NanumGothic' and other Korean fonts

**Time Required:** 5-10 minutes for full installation and testing
