import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_pdf():
    pdf_dir = "/home/lnx/Pictures/test/documents"
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
        
    pdf_path = os.path.join(pdf_dir, "raghuvanshi_food_packets.pdf")
    
    # Document Setup (0.5 inch margins for editorial grid feel)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Brand Colors
    PRIMARY = colors.HexColor("#E65C00")      # Brand Orange
    SECONDARY = colors.HexColor("#2E2722")    # Dark Cocoa
    TEXT_MUTED = colors.HexColor("#5c5043")   # Muted Brown
    BG_CREAM = colors.HexColor("#FAF5F0")     # Light Cream
    ACCENT_GREEN = colors.HexColor("#2E7D32") # Veg Green
    
    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=SECONDARY,
        spaceAfter=15
    )
    
    header_right_style = ParagraphStyle(
        'HeaderRight',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=TEXT_MUTED,
        alignment=2 # Right aligned
    )
    
    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=SECONDARY,
        spaceBefore=15,
        spaceAfter=8,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=SECONDARY,
        spaceAfter=8
    )
    
    body_bold_style = ParagraphStyle(
        'BodyBoldCustom',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    veg_tag_style = ParagraphStyle(
        'VegTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=ACCENT_GREEN,
        alignment=2
    )
    
    note_style = ParagraphStyle(
        'NoteText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_MUTED
    )

    story_box_style = ParagraphStyle(
        'StoryText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#4e4135")
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=SECONDARY
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold'
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.white
    )
    
    story = []
    
    # ------------------ PAGE 1 ------------------
    # Header Grid (Brand Info & Contact)
    header_data = [
        [
            Paragraph("RAGHUVANSHI", title_style),
            Paragraph("<b>Sandeep Thakker:</b> +91 98252-61590<br/><b>Jeet Thakkar:</b> +91 96382-27370", header_right_style)
        ],
        [
            Paragraph("Khaman House &amp; Lassi Centre", subtitle_style),
            Paragraph("13, Perin Complex, Kilavni Naka, Silvassa", header_right_style)
        ]
    ]
    header_table = Table(header_data, colWidths=[300, 240])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 15))
    
    # Decorative colored bar separator
    bar_data = [['']]
    bar_table = Table(bar_data, colWidths=[540], rowHeights=[3])
    bar_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), PRIMARY),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(bar_table)
    story.append(Spacer(1, 15))
    
    # About Section
    story.append(Paragraph("BULK ORDER MENU", h1_style))
    story.append(Paragraph(
        "Raghuvanshi Khaman House makes it easy to serve fresh, hot snacks to your guests. "
        "Whether it is an office meeting, a morning breakfast, or a society function, we provide "
        "ready-to-eat boxes packed with our famous snacks. 100% vegetarian, made fresh the same day.",
        body_style
    ))
    
    # Veg Badge Card
    veg_card_data = [
        [
            Paragraph("<b>100% PURE VEG SNACK BOXES</b>", ParagraphStyle('VegTitle', parent=body_bold_style, textColor=ACCENT_GREEN)),
            Paragraph("[  VEG  ]", veg_tag_style)
        ]
    ]
    veg_card_table = Table(veg_card_data, colWidths=[400, 140])
    veg_card_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#E8F5E9")),
        ('BOX', (0,0), (-1,-1), 1.5, ACCENT_GREEN),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(Spacer(1, 5))
    story.append(veg_card_table)
    story.append(Spacer(1, 15))
    
    # Editorial Legacy Storytelling Quote Box
    story_box_data = [[
        Paragraph(
            "\"We prepare every batch with care and pack it hot. No shortcuts, just pure love for taste.\"",
            story_box_style
        )
    ]]
    story_box_table = Table(story_box_data, colWidths=[540])
    story_box_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_CREAM),
        ('LINELEFT', (0,0), (0,0), 3, PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('RIGHTPADDING', (0,0), (-1,-1), 15),
    ]))
    story.append(story_box_table)
    story.append(Spacer(1, 20))
    
    # Platter Section
    story.append(Paragraph("1. MORNING BREAKFAST BOX (3 ITEMS)", h1_style))
    story.append(Paragraph("<b>Price:</b> &#8377;90 per box (Minimum Order: 20 Boxes)", body_style))
    story.append(Paragraph("A fresh and simple snack box, perfect for morning tea.", body_style))
    story.append(Spacer(1, 5))
    
    # 3-Section Table
    three_sec_data = [
        [
            Paragraph("Hot Farsan (Choose 1)", table_header_style),
            Paragraph("Fried Snack (Choose 1)", table_header_style),
            Paragraph("Sweet / Drink (Choose 1)", table_header_style)
        ],
        [
            Paragraph("• Nylon Khaman<br/>• White Dhokla<br/>• Sev Khamni<br/>• Khandvi<br/>• Patra", table_cell_style),
            Paragraph("• Veg Samosa<br/>• Chinese Samosa", table_cell_style),
            Paragraph("• Motichoor Ladoo (Orange)<br/>• Mango Lassi<br/>• Sweet Lassi", table_cell_style)
        ]
    ]
    three_sec_table = Table(three_sec_data, colWidths=[180, 180, 180])
    three_sec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('BACKGROUND', (0,1), (-1,-1), BG_CREAM),
        ('BOX', (0,0), (-1,-1), 1, SECONDARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E0D6CC")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(three_sec_table)
    story.append(Spacer(1, 20))
    
    # Ordering Note / Footer of Page 1
    note_box_data = [[
        Paragraph(
            "<b>Important Details:</b><br/>"
            "• Please tell us 1-2 days before so we can keep your order ready.<br/>"
            "• We can give you a proper bill with GST if you need it for your office.<br/>"
            "• Everything is packed neatly in good quality boxes.",
            note_style
        )
    ]]
    note_box_table = Table(note_box_data, colWidths=[540])
    note_box_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E0D6CC")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(note_box_table)
    
    # Force Page Break to create Page 2
    story.append(PageBreak())
    
    # ------------------ PAGE 2 ------------------
    # Header Grid (Page 2 Header)
    story.append(header_table)
    story.append(Spacer(1, 10))
    story.append(bar_table)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("2. SPECIAL FUNCTION BOX (4 ITEMS)", h1_style))
    story.append(Paragraph("<b>Price:</b> &#8377;160 per box (Minimum Order: 20 Boxes)", body_style))
    story.append(Paragraph("A heavy, satisfying snack box for evening functions or big parties.", body_style))
    story.append(Spacer(1, 5))
    
    # 4-Section Table
    five_sec_data = [
        [
            Paragraph("Category", table_header_style),
            Paragraph("Item Options (Chutney included)", table_header_style)
        ],
        [
            Paragraph("<b>Item 1</b><br/>Soft Farsan", table_cell_bold),
            Paragraph("Choose 1: Nylon Khaman / White Dhokla / Sev Khamni / Khandvi", table_cell_style)
        ],
        [
            Paragraph("<b>Item 2</b><br/>Fried Snack", table_cell_bold),
            Paragraph("Choose 1: Veg Samosa / Chinese Samosa / Coconut Petis", table_cell_style)
        ],
        [
            Paragraph("<b>Item 3</b><br/>Sweet", table_cell_bold),
            Paragraph("Choose 1: Motichoor Ladoo (Orange)", table_cell_style)
        ],
        [
            Paragraph("<b>Item 4</b><br/>Drink", table_cell_bold),
            Paragraph("Choose 1: Mango Lassi / Sweet Lassi / Masala Buttermilk", table_cell_style)
        ]
    ]
    five_sec_table = Table(five_sec_data, colWidths=[140, 400])
    five_sec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('BACKGROUND', (0,1), (-1,-1), BG_CREAM),
        ('BOX', (0,0), (-1,-1), 1, SECONDARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E0D6CC")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [BG_CREAM, colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(five_sec_table)
    story.append(Spacer(1, 40))
    
    # Call to Action Block
    cta_data = [[
        Paragraph(
            "<font color='#ffffff'><b>READY TO BOOK YOUR ORDER?</b></font><br/>"
            "<font color='#fce6d8'>Click the 'Ask for the Rate' button on our website, or just message us on WhatsApp with your date and total boxes. "
            "You can also call Sandeep at <b>+91 98252-61590</b> or Jeet at <b>+91 96382-27370</b>.</font>",
            ParagraphStyle('CTAText', parent=body_style, textColor=colors.white)
        )
    ]]
    cta_table = Table(cta_data, colWidths=[540])
    cta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PRIMARY),
        ('BOX', (0,0), (-1,-1), 1, PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 15),
        ('BOTTOMPADDING', (0,0), (-1,-1), 15),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(cta_table)
    
    # Build Document
    doc.build(story)
    print("PDF successfully generated at:", pdf_path)

if __name__ == "__main__":
    create_pdf()
