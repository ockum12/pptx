#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TalkTale 투자제안서 PowerPoint 생성 스크립트
AI 대화형 동화책 웹서비스 & 스마트 음성펜 플랫폼
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE


def hex_to_rgb(hex_color):
    """헥스 컬러 코드를 RGB 튜플로 변환"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def add_gradient_background(slide, color1_hex, color2_hex):
    """슬라이드에 그라데이션 배경 추가"""
    background = slide.background
    fill = background.fill
    fill.solid()
    # python-pptx는 네이티브 그라데이션을 지원하지 않으므로 단색 배경 사용
    rgb = hex_to_rgb(color1_hex)
    fill.fore_color.rgb = RGBColor(*rgb)


def add_solid_background(slide, color_hex):
    """슬라이드에 단색 배경 추가"""
    background = slide.background
    fill = background.fill
    fill.solid()
    rgb = hex_to_rgb(color_hex)
    fill.fore_color.rgb = RGBColor(*rgb)


def add_rounded_rectangle(slide, left, top, width, height, bg_color_hex, text_content, font_size=14):
    """둥근 사각형 카드 추가"""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        left, top, width, height
    )
    
    # 배경색 설정
    fill = shape.fill
    fill.solid()
    rgb = hex_to_rgb(bg_color_hex)
    fill.fore_color.rgb = RGBColor(*rgb)
    
    # 테두리 제거
    line = shape.line
    line.fill.background()
    
    # 텍스트 설정
    text_frame = shape.text_frame
    text_frame.word_wrap = True
    text_frame.margin_left = Inches(0.2)
    text_frame.margin_right = Inches(0.2)
    text_frame.margin_top = Inches(0.2)
    text_frame.margin_bottom = Inches(0.2)
    
    p = text_frame.paragraphs[0]
    p.text = text_content
    p.font.size = Pt(font_size)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    return shape


def create_title_slide(prs):
    """슬라이드 1: 표지"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 레이아웃
    add_gradient_background(slide, '#667eea', '#764ba2')
    
    # 메인 타이틀
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.5), Inches(8), Inches(1)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "TalkTale (토크테일)"
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 부제
    subtitle_box = slide.shapes.add_textbox(
        Inches(1), Inches(3.7), Inches(8), Inches(0.6)
    )
    tf = subtitle_box.text_frame
    p = tf.paragraphs[0]
    p.text = "AI 대화형 동화책 웹서비스 & 스마트 음성펜 플랫폼"
    p.font.size = Pt(20)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 태그라인
    tagline_box = slide.shapes.add_textbox(
        Inches(1), Inches(4.5), Inches(8), Inches(0.5)
    )
    tf = tagline_box.text_frame
    p = tf.paragraphs[0]
    p.text = '"읽는 동화에서, 대화하는 동화로"'
    p.font.size = Pt(18)
    p.font.italic = True
    p.font.color.rgb = RGBColor(255, 255, 200)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 날짜
    date_box = slide.shapes.add_textbox(
        Inches(1), Inches(5.5), Inches(8), Inches(0.4)
    )
    tf = date_box.text_frame
    p = tf.paragraphs[0]
    p.text = "투자 제안서 | 2026년 2월"
    p.font.size = Pt(16)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER


