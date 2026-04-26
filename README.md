# pptx

PowerPoint presentation generator with Korean (Hangul) language support for Raspberry Pi.

## 🚀 Quick Start

Install Korean (Hangul) fonts and language support on your Raspberry Pi:

```bash
# Clone the repository
git clone https://github.com/ockum12/pptx.git
cd pptx

# Run the installation script
chmod +x install_korean_fonts.sh
./install_korean_fonts.sh

# Test the installation
python3 test_korean_fonts.py
```

That's it! You now have full Korean language support on your Raspberry Pi.

## 📖 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Step-by-step installation instructions (5 minutes)
- **[Detailed Setup Guide](KOREAN_SETUP.md)** - Comprehensive documentation with troubleshooting
- **[Installation Script](install_korean_fonts.sh)** - Automated font installation for Raspberry Pi
- **[Font Test Script](test_korean_fonts.py)** - Verify Korean fonts are working correctly

## 🎯 What This Installs

The installation script will set up:

- **Nanum Fonts** (나눔 글꼴): NanumGothic, NanumMyeongjo, NanumBarunGothic
- **Baekmuk Fonts** (백묵 글꼴): Traditional Korean fonts
- **UnFonts** (은 글꼴): Additional Korean font family
- **Korean Language Packages**: System-level Korean language support

## 💻 Requirements

- Raspberry Pi OS (or any Debian/Ubuntu-based Linux)
- Python 3.7+ (for PowerPoint generation)
- Internet connection (for downloading fonts)

## 🔧 Usage Example

After installation, you can use Korean fonts in python-pptx:

```python
from pptx import Presentation
from pptx.util import Pt

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])

# Use Korean font
title = slide.shapes.title
title.text = "안녕하세요"  # Hello in Korean
title.text_frame.paragraphs[0].font.name = 'NanumGothic'
title.text_frame.paragraphs[0].font.size = Pt(44)

prs.save('korean_presentation.pptx')
```

## 🧪 Testing

Verify your installation:

```bash
# List installed Korean fonts
fc-list :lang=ko | grep Nanum

# Create a test PowerPoint with Korean text
python3 test_korean_fonts.py
```

## 🐛 Troubleshooting

**Font not found?**
```bash
sudo fc-cache -fv
```

**Korean text shows as boxes?**
- Make sure you're using the exact font name: `'NanumGothic'` (not `'나눔고딕'`)
- Font names are case-sensitive

**Installation fails?**
- Update your system: `sudo apt-get update && sudo apt-get upgrade`
- See the [Detailed Setup Guide](KOREAN_SETUP.md) for manual installation steps

## 📚 Additional Information

This repository is designed to help developers working with Korean language content on Raspberry Pi. The installation script and documentation are based on best practices for Korean font installation on Debian-based systems.

## 📄 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

Issues and pull requests are welcome! If you encounter problems with Korean font installation on Raspberry Pi, please open an issue with details about your setup.