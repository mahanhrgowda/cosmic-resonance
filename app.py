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

# Predefined connections for ALL possible pairs (25 combinations) with base scores and Big Bang analogies
connections = {
    # Original ones
    ("Fire (Type I)", "Air (Type IIB)"): {
        "resonance": "High", "harmony": "Amplifying 💥", 
        "description": "Like wind fueling a flame! Your times resonate with dynamic energy transfer, echoing S-duality in string theory. Perfect for adventurous souls! 🌟",
        "base_score": 90,
        "big_bang_analogy": "Symmetry-breaking event where elements converge to spark cosmic expansion, just like string theory's Big Bang simulation! 💥🌌"
    },
    ("Water (Type IIA)", "Ether (Heterotic E8×E8)"): {
        "resonance": "Moderate", "harmony": "Subtle Flow 🌊✨", 
        "description": "Ripples in the cosmic void! Fluid adaptability meets pervasive space, linked by T-duality. Ideal for deep, intuitive connections! 🌀",
        "base_score": 70,
        "big_bang_analogy": "Pre-Big Bang state transitioning smoothly, avoiding singularity through string dualities! 🌊✨"
    },
    ("Earth (Heterotic SO(32))", "Fire (Type I)"): {
        "resonance": "Low", "harmony": "Tempered Strength 🔥🌍", 
        "description": "Fire refines earth into strength! Grounded stability meets transformative heat, stabilized by anomaly cancellations. Great for building lasting bonds! ⚒️",
        "base_score": 50,
        "big_bang_analogy": "Dense, hot matter state at the singularity, refined by string interactions to form the universe! 🔥🌍"
    },
    ("Air (Type IIB)", "Water (Type IIA)"): {
        "resonance": "Variable", "harmony": "Stormy Cycles 🌬️💧", 
        "description": "Winds over waves create epic cycles! Mobility blends with flow via T-duality. Fun for creative, evolving partnerships! ☁️",
        "base_score": 60,
        "big_bang_analogy": "Cyclic expansions from a converged point, mimicking eternal inflation in string cosmology! 🌬️💧"
    },
    ("Ether (Heterotic E8×E8)", "Earth (Heterotic SO(32))"): {
        "resonance": "Deep", "harmony": "Foundational Unity ✨🌍", 
        "description": "Ether pervades earth in timeless unity! Connected via M-theory's hidden dimensions. For profound, grounded harmonies! 🌌",
        "base_score": 95,
        "big_bang_analogy": "Unified higher-dimensional state before the Big Bang, where all elements converge in M-theory! ✨🌍"
    },
    # Reverses
    ("Air (Type IIB)", "Fire (Type I)"): {
        "resonance": "High", "harmony": "Amplifying 💥", 
        "description": "Like wind fueling a flame! Your times resonate with dynamic energy transfer, echoing S-duality in string theory. Perfect for adventurous souls! 🌟",
        "base_score": 90,
        "big_bang_analogy": "Symmetry-breaking event where elements converge to spark cosmic expansion, just like string theory's Big Bang simulation! 💥🌌"
    },
    ("Ether (Heterotic E8×E8)", "Water (Type IIA)"): {
        "resonance": "Moderate", "harmony": "Subtle Flow 🌊✨", 
        "description": "Ripples in the cosmic void! Fluid adaptability meets pervasive space, linked by T-duality. Ideal for deep, intuitive connections! 🌀",
        "base_score": 70,
        "big_bang_analogy": "Pre-Big Bang state transitioning smoothly, avoiding singularity through string dualities! 🌊✨"
    },
    ("Fire (Type I)", "Earth (Heterotic SO(32))"): {
        "resonance": "Low", "harmony": "Tempered Strength 🔥🌍", 
        "description": "Fire refines earth into strength! Grounded stability meets transformative heat, stabilized by anomaly cancellations. Great for building lasting bonds! ⚒️",
        "base_score": 50,
        "big_bang_analogy": "Dense, hot matter state at the singularity, refined by string interactions to form the universe! 🔥🌍"
    },
    ("Water (Type IIA)", "Air (Type IIB)"): {
        "resonance": "Variable", "harmony": "Stormy Cycles 🌬️💧", 
        "description": "Winds over waves create epic cycles! Mobility blends with flow via T-duality. Fun for creative, evolving partnerships! ☁️",
        "base_score": 60,
        "big_bang_analogy": "Cyclic expansions from a converged point, mimicking eternal inflation in string cosmology! 🌬️💧"
    },
    ("Earth (Heterotic SO(32))", "Ether (Heterotic E8×E8)"): {
        "resonance": "Deep", "harmony": "Foundational Unity ✨🌍", 
        "description": "Ether pervades earth in timeless unity! Connected via M-theory's hidden dimensions. For profound, grounded harmonies! 🌌",
        "base_score": 95,
        "big_bang_analogy": "Unified higher-dimensional state before the Big Bang, where all elements converge in M-theory! ✨🌍"
    },
    # Same element cases
    ("Fire (Type I)", "Fire (Type I)"): {
        "resonance": "Explosive", "harmony": "Blazing Sync 🔥🔥", 
        "description": "Twin flames ignite the cosmos! Perfect vibrational match in Type I strings. Super dynamic duo! 💥",
        "base_score": 100,
        "big_bang_analogy": "Pure singularity point where identical elements converge in infinite density, birthing explosive creation! 🔥🔥💥"
    },
    ("Water (Type IIA)", "Water (Type IIA)"): {
        "resonance": "Flowing", "harmony": "Oceanic Merge 💧💧", 
        "description": "Waves in harmony! Cohesive fluidity doubles via IIA dualities. Deep emotional bonds! 🌊",
        "base_score": 85,
        "big_bang_analogy": "Fluid convergence at the origin, flowing into the expanding universe without singularity issues! 💧💧🌊"
    },
    ("Air (Type IIB)", "Air (Type IIB)"): {
        "resonance": "Whirling", "harmony": "Breezy Freedom 🌬️🌬️", 
        "description": "Winds dancing together! Self-dual expansions in IIB. Free-spirited adventures await! 🌀",
        "base_score": 80,
        "big_bang_analogy": "Whirling gases in pre-Big Bang cosmology, expanding freely from a symmetric state! 🌬️🌬️🌀"
    },
    ("Earth (Heterotic SO(32))", "Earth (Heterotic SO(32))"): {
        "resonance": "Solid", "harmony": "Rock Steady 🌍🌍", 
        "description": "Unshakeable foundations! Hybrid stability in SO(32). Reliable partners forever! 🏔️",
        "base_score": 90,
        "big_bang_analogy": "Solid core at the singularity, grounding the universe's formation in heterotic strings! 🌍🌍🏔️"
    },
    ("Ether (Heterotic E8×E8)", "Ether (Heterotic E8×E8)"): {
        "resonance": "Eternal", "harmony": "Cosmic Void ✨✨", 
        "description": "Infinite connectivity! Exceptional unity in E8×E8. Timeless soul links! 🌌",
        "base_score": 100,
        "big_bang_analogy": "Eternal void before time, where all converges in exceptional symmetry – the true origin! ✨✨🌌"
    },
    # New connections for missing pairs
    ("Fire (Type I)", "Water (Type IIA)"): {
        "resonance": "Low", "harmony": "Steamy Tension 🔥💧", 
        "description": "Fire boils water into steam power! Opposites clash and create in Type I and IIA interactions. Volatile but innovative vibes! 🌫️",
        "base_score": 50,
        "big_bang_analogy": "Clashing elements at the hot dense phase, evaporating into cosmic steam – a tense birth! 🔥💧🌫️"
    },
    ("Water (Type IIA)", "Fire (Type I)"): {
        "resonance": "Low", "harmony": "Steamy Tension 🔥💧", 
        "description": "Fire boils water into steam power! Opposites clash and create in Type I and IIA interactions. Volatile but innovative vibes! 🌫️",
        "base_score": 50,
        "big_bang_analogy": "Clashing elements at the hot dense phase, evaporating into cosmic steam – a tense birth! 🔥💧🌫️"
    },
    ("Fire (Type I)", "Ether (Heterotic E8×E8)"): {
        "resonance": "High", "harmony": "Ethereal Blaze 🔥✨", 
        "description": "Fire illuminates the void! Dynamic energy fills subtle space, unified in M-theory. Inspiring cosmic fireworks! 🎆",
        "base_score": 90,
        "big_bang_analogy": "Energy bursting into the void, like string theory's pre-Big Bang illumination! 🔥✨🎆"
    },
    ("Ether (Heterotic E8×E8)", "Fire (Type I)"): {
        "resonance": "High", "harmony": "Ethereal Blaze 🔥✨", 
        "description": "Fire illuminates the void! Dynamic energy fills subtle space, unified in M-theory. Inspiring cosmic fireworks! 🎆",
        "base_score": 90,
        "big_bang_analogy": "Energy bursting into the void, like string theory's pre-Big Bang illumination! 🔥✨🎆"
    },
    ("Water (Type IIA)", "Earth (Heterotic SO(32))"): {
        "resonance": "Moderate", "harmony": "Fertile Blend 💧🌍", 
        "description": "Water nourishes earth for growth! Fluidity grounds in stability, like IIA branes on heterotic foundations. Nurturing partnerships! 🌱",
        "base_score": 70,
        "big_bang_analogy": "Nourishing flow in early universe, fertilizing stable matter from converged elements! 💧🌍🌱"
    },
    ("Earth (Heterotic SO(32))", "Water (Type IIA)"): {
        "resonance": "Moderate", "harmony": "Fertile Blend 💧🌍", 
        "description": "Water nourishes earth for growth! Fluidity grounds in stability, like IIA branes on heterotic foundations. Nurturing partnerships! 🌱",
        "base_score": 70,
        "big_bang_analogy": "Nourishing flow in early universe, fertilizing stable matter from converged elements! 💧🌍🌱"
    },
    ("Air (Type IIB)", "Earth (Heterotic SO(32))"): {
        "resonance": "Variable", "harmony": "Dusty Winds 🌬️🌍", 
        "description": "Air shapes earth through erosion and renewal! Mobility meets solidity in IIB-heterotic dualities. Adventurous and grounding! 🏜️",
        "base_score": 60,
        "big_bang_analogy": "Winds sculpting primordial dust, renewing from a singular converged state! 🌬️🌍🏜️"
    },
    ("Earth (Heterotic SO(32))", "Air (Type IIB)"): {
        "resonance": "Variable", "harmony": "Dusty Winds 🌬️🌍", 
        "description": "Air shapes earth through erosion and renewal! Mobility meets solidity in IIB-heterotic dualities. Adventurous and grounding! 🏜️",
        "base_score": 60,
        "big_bang_analogy": "Winds sculpting primordial dust, renewing from a singular converged state! 🌬️🌍🏜️"
    },
    ("Air (Type IIB)", "Ether (Heterotic E8×E8)"): {
        "resonance": "Deep", "harmony": "Boundless Breeze 🌬️✨", 
        "description": "Air expands into infinite ether! Lightness pervades space, connected via exceptional symmetries. Free and profound explorations! ☄️",
        "base_score": 95,
        "big_bang_analogy": "Expansion into boundless space from the singularity, driven by string symmetries! 🌬️✨☄️"
    },
    ("Ether (Heterotic E8×E8)", "Air (Type IIB)"): {
        "resonance": "Deep", "harmony": "Boundless Breeze 🌬️✨", 
        "description": "Air expands into infinite ether! Lightness pervades space, connected via exceptional symmetries. Free and profound explorations! ☄️",
        "base_score": 95,
        "big_bang_analogy": "Expansion into boundless space from the singularity, driven by string symmetries! 🌬️✨☄️"
    },
}