def create_problem_slide(prs):
    """슬라이드 2: 문제 정의"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#1a1a2e')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "문제 정의 (Problem)"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4개 카드 (2x2 그리드)
    cards = [
        "📕 일방향 독서 경험\n\n기존 동화책은 아이가 수동적으로 읽기만 하는 구조. 호기심과 질문에 즉각 응답 불가 → 학습 몰입도 저하",
        "🧠 아동 심리 파악 어려움\n\n부모는 아이의 감정과 생각을 파악하기 어려움. 조기 심리 케어의 골든타임을 놓칠 위험",
        "📱 디지털 vs 종이책 딜레마\n\n디지털 콘텐츠의 편리함과 종이책의 감성적 가치 사이에서 양자택일을 강요받는 부모들",
        "💰 에듀테크 시장 기회\n\n글로벌 에듀테크 시장 2030년 $400B+ 성장 전망. AI+아동교육 융합 영역은 아직 블루오션"
    ]
    
    card_positions = [
        (0.5, 1.5, 4.25, 2.2),
        (5.25, 1.5, 4.25, 2.2),
        (0.5, 4.2, 4.25, 2.2),
        (5.25, 4.2, 4.25, 2.2)
    ]
    
    for i, (left, top, width, height) in enumerate(card_positions):
        add_rounded_rectangle(
            slide, 
            Inches(left), Inches(top), 
            Inches(width), Inches(height),
            '#e94560',
            cards[i],
            font_size=12
        )


def create_solution_slide(prs):
    """슬라이드 3: 솔루션 개요"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#0f3460')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "솔루션 개요 (Solution)"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 5단계 플로우
    steps = [
        "1️⃣\n종이책\n+\n음성펜",
        "2️⃣\n음향\n+\n신호전송",
        "3️⃣\n웹\n자동\n표시",
        "4️⃣\nAI\n대화\n(RAG)",
        "5️⃣\n심리\n분석"
    ]
    
    for i, step in enumerate(steps):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 1.9), Inches(1.5),
            Inches(1.6), Inches(2.5),
            '#00d2ff',
            step,
            font_size=11
        )
    
    # 하단 핵심 가치 박스
    value_box = add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(4.5),
        Inches(9), Inches(1.5),
        '#00d2ff',
        "💡 핵심 가치\n\n종이책의 감성 + AI의 대화형 학습 + 아동 심리 데이터를\n하나의 플랫폼에서 제공",
        font_size=14
    )


def create_architecture_slide(prs):
    """슬라이드 4: 시스템 아키텍처"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#16213e')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "시스템 아키텍처"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 3개 레이어
    layers = [
        "🖊️ 하드웨어 레이어\n\n• 음성펜 (OID 코드 리더)\n• 특수코드 인쇄 종이책\n• BLE/Wi-Fi 통신 모듈\n• 내장 스피커 & 마이크\n• 충전식 배터리",
        "☁️ 백엔드 레이어\n\n• API Gateway\n• RAG Engine (LLM + Vector DB)\n• 동화책 콘텐츠 DB\n• 대화 로그 저장소\n• 심리 분석 AI 모듈\n• 음성펜 신호 처리 서버",
        "📱 프론트엔드 레이어\n\n• 반응형 전자책 뷰어\n• AI 채팅 인터페이스\n• 음성 입출력 (STT/TTS)\n• 부모 대시보드\n• 심리 리포트 뷰어"
    ]
    
    for i, layer in enumerate(layers):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 3.2), Inches(1.2),
            Inches(2.9), Inches(3.5),
            '#4ecca3',
            layer,
            font_size=10
        )
    
    # 하단 기술 스택
    tech_box = add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(5.2),
        Inches(9), Inches(1.2),
        '#4ecca3',
        "🔧 기술 스택\nOpenAI GPT/Claude | LangChain | Pinecone/Weaviate | React/Next.js | Node.js | PostgreSQL | WebSocket | Web Audio API | BLE Protocol | TTS/STT Engine",
        font_size=11
    )


def create_rag_slide(prs):
    """슬라이드 5: RAG 기반 AI 대화 시스템"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#1b1b2f')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "RAG 기반 AI 대화 시스템"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4단계 파이프라인
    pipeline = [
        "1️⃣ 📚\n동화책\n임베딩 &\n인덱싱",
        "2️⃣ 🔍\n컨텍스트\n검색\n(Retrieval)",
        "3️⃣ 🧠\nLLM\n응답 생성\n(Generation)",
        "4️⃣ 💾\n대화 로그\n저장 &\n분석"
    ]
    
    for i, step in enumerate(pipeline):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 2.4), Inches(1.2),
            Inches(2.1), Inches(1.8),
            '#ff6b6b',
            step,
            font_size=11
        )
    
    # 대화 예시
    example_text = '''💬 대화 예시 ("백설공주" 동화)

👧 아이: "왜 왕비는 백설공주를 미워해요?"

🤖 AI: "백설공주가 거울에서 세상에서 가장 아름답다고 들었기 때문이에요. 
왕비는 질투심을 느꼈답니다."

👧 아이: "질투심이 뭐예요?"

🤖 AI: "질투심은 다른 사람이 나보다 더 좋은 것을 가지고 있을 때 느끼는 
부정적인 감정이에요. 왕비는 백설공주가 더 예뻐서 화가 난 거예요."'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(3.5),
        Inches(9), Inches(2.8),
        '#ff6b6b',
        example_text,
        font_size=11
    )


def create_voicepen_slide(prs):
    """슬라이드 6: 음성펜 & 웹 연동 시스템"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#2d3436')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "음성펜 & 웹 연동 시스템"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4단계 플로우
    flow = [
        "1️⃣\n종이책\n특수코드",
        "2️⃣\n음성펜\n인식",
        "3️⃣\n웹 서비스\n연동",
        "4️⃣\nAI 대화\n시작"
    ]
    
    for i, step in enumerate(flow):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 2.4), Inches(1.2),
            Inches(2.1), Inches(1.5),
            '#fdcb6e',
            step,
            font_size=12
        )
    
    # 사양 테이블
    specs_text = '''🖊️ 음성펜 사양

