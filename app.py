import streamlit as st
from datetime import datetime, timedelta
import time

# Define the elements and their string theory mappings with emojis
elements = {
    0: {"name": "Fire (Type I)", "emoji": "🔥", "qualities": "Heat, transformation, dynamism"},
    1: {"name": "Water (Type IIA)", "emoji": "💧", "qualities": "Fluidity, cohesion, adaptability"},
    2: {"name": "Air (Type IIB)", "emoji": "🌬️", "qualities": "Mobility, lightness, expansion"},
    3: {"name": "Earth (Heterotic SO(32))", "emoji": "🌍", "qualities": "Stability, solidity, grounding"},
    4: {"name": "Ether (Heterotic E8×E8)", "emoji": "✨", "qualities": "Space, subtlety, connectivity"}
}

# Predefined connections based on the research analogies
connections = {
    ("Fire (Type I)", "Air (Type IIB)"): {
        "resonance": "High", "harmony": "Amplifying 💥", 
        "description": "Like wind fueling a flame! Your times resonate with dynamic energy transfer, echoing S-duality in string theory. Perfect for adventurous souls! 🌟"
    },
    ("Water (Type IIA)", "Ether (Heterotic E8×E8)"): {
        "resonance": "Moderate", "harmony": "Subtle Flow 🌊✨", 
        "description": "Ripples in the cosmic void! Fluid adaptability meets pervasive space, linked by T-duality. Ideal for deep, intuitive connections! 🌀"
    },
    ("Earth (Heterotic SO(32))", "Fire (Type I)"): {
        "resonance": "Low", "harmony": "Tempered Strength 🔥🌍", 
        "description": "Fire refines earth into strength! Grounded stability meets transformative heat, stabilized by anomaly cancellations. Great for building lasting bonds! ⚒️"
    },
    ("Air (Type IIB)", "Water (Type IIA)"): {
        "resonance": "Variable", "harmony": "Stormy Cycles 🌬️💧", 
        "description": "Winds over waves create epic cycles! Mobility blends with flow via T-duality. Fun for creative, evolving partnerships! ☁️"
    },
    ("Ether (Heterotic E8×E8)", "Earth (Heterotic SO(32))"): {
        "resonance": "Deep", "harmony": "Foundational Unity ✨🌍", 
        "description": "Ether pervades earth in timeless unity! Connected via M-theory's hidden dimensions. For profound, grounded harmonies! 🌌"
    },
    # Add reverses for symmetry
    ("Air (Type IIB)", "Fire (Type I)"): {
        "resonance": "High", "harmony": "Amplifying 💥", 
        "description": "Like wind fueling a flame! Your times resonate with dynamic energy transfer, echoing S-duality in string theory. Perfect for adventurous souls! 🌟"
    },
    ("Ether (Heterotic E8×E8)", "Water (Type IIA)"): {
        "resonance": "Moderate", "harmony": "Subtle Flow 🌊✨", 
        "description": "Ripples in the cosmic void! Fluid adaptability meets pervasive space, linked by T-duality. Ideal for deep, intuitive connections! 🌀"
    },
    ("Fire (Type I)", "Earth (Heterotic SO(32))"): {
        "resonance": "Low", "harmony": "Tempered Strength 🔥🌍", 
        "description": "Fire refines earth into strength! Grounded stability meets transformative heat, stabilized by anomaly cancellations. Great for building lasting bonds! ⚒️"
    },
    ("Water (Type IIA)", "Air (Type IIB)"): {
        "resonance": "Variable", "harmony": "Stormy Cycles 🌬️💧", 
        "description": "Winds over waves create epic cycles! Mobility blends with flow via T-duality. Fun for creative, evolving partnerships! ☁️"
    },
    ("Earth (Heterotic SO(32))", "Ether (Heterotic E8×E8)"): {
        "resonance": "Deep", "harmony": "Foundational Unity ✨🌍", 
        "description": "Ether pervades earth in timeless unity! Connected via M-theory's hidden dimensions. For profound, grounded harmonies! 🌌"
    },
    # Same element cases
    ("Fire (Type I)", "Fire (Type I)"): {
        "resonance": "Explosive", "harmony": "Blazing Sync 🔥🔥", 
        "description": "Twin flames ignite the cosmos! Perfect vibrational match in Type I strings. Super dynamic duo! 💥"
    },
    ("Water (Type IIA)", "Water (Type IIA)"): {
        "resonance": "Flowing", "harmony": "Oceanic Merge 💧💧", 
        "description": "Waves in harmony! Cohesive fluidity doubles via IIA dualities. Deep emotional bonds! 🌊"
    },
    ("Air (Type IIB)", "Air (Type IIB)"): {
        "resonance": "Whirling", "harmony": "Breezy Freedom 🌬️🌬️", 
        "description": "Winds dancing together! Self-dual expansions in IIB. Free-spirited adventures await! 🌀"
    },
    ("Earth (Heterotic SO(32))", "Earth (Heterotic SO(32))"): {
        "resonance": "Solid", "harmony": "Rock Steady 🌍🌍", 
        "description": "Unshakeable foundations! Hybrid stability in SO(32). Reliable partners forever! 🏔️"
    },
    ("Ether (Heterotic E8×E8)", "Ether (Heterotic E8×E8)"): {
        "resonance": "Eternal", "harmony": "Cosmic Void ✨✨", 
        "description": "Infinite connectivity! Exceptional unity in E8×E8. Timeless soul links! 🌌"
    },
    # Default for unmapped pairs (add more if needed, but for fun, generalize)
}