# Function to map datetime to element index (pseudo-scientific vibration calc)
def get_element_index(birth_dt):
    # Sum components for 'vibration'
    vibration = birth_dt.year + birth_dt.month + birth_dt.day + birth_dt.hour + birth_dt.minute + birth_dt.second
    # Modulo 5 for 5 elements
    return vibration % 5

# Streamlit app
st.title("💥 Big Bang Elemental Convergence: String Theory Soulmates! 🌌")

st.markdown("""
Welcome to the redesigned app where the Big Bang is the singularity of elemental convergence! 🎉  
Imagine all five elements uniting at a point of infinite possibility, birthing your unique harmony.  
Enter birth dates and times for two people to see how their elements converged from the cosmic origin! 🚀  
Inspired by string theory's views on the Big Bang as a transition from a pre-existing state.  
""")

# Define calendar range for all living humans (approx 1900 to current)
min_birth_date = datetime(1900, 1, 1)
max_birth_date = datetime(2025, 7, 11)  # Current date

# Input for Person 1
st.header("Person 1 👤")
date1 = st.date_input("Birth Date (Person 1)", value=datetime(2000, 1, 1), min_value=min_birth_date, max_value=max_birth_date)
time1 = st.time_input("Birth Time (Person 1)", value=datetime(2000, 1, 1, 12, 0, 0).time(), step=timedelta(minutes=1))
sec1 = st.slider("Birth Second (Person 1)", 0, 59, 0)
birth1 = datetime(date1.year, date1.month, date1.day, time1.hour, time1.minute, sec1)

