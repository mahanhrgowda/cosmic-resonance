import streamlit as st
from datetime import datetime
import numpy as np
import pytz
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Title with emoji
st.title("Cosmic Birth Resonance Explorer 🌟🔮")

# Fun intro
st.write("Enter two birth details and discover their cosmic resonance! 🎉 Using the triple helix model linked to string theory and the mantra 'Om Śrīṁ Bhūṁ Nīlāṁ Agni-Nābhiṁ Prabodhaya Svāhā', we'll map births to divine strings and calculate resonance! ✨")

# Input Section
st.header("Enter Birth Details")
col1, col2 = st.columns(2)

with col1:
    name1 = st.text_input("First Person's Name", value="Explorer 1")
    date1 = st.date_input("First Birth Date", value=datetime(1993, 7, 12).date())
    time1 = st.time_input("First Birth Time", value=datetime.strptime("12:26 PM", "%I:%M %p").time())
    tz1 = st.selectbox("First Time Zone", pytz.all_timezones, index=pytz.all_timezones.index("Asia/Kolkata"))

with col2:
    name2 = st.text_input("Second Person's Name", value="Explorer 2")
    date2 = st.date_input("Second Birth Date", value=datetime(1993, 1, 1).date())
    time2 = st.time_input("Second Birth Time", value=datetime.strptime("12:00 AM", "%I:%M %p").time())
    tz2 = st.selectbox("Second Time Zone", pytz.all_timezones, index=pytz.all_timezones.index("UTC"))

