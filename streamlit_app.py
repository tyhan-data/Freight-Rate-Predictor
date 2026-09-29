import html
from datetime import date

import requests
import streamlit as st

# ==========================================
# Configuration
# ==========================================

API_URL = "https://freight-rate-predictor-1z8w.onrender.com/predict"

st.set_page_config(
    page_title="Freight Rate Prediction",
    page_icon="🚚",
    layout="wide",
)

# ==========================================
# Styling
# ==========================================

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg, #eef4fb 0%, #f8fafc 60%); }
    .block-container { padding-top: 1.5rem; max-width: 1100px; }

    /* Hero */
    .hero {
        background: linear-gradient(120deg, #0f2a4a 0%, #1565c0 55%, #00b4a6 100%);
        color: #fff; padding: 2rem 2.2rem; border-radius: 18px;
        box-shadow: 0 10px 28px rgba(21,101,192,.25); margin-bottom: 1.5rem;
    }
    .hero h1 { margin: 0; font-size: 2.2rem; color: #fff; }
    .hero p  { margin: .4rem 0 0; opacity: .9; font-size: 1.05rem; }

    /* Section titles */
    .section-title {
        font-size: 1.15rem; font-weight: 700; color: #0f2a4a;
        border-left: 5px solid #00b4a6; padding-left: .6rem; margin: .4rem 0 .8rem;
    }

    /* Summary card */
    .summary-card {
        background: #fff; border-radius: 16px; padding: 1.2rem 1.3rem;
        border: 1px solid #dbe6f3; box-shadow: 0 6px 18px rgba(15,42,74,.08);
    }
    .summary-row {
        display: flex; justify-content: space-between; align-items: center;
        padding: .55rem 0; border-bottom: 1px dashed #e3ebf5;
    }
    .summary-row:last-child { border-bottom: none; }
    .summary-label { color: #5b6b80; font-size: .9rem; }
    .chip {
        background: #e6f3ff; color: #0f4c8a; font-weight: 600;
        padding: .2rem .7rem; border-radius: 999px; font-size: .9rem;
    }
    .chip.empty { background: #fdecea; color: #b3261e; }

    /* Result card */
    .result-card {
        background: linear-gradient(135deg, #00b4a6, #1565c0); color: #fff;
        border-radius: 16px; padding: 1.4rem; text-align: center; margin-top: 1rem;
        box-shadow: 0 10px 24px rgba(0,180,166,.3);
    }
    .result-card .label { opacity: .9; font-size: .95rem; }
    .result-card .value { font-size: 2.4rem; font-weight: 800; }

    /* Button */
    div.stButton > button {
        width: 100%; background: linear-gradient(90deg, #1565c0, #00b4a6);
        color: #fff; border: none; border-radius: 12px;
        padding: .75rem 1rem; font-size: 1.05rem; font-weight: 700;
        transition: transform .15s ease, box-shadow .15s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px); color: #fff;
        box-shadow: 0 8px 20px rgba(21,101,192,.35);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] { background: #0f2a4a; }
    section[data-testid="stSidebar"] * { color: #e8f0fa !important; }
    section[data-testid="stSidebar"] code {
        background: rgba(255,255,255,.12); color: #7ff0e6 !important;
    }
    .rule-card {
        background: rgba(255,255,255,.07); border-left: 4px solid #00b4a6;
        border-radius: 10px; padding: .7rem .9rem; margin-bottom: .7rem;
        font-size: .9rem;
    }
    .rule-card b { color: #7ff0e6 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# Sidebar - Instructions & Rules
# ==========================================

with st.sidebar:
    st.header("📋 Instructions")
    st.caption("Follow these rules to get an accurate estimate.")

    st.markdown(
        """
        <div class="rule-card"><b>📍 Locations</b><br>
        Required · 2–50 characters<br>
        Each word starts with a capital letter<br>
        Pickup and delivery must differ<br>
        e.g. <code>Oklahoma City</code>, <code>Hartford</code></div>

        <div class="rule-card"><b>📏 Distance</b><br>
        Minimum <code>1</code> mile · Maximum <code>10,000</code> miles</div>

        <div class="rule-card"><b>⚖️ Weight</b><br>
        Minimum <code>1</code> lb · Maximum <code>100,000</code> lb</div>

        <div class="rule-card"><b>🚛 Equipment</b><br>
        Dry Van · Reefer equipment · Flatbed</div>

        <div class="rule-card"><b>📅 Shipment Date</b><br>
        Pick the full date. Year, month and day are extracted automatically.</div>

        <div class="rule-card"><b>🛡️ Backend Validation</b><br>
        The FastAPI backend performs additional checks using Pydantic.</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("**How to use**")
    st.markdown(
        "1. Fill in the shipment details\n"
        "2. Review your selections on the right\n"
        "3. Click **Predict Freight Rate**"
    )

# ==========================================
# Header
# ==========================================

st.markdown(
    """
    <div class="hero">
        <h1>🚚 Freight Rate Prediction</h1>
        <p>Enter your shipment details and get an instant estimated posted rate.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# Layout: Form (left) | Summary (right)
# ==========================================

form_col, summary_col = st.columns([3, 2], gap="large")

with form_col:
    st.markdown('<div class="section-title">📍 Route</div>', unsafe_allow_html=True)
    loc_1, loc_2 = st.columns(2)
    with loc_1:
        pickup = st.text_input(
            "Pickup Location *",
            placeholder="e.g. Oklahoma City",
            max_chars=50,
            help="Required. 2–50 characters. Each word starts with an uppercase letter.",
        )
    with loc_2:
        delivery = st.text_input(
            "Delivery Location *",
            placeholder="e.g. Hartford",
            max_chars=50,
            help="Required. 2–50 characters. Each word starts with an uppercase letter.",
        )

    st.markdown('<div class="section-title">📦 Shipment Details</div>', unsafe_allow_html=True)
    det_1, det_2 = st.columns(2)
    with det_1:
        distance = st.number_input(
            "Distance (miles) *",
            min_value=1, max_value=10000, value=100, step=1,
            help="Allowed range: 1–10,000 miles.",
        )
        equipment = st.selectbox(
            "Equipment *",
            options=["Dry Van", "Reefer equipment", "Flatbed"],
            help="Select the equipment type used for the shipment.",
        )
    with det_2:
        weight = st.number_input(
            "Weight (lb) *",
            min_value=1, max_value=100000, value=1000, step=1,
            help="Allowed range: 1–100,000 lb.",
        )
        shipment_date = st.date_input(
            "Shipment Date *",
            value=date(2025, 12, 15),
            help="Year, month and day are extracted automatically.",
        )

    # Soft (non-blocking) capitalization hint
    for label, value in (("Pickup", pickup), ("Delivery", delivery)):
        if value.strip() and value.strip() != value.strip().title():
            st.info(f"💡 {label} location: start each word with an uppercase letter.")

    predict_clicked = st.button("🔮 Predict Freight Rate")

# ==========================================
# Live Submission Summary
# ==========================================


def chip(value):
    text = html.escape(str(value).strip()) if str(value).strip() else "Not provided"
    css = "chip" if str(value).strip() else "chip empty"
    return f'<span class="{css}">{text}</span>'


with summary_col:
    st.markdown('<div class="section-title">🧾 Your Submission</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-row"><span class="summary-label">📍 Pickup</span>{chip(pickup)}</div>
            <div class="summary-row"><span class="summary-label">🏁 Delivery</span>{chip(delivery)}</div>
            <div class="summary-row"><span class="summary-label">📏 Distance</span>{chip(f"{distance:,} mi")}</div>
            <div class="summary-row"><span class="summary-label">⚖️ Weight</span>{chip(f"{weight:,} lb")}</div>
            <div class="summary-row"><span class="summary-label">🚛 Equipment</span>{chip(equipment)}</div>
            <div class="summary-row"><span class="summary-label">📅 Date</span>{chip(shipment_date.strftime("%d %b %Y"))}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    result_slot = st.empty()

# ==========================================
# Validation
# ==========================================
MAX_DISTANCE = 10000
MAX_WEIGHT = 100000

def validate(pickup, delivery, distance, weight):
    """Return an error message, or None if the input is valid."""

    # Validate pickup and delivery
    for name, value in (("Pickup", pickup), ("Delivery", delivery)):

        value = value.strip()

        if not value:
            return f"{name} location cannot be empty."

        if len(value) < 2:
            return f"{name} location must contain at least 2 characters."

        if len(value) > 50:
            return f"{name} location cannot exceed 50 characters."

    # Pickup and delivery must be different
    if pickup.strip().lower() == delivery.strip().lower():
        return "Pickup and delivery locations must be different."

    # Validate distance
    if distance <= 0:
        return "Distance must be greater than 0 miles."

    if distance > MAX_DISTANCE:
        return f"Distance cannot exceed {MAX_DISTANCE} miles. Please enter a value within the allowed range."

    # Validate weight
    if weight <= 0:
        return "Weight must be greater than 0 lbs."

    if weight > MAX_WEIGHT:
        return f"Weight cannot exceed {MAX_WEIGHT} lbs. Please enter a value within the allowed range."

    return None


# ==========================================
# Prediction
# ==========================================

if predict_clicked:

    error = validate(
        pickup,
        delivery,
        distance,
        weight
    )

    if error:
        st.error(f"❌ {error}")
        st.stop()
    
    input_data = {
        "pickup": pickup.strip(),
        "delivery": delivery.strip(),
        "distance": distance,
        "equipment": equipment,
        "weight": weight,
        "year": shipment_date.year,
        "month": shipment_date.month,
        "day": shipment_date.day,
    }

    try:
        with st.spinner("Calculating your freight rate..."):
            response = requests.post(url=API_URL, json=input_data, timeout=30)

        if response.status_code == 200:
            try:
                prediction = response.json()["posted_rate"]
                result_slot.markdown(
                    f"""
                    <div class="result-card">
                        <div class="label">💰 Estimated Posted Rate</div>
                        <div class="value">${prediction:,.2f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.balloons()
            except (ValueError, KeyError):
                st.error("❌ The API returned an invalid response.")

        elif response.status_code == 422:
            st.error("❌ Invalid input. Please check the input requirements.")
        elif response.status_code == 500:
            st.error("❌ Internal server error. Please try again later.")
        else:
            st.error(f"❌ Unexpected API error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Couldn't connect to the API. Please make sure the FastAPI server is running.")
    except requests.exceptions.Timeout:
        st.error("❌ The request timed out. Please try again.")
    except Exception as e:
        st.error("❌ An unexpected error occurred.")
        st.caption(f"Error details: {type(e).__name__}: {e}")