#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korean Font Test Script for Raspberry Pi
Tests if Korean fonts are properly installed and can be used in python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def test_korean_fonts():
    """Create a test PowerPoint with Korean text using different fonts"""
    
    print("Creating Korean font test presentation...")
    
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Test fonts available on Raspberry Pi
    test_fonts = [
        ('NanumGothic', '나눔고딕'),
        ('NanumMyeongjo', '나눔명조'),
        ('NanumBarunGothic', '나눔바른고딕'),
        ('UnDotum', '은돋움')
    ]
    
    # Create title slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(30, 30, 60)
    
    # Add title
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.5), Inches(8), Inches(1.5)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "한글 폰트 테스트\n(Korean Font Test)"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = 'NanumGothic'
    p.alignment = PP_ALIGN.CENTER
    
    # Add subtitle
    subtitle_box = slide.shapes.add_textbox(
        Inches(1), Inches(4.2), Inches(8), Inches(0.5)
    )
    tf = subtitle_box.text_frame
    p = tf.paragraphs[0]
    p.text = "Raspberry Pi Korean Font Installation Test"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(200, 200, 200)
    p.font.name = 'NanumGothic'
    p.alignment = PP_ALIGN.CENTER
    
    # Create font test slides
    for font_name, font_korean in test_fonts:
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(40, 40, 70)
        
        # Font name header
        header_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(9), Inches(0.8)
        )
        tf = header_box.text_frame
        p = tf.paragraphs[0]
        p.text = f"Font: {font_name} ({font_korean})"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 200, 100)
        p.font.name = font_name
        p.alignment = PP_ALIGN.CENTER
        
        # Sample Korean text
        korean_samples = [
            "가나다라마바사아자차카타파하",
            "안녕하세요 (Hello)",
            "대한민국 (Republic of Korea)",
            "라즈베리 파이 (Raspberry Pi)",
            "한글 폰트 테스트 성공! ✅"
        ]
        
        y_position = 1.8
        for i, sample_text in enumerate(korean_samples):
            text_box = slide.shapes.add_textbox(
                Inches(1), Inches(y_position + i * 0.9),
                Inches(8), Inches(0.7)
            )
            tf = text_box.text_frame
            p = tf.paragraphs[0]
            p.text = sample_text
            p.font.size = Pt(20)
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.font.name = font_name
            p.alignment = PP_ALIGN.CENTER
    
    # Save the presentation
    output_file = 'korean_font_test.pptx'
    prs.save(output_file)
    
    print(f"\n✅ Test presentation created successfully!")
    print(f"📄 File: {output_file}")
    print(f"📊 Slides: {len(prs.slides)} (1 title + {len(test_fonts)} font tests)")
    print(f"\nFonts tested:")
    for font_name, font_korean in test_fonts:
        print(f"  ✓ {font_name} ({font_korean})")
    print(f"\nOpen '{output_file}' to verify Korean fonts are rendering correctly.")
    print(f"If Korean text appears as boxes, please run: ./install_korean_fonts.sh")

if __name__ == "__main__":
    try:
        test_korean_fonts()
    except Exception as e:
        print(f"\n❌ Error creating test presentation:")
        print(f"   {str(e)}")
        print(f"\nPlease ensure:")
        print(f"  1. python-pptx is installed: pip install python-pptx")
        print(f"  2. Korean fonts are installed: ./install_korean_fonts.sh")
        exit(1)
