# pptx

PowerPoint presentation generator with Korean (Hangul) language support.

## Korean Language Support on Raspberry Pi

This repository includes tools for installing Korean fonts and language support on Raspberry Pi, enabling proper rendering of Korean text in generated PowerPoint presentations.

### Quick Start for Raspberry Pi

To install Korean (Hangul) support on your Raspberry Pi:

```bash
chmod +x install_korean_fonts.sh
./install_korean_fonts.sh
```

For detailed instructions, troubleshooting, and manual installation steps, see [KOREAN_SETUP.md](KOREAN_SETUP.md).

### What Gets Installed

- **Nanum Fonts** (나눔 글꼴): Modern Korean fonts including NanumGothic, NanumMyeongjo
- **Baekmuk Fonts** (백묵 글꼴): Traditional Korean fonts
- **UnFonts** (은 글꼴): Additional Korean font family
- **Korean Language Packages**: System-level Korean language support

## Documentation

- [Korean Setup Guide](KOREAN_SETUP.md) - Detailed guide for installing Hangul support on Raspberry Pi
- [Installation Script](install_korean_fonts.sh) - Automated installation script

## Requirements

- Raspberry Pi OS (or any Debian-based Linux)
- Python 3.7+
- python-pptx (for PowerPoint generation)

## License

This project is for educational and demonstration purposes.