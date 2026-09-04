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
            Paragraph("<b>Mobile:</b> +91 98252-61590<br/><b>Email:</b> raghuvanshikhaman@gmail.com", header_right_style)
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
    story.append(Paragraph("CUSTOM FOOD PACK SOLUTIONS", h1_style))
    story.append(Paragraph(
        "Raghuvanshi Khaman House &amp; Lassi Centre is Silvassa's premier food brand, "
        "renowned for serving fresh, authentic snack platters and premium chilled beverages. "
        "We specialize in providing high-volume bulk meal boxes for corporate offices, "
        "industrial staff, training meetings, and family functions. "
        "Our focus is simple: 100% vegetarian recipes, absolute hygiene, and authentic home-style flavors.",
        body_style
    ))
    
    # Veg Badge Card
    veg_card_data = [
        [
            Paragraph("<b>100% PURE VEGETARIAN SNAP-PACKS</b>", ParagraphStyle('VegTitle', parent=body_bold_style, textColor=ACCENT_GREEN)),
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
    
    # Editorial Legacy Storytelling Quote Box (Wordings: generic Khaman and Lassi)
    story_box_data = [[
        Paragraph(
            "\"At half past five, long before the first rays touch Silvassa, our steamers are already firing. "
            "Our besan is whisked by hand, and our sweet thick curd is blended with traditional flavors. We prepare "
            "every batch with care and serve it all-day. No shortcuts, just pure love for taste.\"",
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
    story.append(Paragraph("1. COMPACT 3-COMPARTMENT MEAL PLATTER", h1_style))
    story.append(Paragraph("<b>Corporate Package Price:</b> &#8377;90 per plate (Minimum Order Quantity: 20 Plates)", body_style))
    story.append(Paragraph("A balanced individual pack containing a fresh main farsan, a hot fried snack, and a signature sweet.", body_style))
    story.append(Spacer(1, 5))
    
    # 3-Section Table
    three_sec_data = [
        [
            Paragraph("Compartment 1: Gujarati Farsan (Select Any One)", table_header_style),
            Paragraph("Compartment 2: Fried Savory (Select Any One)", table_header_style),
            Paragraph("Compartment 3: Sweets &amp; Drinks (Select Any One)", table_header_style)
        ],
        [
            Paragraph("• Nylon Khaman (3 pcs)<br/>• Idada / White Dhokla (4 pcs)<br/>• Sev Khamani (Portion)<br/>• Special Khandvi (4 pcs)<br/>• Patra (4 pcs)", table_cell_style),
            Paragraph("• Spiced Veg Samosa (1 pc)<br/>• Chinese Samosa (1 pc)<br/>• Crispy Spring Roll (1 pc)<br/>• Crunchy Gathiya (Portion)", table_cell_style),
            Paragraph("• Golden Sweet Jalebi (2 pcs)<br/>• Gulab Jamun (1 large pc)<br/>• Rich Mango Lassi (Small cup)<br/>• Chilled Sweet Lassi (Small cup)", table_cell_style)
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
            "<b>Catering Terms:</b><br/>"
            "• Please place all orders at least 24 hours prior to delivery.<br/>"
            "• We support full GST billing (GST invoice will be sent to your corporate email).<br/>"
            "• Food-grade biodegradable packaging is used for all custom packets.",
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
    
    story.append(Paragraph("2. EXECUTIVE 5-COMPARTMENT PLATTER", h1_style))
    story.append(Paragraph("<b>Corporate Package Price:</b> &#8377;160 per plate (Minimum Order Quantity: 20 Plates)", body_style))
    story.append(Paragraph("Our flagship executive platter designed for client lunches and formal corporate meetings.", body_style))
    story.append(Spacer(1, 5))
    
    # 5-Section Table
    five_sec_data = [
        [
            Paragraph("Category", table_header_style),
            Paragraph("Item Selections &amp; Portions (Includes Green &amp; Garlic Chutneys)", table_header_style)
        ],
        [
            Paragraph("<b>Compartment 1</b><br/>Gujarati Farsan", table_cell_bold),
            Paragraph("Select One: Nylon Khaman (3 pcs) / Idada (4 pcs) / Sev Khamani (Portion) / Khandvi (4 pcs)", table_cell_style)
        ],
        [
            Paragraph("<b>Compartment 2</b><br/>Fried Snack", table_cell_bold),
            Paragraph("Select One: Special Veg Samosa (1 pc) / Crispy Spring Roll (1 pc) / Chinese Samosa (1 pc)", table_cell_style)
        ],
        [
            Paragraph("<b>Compartment 3</b><br/>Gujarati Side", table_cell_bold),
            Paragraph("Select One: Soft Thepla with Pickles (2 pcs) / Steamed Patra (4 pcs) / Gathiya Bowl", table_cell_style)
        ],
        [
            Paragraph("<b>Compartment 4</b><br/>Sweets", table_cell_bold),
            Paragraph("Select One: Gulab Jamun (1 pc) / Sweet Jalebi (3 pcs) / Traditional Rasgulla (1 pc)", table_cell_style)
        ],
        [
            Paragraph("<b>Compartment 5</b><br/>Chilled Drink", table_cell_bold),
            Paragraph("Select One: Thick Mango Lassi (Medium cup) / Traditional Sweet Lassi / Spiced Masala Chhas", table_cell_style)
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
            "<font color='#ffffff'><b>READY TO ORDER A PACKET FOR YOUR EVENT?</b></font><br/>"
            "<font color='#fce6d8'>Click the 'Request a Corporate Quote' button on our website, fill out your inquiry, "
            "and send it to us via WhatsApp. Alternatively, call us directly at <b>+91 98252-61590</b>. "
            "We will return a customized proposal within 2 hours.</font>",
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
