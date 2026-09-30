import streamlit as st
from transformers import pipeline

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Sentiment AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# HUGGING FACE MODEL
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

# ---------------------------------------------------------
# PREMIUM LIGHT THEME
# ---------------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f8faff 0%, #ffffff 45%, #f3f6ff 100%);
        color: #172033;
    }

    /* Remove Streamlit default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #ffffff 0%, #f5f7ff 100%);
        border: 1px solid #e5e9f5;
        border-radius: 24px;
        padding: 45px 50px;
        margin-bottom: 28px;
        box-shadow: 0 12px 40px rgba(30, 50, 100, 0.08);
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 220px;
        height: 220px;
        border-radius: 50%;
        background: rgba(91, 95, 255, 0.08);
        right: -70px;
        top: -80px;
    }

    .badge {
        display: inline-block;
        background: #eef0ff;
        color: #5759d9;
        border-radius: 50px;
        padding: 7px 14px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        margin: 0;
        color: #151b2e;
        letter-spacing: -1.5px;
    }

    .hero-title span {
        color: #5b5ff7;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #667085;
        margin-top: 12px;
        max-width: 700px;
        line-height: 1.6;
    }

    /* Section headings */
    .section-title {
        font-size: 20px;
        font-weight: 750;
        color: #172033;
        margin-bottom: 10px;
    }

    /* Text area */
    textarea {
        border: 1px solid #dfe4f0 !important;
        border-radius: 16px !important;
        background: #ffffff !important;
        color: #172033 !important;
        font-size: 16px !important;
        padding: 16px !important;
        box-shadow: 0 5px 20px rgba(30, 50, 100, 0.05) !important;
    }

    textarea:focus {
        border: 2px solid #6a6df5 !important;
        box-shadow: 0 0 0 4px rgba(106, 109, 245, 0.10) !important;
    }

    /* Analyze button */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: none;
        padding: 14px 20px;
        background: linear-gradient(135deg, #5b5ff7, #7657e8);
        color: white;
        font-size: 16px;
        font-weight: 700;
        box-shadow: 0 8px 22px rgba(91, 95, 247, 0.25);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(91, 95, 247, 0.32);
    }

    /* Result card */
    .result-card {
        background: #ffffff;
        border: 1px solid #e5e9f5;
        border-radius: 22px;
        padding: 30px;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 12px 35px rgba(30, 50, 100, 0.08);
    }

    .result-icon {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .result-label {
        font-size: 30px;
        font-weight: 800;
        color: #20263a;
        margin: 5px 0;
    }

    .result-confidence {
        color: #667085;
        font-size: 15px;
        margin-bottom: 18px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        border: 1px solid #e5e9f5;
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 8px 25px rgba(30, 50, 100, 0.06);
        height: 100%;
    }

    .metric-title {
        color: #7b8498;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .metric-value {
        color: #172033;
        font-size: 25px;
        font-weight: 800;
        margin-top: 7px;
    }

    /* Example cards */
    .example-title {
        font-size: 17px;
        font-weight: 750;
        color: #172033;
        margin-top: 30px;
        margin-bottom: 12px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #98a1b2;
        font-size: 13px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e8ebf3;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">

    <div class="badge">✦ AI-POWERED TEXT ANALYSIS</div>

    <div class="hero-title">
        Sentiment <span>Analyzer</span>
    </div>

    <div class="hero-subtitle">
        Understand the emotion behind your text using
        Artificial Intelligence and Natural Language Processing.
        Enter a review, comment, or message and let AI analyze it.
    </div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------
st.markdown(
    '<div class="section-title">Analyze your text</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Text input",
    placeholder="Type or paste your text here...",
    height=170,
    label_visibility="collapsed"
)

st.write("")

analyze = st.button("✦  Analyze Sentiment")


# ---------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------
if analyze:

    if text.strip() == "":
        st.warning("Please enter some text before analyzing.")

    else:

        with st.spinner("Analyzing sentiment..."):
            result = model(text)[0]

        label = result["label"]
        score = result["score"]
        confidence = score * 100

        # Determine icon
        if label.upper() == "POSITIVE":
            icon = "😊"
        elif label.upper() == "NEGATIVE":
            icon = "😞"
        else:
            icon = "😐"

        # Result
        st.markdown(f"""
        <div class="result-card">

            <div class="result-icon">{icon}</div>

            <div class="result-label">
                {label}
            </div>

            <div class="result-confidence">
                AI confidence score
            </div>

        </div>
        """, unsafe_allow_html=True)

        # Confidence progress
        st.progress(score)

        st.write("")

        # Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Sentiment</div>
                <div class="metric-value">{label}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Confidence</div>
                <div class="metric-value">{confidence:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Characters</div>
                <div class="metric-value">{len(text)}</div>
            </div>
            """, unsafe_allow_html=True)


# ---------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------
st.markdown(
    '<div class="example-title">Try an example</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("😊 Positive\n\nAmazing product! I absolutely loved it.")

with col2:
    st.info("😐 Neutral\n\nThe product arrived yesterday.")

with col3:
    st.info("😞 Negative\n\nThe product was disappointing and poor quality.")


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    ✦ Sentiment Analyzer &nbsp; • &nbsp;
    Powered by Hugging Face Transformers &nbsp; • &nbsp;
    Built with Streamlit
</div>
""", unsafe_allow_html=True)