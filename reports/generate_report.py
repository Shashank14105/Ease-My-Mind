import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def load_report_data():

    conn = sqlite3.connect("database/mood_history.db")

    df = pd.read_sql_query(
        "SELECT * FROM mood_logs ORDER BY timestamp DESC",
        conn
    )

    conn.close()

    return df

#Charts for report 
def create_charts(df):

    # Stress Distribution Pie Chart
    stress_count = df["stress_level"].value_counts()

    plt.figure(figsize=(5,5))

    plt.pie(
        stress_count.values,
        labels=stress_count.index,
        autopct="%1.1f%%"
    )

    plt.title("Stress Distribution")

    plt.savefig(
        "reports_output/stress_chart.png"
    )

    plt.close()


    # Sentiment Distribution Bar Chart

    sentiment_count = df["sentiment"].value_counts()

    plt.figure(figsize=(6,4))

    plt.bar(
        sentiment_count.index,
        sentiment_count.values
    )

    plt.title("Sentiment Distribution")

    plt.ylabel("Count")

    plt.savefig(
        "reports_output/sentiment_chart.png"
    )

    plt.close()

#Footer
def add_footer(canvas, doc):

    canvas.saveState()

    canvas.setFont("Helvetica", 8)

    canvas.setFillColor(colors.grey)

    canvas.drawCentredString(
        300,
        20,
        "Powered by Ease My Mind · Developed by Shashank"
    )

    canvas.restoreState()

#Generate PDF
def generate_pdf():

    df = load_report_data()

    if df.empty:
        print("No wellness records found.")
        return

    latest = df.iloc[0]
    create_charts(df)

    doc = SimpleDocTemplate(
        "reports_output/wellness_report.pdf"
    )

    styles = getSampleStyleSheet()

    from reportlab.lib.styles import ParagraphStyle
    from datetime import datetime

    # Custom styles
    advice_style = ParagraphStyle(
        "AdviceStyle",
        parent=styles["BodyText"],
        leading=18,
        spaceAfter=8
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent= styles["Heading2"],
        textColor=colors.darkblue,
        spaceAfter=12
    )

    quote_style = ParagraphStyle(
        "QuoteStyle",
        parent=styles["BodyText"],
        textColor=colors.darkgreen,
        alignment=1,
        italic=True,
        leading=18
    )

    story = []

    # Logo + Header
    logo = Image(
        "assets/logo.png",
        width=60,
        height=60
    )

    title = Paragraph(
        "Ease My Mind Wellness Report",
        styles["Title"]
    )

    date_paragraph = Paragraph(
        f"Generated on: {datetime.now().strftime('%d %B %Y')}",
        styles["BodyText"]
    )

    header_table = Table(
        [
            [
                [title, date_paragraph],
                logo
            ]
        ],
        colWidths=[430, 70]
    )

    header_table.setStyle(
        TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ])
    )

    story.append(header_table)
    story.append(Spacer(1, 25))

    
    # Wellness Summary
    story.append(
        HRFlowable(
            width="100%",
            color=colors.lightgrey
        )
    )

    story.append(
        Spacer(1,10)
    )

    story.append(
        Paragraph(
            "Current Wellness Summary",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"Stress Level : {latest['stress_level']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Sentiment : {latest['sentiment']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Sleep Duration : {latest['sleep_duration']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    
    # Latest Journal
    story.append(
        HRFlowable(
            width="100%",
            color=colors.lightgrey
        )
    )

    story.append(
        Spacer(1,10)
    )
    story.append(
        Paragraph(
            "Latest Journal Entry",
            heading_style
        )
    )

    story.append(
        Paragraph(
            latest["journal"],
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    
    # Gemini Advice
    story.append(
        HRFlowable(
            width="100%",
            color=colors.lightgrey
        )
    )

    story.append(
        Spacer(1,10)
    )
    story.append(
        Paragraph(
            "AI Wellness Coach Recommendation",
            heading_style
        )
    )

    advice_lines = latest["gemini_advice"].split("\n")

    for line in advice_lines:

        line = line.replace("**", "")
        line = line.replace("*", "")

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    advice_style
                )
            )

            story.append(
                Spacer(1, 4)
            )

    story.append(Spacer(1, 15))

    
    # Recent History Table
    story.append(
        HRFlowable(
            width="100%",
            color=colors.lightgrey
        )
    )

    story.append(
        Spacer(1,10)
    )

    story.append(
        Paragraph(
            "Recent Wellness History",
            heading_style
        )
    )

    recent = df.head(7)

    table_data = [
        ["Date", "Stress Level", "Sentiment"]
    ]

    for _, row in recent.iterrows():

        date = str(row["timestamp"])[:10]

        table_data.append(
            [
                date,
                row["stress_level"],
                row["sentiment"]
            ]
        )

    history_table = Table(
        table_data,
        colWidths=[100, 150, 120]
    )

    history_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('PADDING', (0, 0), (-1, -1), 8)
        ])
    )

    story.append(history_table)

    story.append(Spacer(1, 20))

    #Wellness Analytics
    story.append(
    HRFlowable(
        width="100%",
        color=colors.lightgrey
        )
    )

    story.append(
        Spacer(1,10)
    )

    story.append(
        Paragraph(
            "Wellness Analytics",
            heading_style
        )
    )

    stress_chart = Image(
        "reports_output/stress_chart.png",
        width=300,
        height=300
    )

    story.append(stress_chart)

    story.append(
        Spacer(1,15)
    )

    sentiment_chart = Image(
        "reports_output/sentiment_chart.png",
        width=300,
        height=230
    )

    story.append(sentiment_chart)
    
    story.append(
        Spacer(1,15)
    )

    story.append(
    HRFlowable(
        width="100%",
        color=colors.lightgrey
        )
    )

    story.append(
        Paragraph(
            '"Progress, not perfection."',
            quote_style
        )
    )

    
    # Build PDF
    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer
    )

    print("Wellness report generated successfully!")

# Test
if __name__ == "__main__":
    generate_pdf()