# Function to get default connection if not predefined
def get_default_connection(elem1, elem2):
    return {
        "resonance": "Mysterious", "harmony": "Quantum Surprise ❓", 
        "description": f"{elem1['emoji']} meets {elem2['emoji']} in a wild string twist! Explore uncharted resonances in the multiverse. Fun surprises ahead! 🎉"
    }

# Function to map datetime to element index (pseudo-scientific vibration calc)
def get_element_index(birth_dt):
    # Sum components for 'vibration'
    vibration = birth_dt.year + birth_dt.month + birth_dt.day + birth_dt.hour + birth_dt.minute + birth_dt.second
    # Modulo 5 for 5 elements
    return vibration % 5

# Streamlit app
st.title("🌌 String Theory Soulmates: Elemental Harmony Calculator! ✨")

st.markdown("""
Welcome to this fun app inspired by string theory and ancient Panchabhuta elements! 🎉  
Enter the birth dates and exact times (down to seconds) for two people, and discover their spacetime connection.  
Rooted in physics analogies: Your birth moments map to vibrating strings and elements, revealing resonance and harmony! 🚀  
""")

# Input for Person 1
st.header("Person 1 👤")
date1 = st.date_input("Birth Date (Person 1)", value=datetime(2000, 1, 1))
time1 = st.time_input("Birth Time (Person 1)", value=datetime(2000, 1, 1, 12, 0, 0).time())
sec1 = st.slider("Birth Second (Person 1)", 0, 59, 0)
birth1 = datetime(date1.year, date1.month, date1.day, time1.hour, time1.minute, sec1)

# Input for Person 2
st.header("Person 2 👥")
date2 = st.date_input("Birth Date (Person 2)", value=datetime(2000, 1, 1))
time2 = st.time_input("Birth Time (Person 2)", value=datetime(2000, 1, 1, 12, 0, 0).time())
sec2 = st.slider("Birth Second (Person 2)", 0, 59, 0)
birth2 = datetime(date2.year, date2.month, date2.day, time2.hour, time2.minute, sec2)

if st.button("Calculate Harmony! 🔮"):
    if birth1 == birth2:
        st.warning("Birth times are identical! In spacetime, that's a singularity—try different times! ⚠️")
    else:
        # Get elements
        idx1 = get_element_index(birth1)
        idx2 = get_element_index(birth2)
        elem1 = elements[idx1]
        elem2 = elements[idx2]
        
        # Time difference for fun 'resonance factor'
        delta = abs(birth1 - birth2)
        days_diff = delta.days
        resonance_factor = (days_diff % 11) * 10  # Nod to 11D M-theory, fun score 0-100
        
        st.header("Your Elemental Mappings 🌟")
        st.markdown(f"**Person 1:** {elem1['name']} {elem1['emoji']} - {elem1['qualities']}")
        st.markdown(f"**Person 2:** {elem2['name']} {elem2['emoji']} - {elem2['qualities']}")
        
        # Get connection
        key = (elem1['name'], elem2['name'])
        conn = connections.get(key, get_default_connection(elem1, elem2))
        
        st.header("Spacetime Connection Analysis 🪐")
        st.markdown(f"**Resonance:** {conn['resonance']} {elem1['emoji']}{elem2['emoji']}")
        st.markdown(f"**Harmony:** {conn['harmony']}")
        st.markdown(f"**Description:** {conn['description']}")
        st.markdown(f"**Compatibility Score (M-Theory Inspired):** {resonance_factor}% ❤️")
        
        # Fun animation
        with st.spinner("Vibrating strings in higher dimensions..."):
            time.sleep(1)
        st.balloons()