if st.button("Calculate Cosmic Resonance! 🚀"):
    # Fun effects
    st.balloons()

    # Convert to UTC
    def to_utc(date, time, tz_name):
        tz = pytz.timezone(tz_name)
        dt = datetime.combine(date, time).replace(tzinfo=tz)
        return dt.astimezone(pytz.UTC)

    dt1_utc = to_utc(date1, time1, tz1)
    dt2_utc = to_utc(date2, time2, tz2)
    st.write(f"{name1}'s Birth in UTC: {dt1_utc.strftime('%Y-%m-%d %H:%M:%S')} ⏰")
    st.write(f"{name2}'s Birth in UTC: {dt2_utc.strftime('%Y-%m-%d %H:%M:%S')} ⏰")

    # Reference date (Jan 1, 1900, UTC)
    ref_date = datetime(1900, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
    seconds1 = (dt1_utc - ref_date).total_seconds()
    seconds2 = (dt2_utc - ref_date).total_seconds()

    # Scale factor rooted in science (approx seconds in 7.44 years, from original model)
    scale_factor = 7.44 * 365.25 * 24 * 3600  # Years to seconds, ~234,436,800 seconds per Z unit
    z1 = seconds1 / scale_factor
    z2 = seconds2 / scale_factor
    st.write(f"{name1}'s Cosmic Z-Value: {z1:.6f} 🌌")
    st.write(f"{name2}'s Cosmic Z-Value: {z2:.6f} 🌌")

    # Dominant Energy (Shri, Bhu, Nila) using phase from helical model
    def get_dominant_energy(z):
        phase = np.sin(0.5 * z)  # Frequency from helical parameterization
        if phase > 0.33:
            return "Śrī (Prosperity) 💰✨ - Linked to open strings for dynamic interactions!"
        elif phase > -0.33:
            return "Bhū (Material Grounding) 🌍🏔️ - Linked to closed strings for gravitational stability!"
        else:
            return "Nīlā (Compassion) ❤️🙏 - Linked to heterotic strings for unifying symmetries!"

    energy1 = get_dominant_energy(z1)
    energy2 = get_dominant_energy(z2)
    st.write(f"{name1}'s Dominant Divine Energy: {energy1}")
    st.write(f"{name2}'s Dominant Divine Energy: {energy2}")

    # Cosmic Resonance Calculation (rooted in wave interference, like in quantum mechanics or string vibrations)
    delta_z = abs(z1 - z2)
    phase_diff = 0.5 * delta_z  # Phase difference from helical frequency
    resonance_score = (1 + np.cos(phase_diff)) / 2  # Interference formula, 1=perfect resonance, 0=no resonance
    st.write(f"Cosmic Resonance Score (0-1, 1=perfect wave alignment): {resonance_score:.2f} 🌊")

    # Cosmic Alignment Year (midpoint in years, like barycenter in physics)
    midpoint_seconds = (seconds1 + seconds2) / 2
    alignment_date = ref_date + timedelta(seconds=midpoint_seconds)
    alignment_year = alignment_date.year
    st.write(f"Cosmic Alignment Year (barycenter-like midpoint): {alignment_year} CE - Where your energies harmonize! ⭐")

    # Time Harmony (time dilation-inspired, using relative time difference)
    time_diff_seconds = abs(seconds1 - seconds2)
    time_diff_years = time_diff_seconds / (365.25 * 24 * 3600)
    harmony_score = np.exp(-time_diff_years / 7.44)  # Exponential decay, like relativistic effects, scaled to original factor
    st.write(f"Time Harmony Score (0-1, 1=close in time): {harmony_score:.2f} ⏳")

    # Mantra Interpretation with linkage
    st.subheader("Mantra Magic 🔮")
    st.write("The mantra 'Om Śrīṁ Bhūṁ Nīlāṁ Agni-Nābhiṁ Prabodhaya Svāhā' awakens fiery energy at the cosmic center! 🌋")
    st.write("Link to Triple Helix and String Theory: The triple helix model, with strands for Śrī, Bhū, and Nīlā, mirrors string theory's open, closed, and heterotic strings in the spacetime continuum. Śrīṁ invokes prosperity through open strings' dynamic interactions (particle-like vibrations in branes), Bhūṁ grounds material reality via closed strings' loops (gravitons mediating gravity in the block universe), and Nīlāṁ unifies compassion with heterotic strings' hybrid symmetries (E8×E8 or SO(32) gauge groups addressing low-energy unification). Convergence points, like your births, are wave peaks where these strings align, resonating in the eternal block universe! 🌊🔗")

    # 3D Helical Plot using Plotly
    st.subheader("3D Helical Plot with Birth Positions")
    Z = np.linspace(-6000, 2100, 1000)  # Years BCE to CE
    phi = [0, 2*np.pi/3, 4*np.pi/3]  # Phase shifts
    data = []
    for i, color in enumerate(['#FFD700', '#FF8C00', '#FF0000']):  # Gold, Orange, Red
        X = 0.5 * np.sin(0.000001 * Z + phi[i])
        Y = 0.25 * np.cos(0.000001 * Z + phi[i])
        trace = go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=f'Strand {i+1}', line=dict(color=color))
        data.append(trace)

    # Birth markers
    birth_markers = [
        go.Scatter3d(x=[0], y=[0], z=[dt1_utc.year], mode='markers+text', name=f'{name1}',
                     marker=dict(symbol='circle', size=10, color='#0000FF'),
                     text=[f'{name1}: {dt1_utc.strftime("%Y-%m-%d %H:%M")}'], textposition="top center"),
        go.Scatter3d(x=[0], y=[0], z=[dt2_utc.year], mode='markers+text', name=f'{name2}',
                     marker=dict(symbol='circle', size=10, color='#00FF00'),
                     text=[f'{name2}: {dt2_utc.strftime("%Y-%m-%d %H:%M")}'], textposition="top center")
    ]
    data.extend(birth_markers)

    fig = go.Figure(data=data)
    fig.update_layout(scene=dict(xaxis_title='Time Strand (-1 to 1)',
                                 yaxis_title='Cosmic Flow (-1 to -0.25)',
                                 zaxis_title='Year (BCE/CE)'),
                      title='Triple Helix with Birth Positions')
    st.plotly_chart(fig)

    # Timeline Plot
    st.subheader("Timeline Plot with Birth Positions")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([dt1_utc.year, dt2_utc.year], [0, 0], 'bo-', label='Births')
    ax.plot(dt1_utc.year, 0, 'bo', label=name1)
    ax.plot(dt2_utc.year, 0, 'go', label=name2)
    ax.text(dt1_utc.year, 0.1, f'{name1}: {dt1_utc.strftime("%Y-%m-%d %H:%M")}', rotation=45, fontsize=8)
    ax.text(dt2_utc.year, 0.1, f'{name2}: {dt2_utc.strftime("%Y-%m-%d %H:%M")}', rotation=45, fontsize=8)
    ax.set_xlabel('Year (CE)')
    ax.set_ylabel('Convergence Level')
    ax.set_title('Timeline of Birth Positions')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Fun effects
    st.success("Cosmic connection unlocked! Share your resonance story! 😊")
    st.confetti()  # Assuming available, or simulate with text