• 코드 방식: OID 미세 도트 패턴
• 통신 방식: BLE 5.0 + Wi-Fi
• 음성 출력: 내장 스피커 (2W)
• 음성 입력: 내장 마이크 + STT
• 배터리: Li-Po 800mAh, USB-C 충전
• 안전 인증: KC, CE, FCC'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(3.2),
        Inches(9), Inches(3),
        '#fdcb6e',
        specs_text,
        font_size=13
    )


def create_psychology_slide(prs):
    """슬라이드 7: 아동 심리 분석 시스템"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#0c0c1d')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "아동 심리 분석 시스템"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4개 기능 카드
    functions = [
        "📝\n대화 로그\n수집",
        "🎭\n감정 분석\n(Sentiment)",
        "📈\n성장 추이\n트래킹",
        "⚠️\n조기 경보\n시스템"
    ]
    
    for i, func in enumerate(functions):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 2.4), Inches(1.2),
            Inches(2.1), Inches(1.5),
            '#a29bfe',
            func,
            font_size=12
        )
    
    # 부모 대시보드 리포트
    report_text = '''📊 부모 대시보드 리포트 예시

호기심 지수: ████████████████████ 85%
공감 능력:   ██████████████▒▒▒▒▒▒ 72%
어휘 다양성: ████████████▒▒▒▒▒▒▒▒ 68%
불안 지수:   ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 15%

✅ 종합 평가: 정상 발달 범위 내, 호기심과 탐구심이 높은 편'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(3.2),
        Inches(9), Inches(3),
        '#a29bfe',
        report_text,
        font_size=12
    )


def create_business_model_slide(prs):
    """슬라이드 8: 비즈니스 모델"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#0a3d62')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "비즈니스 모델"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 3개 요금제 카드
    plans = [
        "📦 스타터 패키지\n₩89,000 / 1회\n\n• 음성펜 1개\n• 동화책 3권\n• Basic AI 대화 월 100회\n• 기본 심리 리포트",
        "⭐ 프리미엄 구독\n₩14,900 / 월\n\n• 무제한 AI 대화\n• 월 2권 신규 동화책\n• 상세 심리 분석\n• 전문가 상담 연계",
        "🏢 B2B/기관용\n별도 협의\n\n• 단체 라이선스\n• 교육기관 대시보드\n• 커스텀 콘텐츠\n• API 연동"
    ]
    
    for i, plan in enumerate(plans):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 3.2), Inches(1.2),
            Inches(2.9), Inches(3.5),
            '#78e08f',
            plan,
            font_size=11
        )
    
    # 하단 요약
    summary_box = add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(5.2),
        Inches(9), Inches(1.2),
        '#78e08f',
        "💰 수익 다각화 전략 & 높은 고객 Lock-in 효과\nLTV (고객 생애 가치) ₩400,000+",
        font_size=13
    )


