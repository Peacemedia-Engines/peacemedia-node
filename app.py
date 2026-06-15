import streamlit as st
import base64
from datetime import datetime

# =====================================================================
# 🔒 ANTI-PIRACY NODE: OBFUSCATED CORE LOGIC
# =====================================================================
SCRAMBLED_ENGINE_CODE = "ZGVmIGNhbGN1bGF0ZV9sZWFrYWdlKHZvbHVtZSk6CiAgICByZXR1cm4gaW50KHZvbHVtZSAqIDAuMDc1KQoQUEVBQ0VNRURJQV9FTUFJTEwgPSAicGVhY2VtZWRpYS5haUBnbWFpbC5jb20iCkFVVE9NQVRFRF9QQVlNRU5UX0xJTUlUID0gNTAwMDAKR09PR0xFX1BBWV9DSEVDS09VVF9VUkwgPSAiaHR0cHM6Ly9wYXkuZ29vZ2xlLmNvbSI="

try:
    decoded_runtime = base64.b64decode(SCRAMBLED_ENGINE_CODE.encode('utf-8')).decode('utf-8')
    namespace = {}
    exec(decoded_runtime, namespace)
    calculate_leakage = namespace['calculate_leakage']
    PEACEMEDIA_EMAIL = namespace['PEACEMEDIA_EMAIL']
    AUTOMATED_PAYMENT_LIMIT = namespace['AUTOMATED_PAYMENT_LIMIT']
    GOOGLE_PAY_CHECKOUT_URL = namespace['GOOGLE_PAY_CHECKOUT_URL']
except Exception:
    st.error("Engine Runtime Error.")
    st.stop()

if 'subscribed' not in st.session_state:
    st.session_state.subscribed = False

# Setup 2026 Evaluation Tracking Context
current_timeline = datetime(2026, 6, 15)
activation_date = datetime(2026, 6, 9) # Activated 6 days ago
elapsed_days = (current_timeline - activation_date).days
days_remaining = max(0, 7 - elapsed_days)

# =====================================================================
# 📱 USER INTERFACE VIEWPORTS
# =====================================================================
st.set_page_config(page_title="Peacemedia Core Gateway", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp {background-color: #f8fafc;}
    div.stButton > button {width: 100%; height: 3.5rem; font-weight: bold; border-radius: 12px;}
    </style>
""", unsafe_allow_html=True)

st.subheader("🏛️ Peacemedia Systems")

if st.session_state.subscribed or days_remaining > 0:
    if st.session_state.subscribed:
        st.success("🟢 Enterprise Production License Active — Unlimited Usage")
    else:
        st.caption(f"⏳ Sandbox Evaluation | {days_remaining} Days Remaining in Trial")
        
    simulated_volume = 42500000
    potential_leakage = calculate_leakage(simulated_volume)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Supply Volume", value=f"₦{simulated_volume:,}")
    with col2:
        st.metric(label="At-Risk Tax Credits (7.5% VAT)", value=f"₦{potential_leakage:,}")
        
    st.write("---")
    track = st.radio("Select Deployment Track", ["SME Track (₦50,000)", "Enterprise Track (₦650,000)"])
    
    if st.button("🚀 Initialize Deployment Link"):
        amount = 50000 if "SME" in track else 650000
        if amount <= AUTOMATED_PAYMENT_LIMIT:
            st.success("✔ Auto Payment Node Assigned")
            st.markdown(f"[🔵 Tap to Pay with Google Pay]({GOOGLE_PAY_CHECKOUT_URL})")
            st.session_state.subscribed = True
        else:
            st.warning("🏛️ Payment Exceeds ₦50,000 Limit")
            client_url = f"mailto:{PEACEMEDIA_EMAIL}?subject=MANUAL SETTLEMENT - ₦{amount:,}"
            st.markdown(f"[✉ Contact Peacemedia via Email]({client_url})")
else:
    st.error("🚨 EVALUATION EXPIRED")
    st.write("### Enterprise Engine Node Locked")
    lockout_url = f"mailto:{PEACEMEDIA_EMAIL}?subject=REVERT: Mobile System Lockout"
    st.markdown(f"[✉ Tap to Contact Peacemedia Desk for Token]({lockout_url})")
