import streamlit as st
import random

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="CR7 – La Leyenda",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS personalizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600;700&display=swap');

  /* Fondo oscuro con degradado dorado */
  .stApp {
    background: linear-gradient(160deg, #0a0a0a 0%, #1a1200 60%, #0a0a0a 100%);
    color: #e8d5a3;
    font-family: 'Inter', sans-serif;
  }

  /* Hero ─────────────────────────────────────────────── */
  .hero {
    text-align: center;
    padding: 3rem 1rem 1.5rem;
  }
  .hero h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3.5rem, 10vw, 7rem);
    letter-spacing: 0.08em;
    background: linear-gradient(90deg, #c8a84b, #ffe680, #c8a84b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1;
  }
  .hero .subtitle {
    font-size: 1.1rem;
    color: #a89060;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-top: 0.4rem;
  }
  .hero .number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(5rem, 18vw, 11rem);
    color: rgba(200,168,75,0.08);
    line-height: 0.85;
    display: block;
    margin-top: -0.5rem;
  }

  /* Divider */
  .gold-line {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c8a84b, transparent);
    margin: 1.5rem auto;
    width: 70%;
  }

  /* Stat cards */
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
  }
  .stat-card {
    background: rgba(200,168,75,0.07);
    border: 1px solid rgba(200,168,75,0.25);
    border-radius: 8px;
    padding: 1.2rem 1rem;
    text-align: center;
    transition: transform 0.2s, border-color 0.2s;
  }
  .stat-card:hover {
    transform: translateY(-4px);
    border-color: #c8a84b;
  }
  .stat-card .num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.6rem;
    color: #ffe680;
    line-height: 1;
  }
  .stat-card .lbl {
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #a89060;
    margin-top: 0.3rem;
  }

  /* Quote box */
  .quote-box {
    background: rgba(200,168,75,0.06);
    border-left: 4px solid #c8a84b;
    border-radius: 0 8px 8px 0;
    padding: 1.4rem 1.8rem;
    margin: 1.2rem 0;
    font-size: 1.15rem;
    font-style: italic;
    color: #e8d5a3;
    line-height: 1.7;
  }

  /* Section headers */
  .section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: 0.12em;
    color: #c8a84b;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
  }

  /* Achievement items */
  .ach-item {
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(200,168,75,0.12);
  }
  .ach-icon {
    font-size: 1.4rem;
    flex-shrink: 0;
    margin-top: 0.1rem;
  }
  .ach-text strong {
    color: #ffe680;
    font-size: 0.95rem;
  }
  .ach-text span {
    display: block;
    font-size: 0.82rem;
    color: #a89060;
    margin-top: 0.15rem;
  }

  /* Imagen CR7 */
  .cr7-photo-wrap {
    text-align: center;
    margin: 1.5rem 0;
  }
  .cr7-photo-wrap img {
    border-radius: 12px;
    border: 3px solid rgba(200,168,75,0.4);
    max-width: 100%;
    box-shadow: 0 8px 40px rgba(200,168,75,0.15);
  }
  .cr7-photo-caption {
    font-size: 0.78rem;
    color: #a89060;
    margin-top: 0.5rem;
    letter-spacing: 0.1em;
  }

  /* Video banner */
  .video-banner {
    background: linear-gradient(135deg, rgba(200,168,75,0.12), rgba(200,168,75,0.04));
    border: 1px solid rgba(200,168,75,0.35);
    border-radius: 12px;
    padding: 2rem 1.5rem;
    text-align: center;
    margin: 2rem 0 1rem;
  }
  .video-banner h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #ffe680;
    letter-spacing: 0.12em;
    margin: 0 0 0.5rem;
  }
  .video-banner p {
    color: #a89060;
    font-size: 0.9rem;
    margin-bottom: 1.2rem;
  }
  .video-btn {
    display: inline-block;
    background: linear-gradient(90deg, #c8a84b, #ffe680);
    color: #0a0a0a !important;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.2rem;
    letter-spacing: 0.15em;
    padding: 0.7rem 2.2rem;
    border-radius: 6px;
    text-decoration: none !important;
    transition: opacity 0.2s, transform 0.2s;
  }
  .video-btn:hover {
    opacity: 0.85;
    transform: scale(1.04);
    text-decoration: none !important;
  }

  /* Footer */
  .cr7-footer {
    text-align: center;
    padding: 2.5rem 1rem 1rem;
    font-size: 0.78rem;
    color: #5a4a20;
    letter-spacing: 0.1em;
  }

  /* Hide Streamlit branding */
  #MainMenu, footer { visibility: hidden; }
  .block-container { padding-top: 0; max-width: 960px; }
</style>
""", unsafe_allow_html=True)

# ── Datos ─────────────────────────────────────────────────────────────────────
QUOTES = [
    ("Tus limitaciones solo existen en tu mente.", "Entrevista, 2012"),
    ("El talento sin trabajo no es nada.", "CR7 – Autobiografía"),
    ("No me compares con Messi. No me gusta que me comparen con nadie.", "France Football, 2015"),
    ("Si crees en ti mismo, nada te detiene.", "Nike Campaign, 2018"),
    ("Soy el mejor jugador de la historia. Lo creo de verdad.", "Marca, 2017"),
    ("La presión es un privilegio — solo se la dan a los mejores.", "UEFA Gala, 2019"),
    ("Quiero ser el mejor hasta mi último día.", "DAZN Interview, 2022"),
    ("No es arrogancia cuando puedes respaldarlo.", "The Sun, 2013"),
    ("El trabajo duro supera al talento cuando el talento no trabaja duro.", "Training Camp, 2014"),
    ("Lloré cuando gané la Eurocopa. No me avergüenza.", "Portugal FC, 2016"),
]

ACHIEVEMENTS = [
    ("🏆", "5× Balón de Oro", "2008, 2013, 2014, 2016, 2017"),
    ("🥇", "5× UEFA Champions League", "Man Utd 2008 · Real Madrid 2014, 16, 17, 18"),
    ("🌍", "5× Liga de campeones nacionales", "Premier, La Liga ×2, Serie A ×2, Saudi Pro"),
    ("🇵🇹", "UEFA Euro 2016", "Primer título internacional con Portugal"),
    ("🌐", "UEFA Nations League 2019", "Segunda conquista con la selección"),
    ("👑", "Máximo goleador histórico FIFA", "900+ goles oficiales en carrera"),
    ("⚽", "Máximo goleador Champions League", "141 goles, récord absoluto"),
    ("🎯", "Máximo goleador selecciones masculinas", "130+ goles con Portugal"),
    ("🏅", "4× Bota de Oro europea", "2008, 2011, 2014, 2015"),
    ("🌟", "FIFA Best Player", "2016, 2017"),
    ("📈", "Primer jugador en marcar en 5 Mundiales", "2006 → 2022"),
    ("💰", "Primer deportista en superar €1,000M de ingresos", "Forbes, 2023"),
]

STATS = [
    ("900+", "Goles oficiales"),
    ("130+", "Goles con Portugal"),
    ("141", "Goles en Champions"),
    ("5", "Balones de Oro"),
    ("5", "Champions League"),
    ("22", "Trofeos colectivos"),
]

# ── Render ────────────────────────────────────────────────────────────────────

# Hero
st.markdown("""
<div class="hero">
  <span class="number">CR7</span>
  <h1>CRISTIANO RONALDO</h1>
  <p class="subtitle">El mejor de todos los tiempos &nbsp;·&nbsp; Siuu</p>
</div>
<hr class="gold-line">
""", unsafe_allow_html=True)

# Imagen de CR7 — st.image es más confiable en Streamlit que HTML img
col_img_l, col_img_c, col_img_r = st.columns([1, 2, 1])
with col_img_c:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Cristiano_Ronaldo_playing_for_Al_Nassr_FC_against_Persepolis%2C_September_2023_crop.jpg/800px-Cristiano_Ronaldo_playing_for_Al_Nassr_FC_against_Persepolis%2C_September_2023_crop.jpg",
        caption="Cristiano Ronaldo · Al-Nassr · #7",
        use_container_width=True,
    )

# Stats row
cols_stats = "".join(
    f'<div class="stat-card"><div class="num">{n}</div><div class="lbl">{l}</div></div>'
    for n, l in STATS
)
st.markdown(f'<div class="stat-grid">{cols_stats}</div>', unsafe_allow_html=True)
st.markdown('<hr class="gold-line">', unsafe_allow_html=True)

# ── Dos columnas: Frases | Logros ─────────────────────────────────────────────
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="section-title">💬 Frases Memorables</div>', unsafe_allow_html=True)

    # Frase aleatoria con botón
    if "quote_idx" not in st.session_state:
        st.session_state.quote_idx = 0

    q, src = QUOTES[st.session_state.quote_idx]
    st.markdown(f'<div class="quote-box">"{q}"<br><small style="color:#a89060;font-style:normal;">— {src}</small></div>',
                unsafe_allow_html=True)

    if st.button("🎲 Nueva frase", use_container_width=True):
        st.session_state.quote_idx = random.randint(0, len(QUOTES) - 1)
        st.rerun()

    st.markdown('<hr class="gold-line">', unsafe_allow_html=True)
    st.markdown('<div class="section-title" style="font-size:1.3rem;">Todas las frases</div>',
                unsafe_allow_html=True)
    for quote, source in QUOTES:
        st.markdown(
            f'<div class="quote-box" style="font-size:0.9rem;padding:0.9rem 1.2rem;">'
            f'"{quote}"<br><small style="color:#a89060;font-style:normal;">— {source}</small></div>',
            unsafe_allow_html=True,
        )

with col2:
    st.markdown('<div class="section-title">🏆 Palmarés & Logros</div>', unsafe_allow_html=True)

    for icon, title, detail in ACHIEVEMENTS:
        st.markdown(
            f'<div class="ach-item">'
            f'<div class="ach-icon">{icon}</div>'
            f'<div class="ach-text"><strong>{title}</strong><span>{detail}</span></div>'
            f'</div>',
            unsafe_allow_html=True,
        )

# ── Sección de video ──────────────────────────────────────────────────────────
st.markdown("""
<hr class="gold-line">
<div class="video-banner">
  <h2>🎬 VER LOS MEJORES CLIPS DE CR7</h2>
  <p>Goles imposibles, regates imposibles, momentos que quedaron en la historia del fútbol</p>
  <a class="video-btn"
     href="https://www.youtube.com/watch?v=mmeLCAP74KA"
     target="_blank"
     rel="noopener noreferrer">
    ▶ &nbsp; VER VIDEO EN YOUTUBE
  </a>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr class="gold-line">
<div class="cr7-footer">
  ⚽ &nbsp; CR7 · Madeira, 1985 &nbsp;·&nbsp; SIUUU &nbsp;·&nbsp; Hecho con Python & Streamlit
</div>
""", unsafe_allow_html=True)