def create_market_slide(prs):
    """슬라이드 9: 시장 규모 & 경쟁 우위"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#2c2c54')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "시장 규모 & 경쟁 우위"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 좌측: 시장 규모
    market_text = '''📊 시장 규모

TAM: $180B
(글로벌 에듀테크)

SAM: $12B
(아동 학습 콘텐츠)

SOM: $500M
(한국 타겟 시장)

• 국내 아동 교육 콘텐츠:
  약 2.5조원 (연 15% 성장)
• 음성펜 시장: 연 20% 성장'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(1.2),
        Inches(4.5), Inches(5),
        '#ffb142',
        market_text,
        font_size=12
    )
    
    # 우측: 경쟁 우위
    advantage_text = '''🏆 4대 경쟁 우위

1️⃣ 유일한 AI+음성펜+웹
   통합 플랫폼

2️⃣ 심리 분석 데이터
   경제적 해자

3️⃣ 콘텐츠 IP 확장성
   (출판, 라이선스)

4️⃣ HW+SW Lock-in 효과
   (전환 장벽 높음)'''
    
    add_rounded_rectangle(
        slide,
        Inches(5.5), Inches(1.2),
        Inches(4), Inches(5),
        '#ffb142',
        advantage_text,
        font_size=12
    )


def create_roadmap_slide(prs):
    """슬라이드 10: 로드맵 & 마일스톤"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#1e272e')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "로드맵 & 마일스톤"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4단계 타임라인
    phases = [
        "Phase 1 — MVP 개발 & 검증\n2026 Q2~Q3\n\n• RAG AI 프로토타입\n• 웹뷰어 & 음성펜 시제품\n• 동화책 5권\n• 베타 50가정\n\nKPI: 만족도 80%+",
        "Phase 2 — 정식 런칭\n2026 Q4~2027 Q1\n\n• 음성펜 양산\n• 동화책 20권+\n• 대시보드 v1.0\n• 마케팅 캠페인\n• B2B 파일럿\n\nKPI: 유료 가입 3,000+",
        "Phase 3 — 스케일업\n2027 Q2~Q4\n\n• 심리 AI 고도화\n• 다국어 지원\n• 출판사 파트너십\n• B2B 100개소+\n\nKPI: MAU 50,000+\nARR ₩30억+",
        "Phase 4 — 글로벌 진출\n2028 Q1~\n\n• 해외 시장 진출\n• IP 확장 (애니, 게임)\n• 공공 교육 프로그램\n• Exit 준비\n\nKPI: 글로벌 MAU\n200,000+"
    ]
    
    y_positions = [1.2, 2.5, 3.8, 5.1]
    
    for i, (phase, y_pos) in enumerate(zip(phases, y_positions)):
        add_rounded_rectangle(
            slide,
            Inches(0.5), Inches(y_pos),
            Inches(9), Inches(1.1),
            '#0be881',
            phase,
            font_size=9
        )