# Input for Person 2
st.header("Person 2 👥")
date2 = st.date_input("Birth Date (Person 2)", value=datetime(2000, 1, 1), min_value=min_birth_date, max_value=max_birth_date)
time2 = st.time_input("Birth Time (Person 2)", value=datetime(2000, 1, 1, 12, 0, 0).time(), step=timedelta(minutes=1))
sec2 = st.slider("Birth Second (Person 2)", 0, 59, 0)
birth2 = datetime(date2.year, date2.month, date2.day, time2.hour, time2.minute, sec2)

if st.button("Converge Elements! 🔮💥"):
    if birth1 == birth2:
        st.warning("Birth times are identical! That's the ultimate singularity – pure convergence! Try different times for expansion! ⚠️")
    else:
        # Get elements
        idx1 = get_element_index(birth1)
        idx2 = get_element_index(birth2)
        elem1 = elements[idx1]
        elem2 = elements[idx2]
        
        # Time difference for enhanced 'time_factor'
        delta = abs(birth1 - birth2)
        total_seconds = int(delta.total_seconds())
        time_factor = (total_seconds % 101)  # 0-100 for finer granularity
        
        # Get connection
        key = (elem1['name'], elem2['name'])
        conn = connections[key]
        
        # Enhanced compatibility score: base from pair + modulated by time_factor
        compatibility_score = conn['base_score'] + (time_factor - 50) // 5  # Varies +/-10 around base
        
        # Clamp to 0-100
        compatibility_score = max(0, min(100, compatibility_score))
        
        st.header("Your Elemental Mappings 🌟")
        st.markdown(f"**Person 1:** {elem1['name']} {elem1['emoji']} - {elem1['qualities']}")
        st.markdown(f"**Person 2:** {elem2['name']} {elem2['emoji']} - {elem2['qualities']}")
        
        st.header("Spacetime Connection Analysis 🪐")
        st.markdown(f"**Resonance:** {conn['resonance']} {elem1['emoji']}{elem2['emoji']}")
        st.markdown(f"**Harmony:** {conn['harmony']}")
        st.markdown(f"**Description:** {conn['description']}")
        st.markdown(f"**Big Bang Analogy:** {conn['big_bang_analogy']}")
        st.markdown(f"**Convergence Score (String Cosmology Inspired):** {compatibility_score}% ❤️")
        
        # Fun animation
        with st.spinner("Elements converging at the singularity..."):
            time.sleep(1)
        st.balloons()
