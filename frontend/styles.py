def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top left, rgba(255, 93, 177, 0.22), transparent 34%),
                radial-gradient(circle at top right, rgba(59, 130, 246, 0.20), transparent 36%),
                linear-gradient(135deg, #fff7fc 0%, #f7f8ff 52%, #f6f0ff 100%);
            color: #1e1b4b;
        }

        [data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0);
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero-card {
            background: linear-gradient(135deg, #ff5db1 0%, #8b5cf6 48%, #3b82f6 100%);
            color: white;
            padding: 34px;
            border-radius: 28px;
            box-shadow: 0 20px 50px rgba(95, 72, 191, 0.25);
            margin-bottom: 26px;
            position: relative;
            overflow: hidden;
        }

        .hero-card::before {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: rgba(255,255,255,0.14);
            right: -70px;
            top: -90px;
        }

        .hero-title {
            font-size: 46px;
            font-weight: 800;
            line-height: 1.1;
            margin: 0;
            color: white;
            position: relative;
            z-index: 1;
        }

        .hero-subtitle {
            font-size: 17px;
            line-height: 1.7;
            max-width: 760px;
            margin-top: 14px;
            margin-bottom: 0;
            color: rgba(255,255,255,0.94);
            position: relative;
            z-index: 1;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
            position: relative;
            z-index: 1;
        }

        .chip {
            background: rgba(255,255,255,0.18);
            border: 1px solid rgba(255,255,255,0.28);
            border-radius: 999px;
            padding: 8px 13px;
            font-weight: 700;
            font-size: 13px;
            color: white;
        }

        .section-title {
            font-size: 28px;
            font-weight: 800;
            color: #1e1b4b;
            margin-top: 12px;
            margin-bottom: 8px;
        }

        .section-desc {
            color: #64748b;
            font-size: 16px;
            margin-bottom: 20px;
            line-height: 1.7;
        }

        .soft-card {
            background: rgba(255,255,255,0.90);
            border: 1px solid rgba(139, 92, 246, 0.16);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 14px 34px rgba(87, 73, 160, 0.10);
            margin-top: 18px;
        }

        .input-helper {
            background: rgba(255,255,255,0.78);
            border: 1px solid #e9d5ff;
            border-radius: 16px;
            padding: 14px 16px;
            color: #475569;
            margin-bottom: 14px;
            line-height: 1.6;
        }

        div.stButton > button {
            min-height: 50px;
            border-radius: 14px;
            font-weight: 800;
            border: none !important;
            background: linear-gradient(90deg, #ff5db1, #8b5cf6, #3b82f6) !important;
            color: white !important;
            box-shadow: 0 10px 22px rgba(139, 92, 246, 0.18);
            transition: 0.2s ease;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            filter: brightness(1.05);
            color: white !important;
            border: none !important;
            box-shadow: 0 14px 28px rgba(139, 92, 246, 0.25);
        }

        div.stButton > button:focus {
            color: white !important;
            border: none !important;
            box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.22);
        }

        [data-testid="stTextArea"] textarea {
            background: #ffffff !important;
            color: #1e1b4b !important;
            border: 2px solid #c4b5fd !important;
            border-radius: 18px !important;
            padding: 18px !important;
            min-height: 155px;
            font-size: 16px !important;
            box-shadow: 0 10px 25px rgba(109, 86, 210, 0.08);
            caret-color: #ff5db1 !important;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color: #ff5db1 !important;
            box-shadow: 0 0 0 4px rgba(255, 93, 177, 0.18);
        }

        [data-testid="stTextArea"] label {
            color: #1e1b4b !important;
            font-weight: 800 !important;
            font-size: 16px !important;
        }

        .result-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-top: 18px;
        }

        .result-card {
            border-radius: 20px;
            padding: 22px;
            min-height: 145px;
            box-shadow: 0 12px 26px rgba(88, 73, 160, 0.10);
        }

        .category-card {
            background: linear-gradient(145deg, #fff0f8, #ffe1f0);
            border: 1px solid #ffc9e1;
        }

        .priority-card {
            background: linear-gradient(145deg, #f4efff, #e7ddff);
            border: 1px solid #d8c9ff;
        }

        .unit-card {
            background: linear-gradient(145deg, #edf7ff, #dceeff);
            border: 1px solid #bfdbfe;
        }

        .card-icon {
            font-size: 34px;
            margin-bottom: 10px;
            color: #1e1b4b;
        }

        .card-label {
            color: #64748b;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 0.7px;
            text-transform: uppercase;
        }

        .card-value {
            color: #1e1b4b;
            font-size: 21px;
            font-weight: 800;
            line-height: 1.3;
            margin-top: 5px;
        }

        .summary-box {
            background: #ffffff;
            border: 1px solid #ece8fa;
            border-radius: 18px;
            color: #475569;
            padding: 18px;
            margin-top: 18px;
            line-height: 1.7;
            font-size: 16px;
        }

        .summary-box strong {
            color: #1e1b4b;
        }

        .flow-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            margin-top: 18px;
        }

        .flow-card {
            background: #ffffff;
            border: 1px solid #e9d5ff;
            border-radius: 18px;
            padding: 18px;
            text-align: center;
            min-height: 155px;
            box-shadow: 0 10px 22px rgba(87, 73, 160, 0.08);
        }

        .flow-icon {
            font-size: 34px;
            margin-bottom: 10px;
        }

        .flow-title {
            font-weight: 800;
            color: #1e1b4b;
            margin-bottom: 6px;
        }

        .flow-desc {
            color: #64748b;
            font-size: 14px;
            line-height: 1.5;
        }

        .about-text {
            color: #475569;
            line-height: 1.8;
            font-size: 16px;
        }

        .about-text strong {
            color: #1e1b4b;
        }

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 13px;
            margin-top: 28px;
            padding: 14px;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }

        .stTabs [data-baseweb="tab"] {
            background: rgba(255,255,255,0.72);
            border-radius: 999px;
            color: #4c1d95 !important;
            font-weight: 800;
            padding: 10px 18px;
            border: 1px solid rgba(139, 92, 246, 0.16);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(90deg, #ff5db1, #8b5cf6, #3b82f6) !important;
            color: white !important;
        }

        .stTabs [data-baseweb="tab"] p {
            color: inherit !important;
            font-weight: 800;
        }

        @media screen and (max-width: 800px) {
            .hero-title {
                font-size: 32px;
            }

            .result-grid,
            .flow-grid {
                grid-template-columns: 1fr;
            }

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>
    """