def create_financial_slide(prs):
    """슬라이드 11: 재무 계획 & 투자 요청"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_solid_background(slide, '#192a56')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "재무 계획 & 투자 요청"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 좌측: 매출 전망
    revenue_text = '''📈 매출 전망 (3개년)

2026년 (H2)
총 매출: ₩4.5억
영업이익률: -40%

2027년
총 매출: ₩35억
영업이익률: 5%

2028년
총 매출: ₩96억
영업이익률: 22%'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(1.2),
        Inches(4.5), Inches(2.8),
        '#f7d794',
        revenue_text,
        font_size=12
    )
    
    # 우측: 핵심 KPI
    kpi_text = '''📊 핵심 KPI 전망

• 가입 가정 수: 3K → 20K → 50K
• MAU: 2K → 15K → 40K
• 구독 전환율: 15% → 25% → 35%
• 이탈률: 8% → 5% → 3%
• LTV: ₩300K → ₩400K → ₩500K
• CAC: ₩80K → ₩50K → ₩40K'''
    
    add_rounded_rectangle(
        slide,
        Inches(5.5), Inches(1.2),
        Inches(4), Inches(2.8),
        '#f7d794',
        kpi_text,
        font_size=11
    )
    
    # 하단: 투자 요청
    investment_text = '''💰 시드 라운드 투자 요청

₩15억 투자 유치 (Pre-money ₩60억, 지분 20%)

자금 사용 계획:
• 제품 개발 (40%): ₩6억
• 콘텐츠 제작 (25%): ₩3.75억
• 마케팅 (20%): ₩3억
• 인력 채용 (10%): ₩1.5억
• 운영비 및 기타 (5%): ₩0.75억'''
    
    add_rounded_rectangle(
        slide,
        Inches(0.5), Inches(4.5),
        Inches(9), Inches(1.8),
        '#f7d794',
        investment_text,
        font_size=12
    )


def create_team_slide(prs):
    """슬라이드 12: 팀 구성 & 클로징"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_gradient_background(slide, '#667eea', '#764ba2')
    
    # 제목
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.4), Inches(9), Inches(0.6)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "팀 구성 & 클로징"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    
    # 4명 팀 카드
    team = [
        "👨‍💼 CEO/대표\n\n에듀테크 창업 경험\n아동교육 콘텐츠\n10년 경력",
        "👩‍💻 CTO/기술총괄\n\nNLP/RAG 전문가\n대기업 AI Lab\n출신",
        "👨‍🔬 HW Lead\n\nIoT 디바이스\n양산 경험\n전자펜 기구 설계",
        "👩‍⚕️ 아동심리 자문\n\n아동발달심리학\n박사\n임상 상담 15년"
    ]
    
    for i, member in enumerate(team):
        add_rounded_rectangle(
            slide,
            Inches(0.5 + i * 2.4), Inches(1.2),
            Inches(2.1), Inches(2.5),
            '#764ba2',
            member,
            font_size=10
        )
    
    # 클로징 메시지
    closing_box = slide.shapes.add_textbox(
        Inches(1), Inches(4.2), Inches(8), Inches(0.8)
    )
    tf = closing_box.text_frame
    p = tf.paragraphs[0]
    p.text = '"읽는 동화에서, 대화하는 동화로"'
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.italic = True
    p.font.color.rgb = RGBColor(255, 255, 200)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 연락처
    contact_box = slide.shapes.add_textbox(
        Inches(1), Inches(5.3), Inches(8), Inches(0.8)
    )
    tf = contact_box.text_frame
    
    # 첫 번째 줄
    p = tf.paragraphs[0]
    p.text = "📧 contact@talktale.co.kr"
    p.font.size = Pt(14)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 두 번째 줄
    p = tf.add_paragraph()
    p.text = "📞 02-XXXX-XXXX"
    p.font.size = Pt(14)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER
    
    # 세 번째 줄
    p = tf.add_paragraph()
    p.text = "🌐 www.talktale.co.kr"
    p.font.size = Pt(14)
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.name = '맑은 고딕'
    p.alignment = PP_ALIGN.CENTER


def main():
    """메인 함수"""
    print("TalkTale 투자제안서 PowerPoint 생성 시작...")
    
    # 프레젠테이션 생성
    prs = Presentation()
    prs.slide_width = Inches(10)  # 16:9 와이드스크린
    prs.slide_height = Inches(7.5)
    
    # 모든 슬라이드 생성
    print("슬라이드 1: 표지")
    create_title_slide(prs)
    
    print("슬라이드 2: 문제 정의")
    create_problem_slide(prs)
    
    print("슬라이드 3: 솔루션 개요")
    create_solution_slide(prs)
    
    print("슬라이드 4: 시스템 아키텍처")
    create_architecture_slide(prs)
    
    print("슬라이드 5: RAG 기반 AI 대화 시스템")
    create_rag_slide(prs)
    
    print("슬라이드 6: 음성펜 & 웹 연동 시스템")
    create_voicepen_slide(prs)
    
    print("슬라이드 7: 아동 심리 분석 시스템")
    create_psychology_slide(prs)
    
    print("슬라이드 8: 비즈니스 모델")
    create_business_model_slide(prs)
    
    print("슬라이드 9: 시장 규모 & 경쟁 우위")
    create_market_slide(prs)
    
    print("슬라이드 10: 로드맵 & 마일스톤")
    create_roadmap_slide(prs)
    
    print("슬라이드 11: 재무 계획 & 투자 요청")
    create_financial_slide(prs)
    
    print("슬라이드 12: 팀 구성 & 클로징")
    create_team_slide(prs)
    
    # 파일 저장
    output_file = "TalkTale_투자제안서.pptx"
    prs.save(output_file)
    print(f"\n✅ PowerPoint 파일이 생성되었습니다: {output_file}")
    print(f"   총 {len(prs.slides)} 개의 슬라이드가 포함되어 있습니다.")


if __name__ == "__main__":
    main()
