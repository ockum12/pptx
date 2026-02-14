#!/bin/bash
# Script to install Korean (Hangul) fonts and language support on Raspberry Pi
# This enables proper rendering of Korean text in PowerPoint presentations

set -e

echo "=========================================="
echo "Korean (Hangul) Font Installation Script"
echo "for Raspberry Pi"
echo "=========================================="
echo ""

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "Warning: This script is designed for Linux systems (Raspberry Pi OS)"
    echo "Your OS: $OSTYPE"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "Step 1: Updating package lists..."
sudo apt-get update

echo ""
echo "Step 2: Installing Korean fonts..."
echo "This will install:"
echo "  - fonts-nanum: Nanum fonts (NanumGothic, NanumMyeongjo)"
echo "  - fonts-nanum-coding: Nanum coding fonts"
echo "  - fonts-nanum-extra: Additional Nanum fonts"
echo ""

sudo apt-get install -y \
    fonts-nanum \
    fonts-nanum-coding \
    fonts-nanum-extra

echo ""
echo "Step 3: Installing additional Korean fonts..."
sudo apt-get install -y \
    fonts-unfonts-core \
    fonts-baekmuk

echo ""
echo "Step 4: Installing Korean language support packages..."
sudo apt-get install -y \
    language-pack-ko \
    language-pack-ko-base

echo ""
echo "Step 5: Updating font cache..."
sudo fc-cache -fv

echo ""
echo "Step 6: Verifying Korean font installation..."
if fc-list :lang=ko | grep -q "Nanum"; then
    echo "✅ Korean fonts installed successfully!"
    echo ""
    echo "Available Korean fonts:"
    fc-list :lang=ko | grep -E "Nanum|Baekmuk|UnDotum" | head -10
else
    echo "⚠️  Warning: Korean fonts may not be properly installed"
    echo "Please check the installation manually"
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Korean fonts installed:"
echo "  - NanumGothic (나눔고딕)"
echo "  - NanumMyeongjo (나눔명조)"
echo "  - NanumBarunGothic (나눔바른고딕)"
echo "  - Baekmuk fonts (백묵 글꼴)"
echo "  - UnDotum fonts (은 글꼴)"
echo ""
echo "You can now use these fonts in your applications."
echo "For python-pptx, use font names like:"
echo "  - 'NanumGothic'"
echo "  - 'NanumMyeongjo'"
echo "  - 'NanumBarunGothic'"
echo ""
echo "Note: If you have scripts using Windows fonts like '맑은 고딕' (Malgun Gothic)"
echo "or '돋움' (Dotum), replace them with 'NanumGothic' for Raspberry Pi compatibility."
echo ""
echo "Run 'python3 test_korean_fonts.py' to verify the installation."
echo ""
