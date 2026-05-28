import streamlit as st
import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CloudAI Pulse | AI & Cloud Technology Blog",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Fira+Code:wght@300;400;500&family=Lora:ital,wght@0,400;0,500;1,400&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #030712 !important;
    color: #e2e8f0 !important;
    font-family: 'Lora', Georgia, serif;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(14,165,233,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 90% 50%, rgba(99,102,241,0.08) 0%, transparent 50%),
        #030712 !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c1220 0%, #060d18 100%) !important;
    border-right: 1px solid rgba(14,165,233,0.15) !important;
}

[data-testid="stSidebar"] * { color: #cbd5e1 !important; }

[data-testid="stSidebar"] .stTextInput input {
    background: rgba(14,165,233,0.08) !important;
    border: 1px solid rgba(14,165,233,0.25) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 0.85rem !important;
}

[data-testid="stSidebar"] .stTextInput input:focus {
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 0 2px rgba(14,165,233,0.2) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

/* ── Top Padding ── */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px !important;
}

/* ── Masthead ── */
.masthead {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(14,165,233,0.18);
}

.masthead-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.masthead-tagline {
    font-family: 'Fira Code', monospace;
    font-size: 0.72rem;
    color: #64748b;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    border-left: 2px solid rgba(14,165,233,0.3);
    padding-left: 14px;
}

/* ── Featured badge ── */
.featured-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(14,165,233,0.15), rgba(99,102,241,0.15));
    border: 1px solid rgba(14,165,233,0.3);
    color: #38bdf8;
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 1.2rem;
}

/* ── Hero Blog Card ── */
.hero-card {
    background: linear-gradient(135deg,
        rgba(14,165,233,0.06) 0%,
        rgba(99,102,241,0.06) 50%,
        rgba(6,182,212,0.04) 100%);
    border: 1px solid rgba(14,165,233,0.2);
    border-radius: 16px;
    padding: 2.5rem 2.8rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}

.hero-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #0ea5e9, #6366f1, #06b6d4);
    border-radius: 16px 16px 0 0;
}

.hero-card::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(99,102,241,0.06) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.1rem;
    font-weight: 800;
    line-height: 1.2;
    color: #f1f5f9;
    margin-bottom: 1rem;
    letter-spacing: -0.5px;
}

.hero-meta {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1.2rem;
    flex-wrap: wrap;
}

.hero-meta-item {
    font-family: 'Fira Code', monospace;
    font-size: 0.75rem;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 5px;
}

.hero-meta-item span { color: #94a3b8; }

.hero-excerpt {
    font-size: 1.05rem;
    color: #94a3b8;
    line-height: 1.75;
    font-style: italic;
}

/* ── Tag pills ── */
.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 1.2rem 0;
}

.tag {
    background: rgba(14,165,233,0.1);
    border: 1px solid rgba(14,165,233,0.2);
    color: #38bdf8;
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 4px;
    letter-spacing: 0.05em;
}

/* ── Section headings ── */
.section-heading {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #f1f5f9;
    margin: 2.2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(14,165,233,0.15);
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-heading .accent { color: #38bdf8; }

/* ── Info cards (What is X) ── */
.info-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(14,165,233,0.12);
    border-left: 3px solid #0ea5e9;
    border-radius: 0 12px 12px 0;
    padding: 1.5rem 1.8rem;
    margin: 1rem 0;
}

.info-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 0.6rem;
}

.info-card p {
    color: #94a3b8;
    font-size: 0.95rem;
    line-height: 1.7;
}

/* ── Step cards ── */
.step-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1rem;
    margin: 1rem 0 1.5rem;
}

.step-card {
    background: rgba(14,165,233,0.04);
    border: 1px solid rgba(14,165,233,0.12);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    position: relative;
}

.step-number {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: rgba(14,165,233,0.18);
    line-height: 1;
    margin-bottom: 0.4rem;
}

.step-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #cbd5e1;
    margin-bottom: 0.35rem;
}

.step-desc {
    font-size: 0.82rem;
    color: #64748b;
    line-height: 1.5;
}

/* ── Code block wrapper ── */
.code-wrapper {
    background: #0a0f1a;
    border: 1px solid rgba(14,165,233,0.18);
    border-radius: 10px;
    margin: 1rem 0 1.5rem;
    overflow: hidden;
}

.code-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.55rem 1rem;
    background: rgba(14,165,233,0.07);
    border-bottom: 1px solid rgba(14,165,233,0.12);
}

.code-lang {
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    color: #38bdf8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.code-dots { display: flex; gap: 5px; }
.code-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
}
.dot-red   { background: #ef4444; }
.dot-yellow{ background: #f59e0b; }
.dot-green { background: #22c55e; }

/* ── Use-case chips ── */
.usecase-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 0.8rem;
    margin: 1rem 0;
}

.usecase-chip {
    background: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(14,165,233,0.06));
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 10px;
    padding: 1rem 1.2rem;
}

.usecase-chip-icon {
    font-size: 1.5rem;
    margin-bottom: 0.4rem;
    display: block;
}

.usecase-chip-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: #c7d2fe;
    margin-bottom: 0.2rem;
}

.usecase-chip-desc {
    font-size: 0.78rem;
    color: #64748b;
    line-height: 1.45;
}

/* ── FAQ ── */
.faq-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(14,165,233,0.1);
    border-radius: 10px;
    margin-bottom: 0.75rem;
    overflow: hidden;
}

.faq-q {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #cbd5e1;
    padding: 1rem 1.2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
}

.faq-a {
    color: #94a3b8;
    font-size: 0.88rem;
    line-height: 1.7;
    padding: 0 1.2rem 1rem;
    border-top: 1px solid rgba(14,165,233,0.08);
}

/* ── Sidebar nav items ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 9px;
    padding: 8px 12px;
    border-radius: 8px;
    cursor: pointer;
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    color: #94a3b8;
    margin-bottom: 4px;
    transition: all 0.2s;
    border: 1px solid transparent;
    text-decoration: none;
}

.nav-item:hover, .nav-item.active {
    background: rgba(14,165,233,0.1);
    border-color: rgba(14,165,233,0.2);
    color: #38bdf8;
}

/* ── Sidebar widget ── */
.sidebar-widget {
    background: rgba(14,165,233,0.04);
    border: 1px solid rgba(14,165,233,0.12);
    border-radius: 10px;
    padding: 1rem;
    margin-top: 1.2rem;
}

.sidebar-widget-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgba(14,165,233,0.15);
}

.sidebar-tech-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 5px 0;
    font-size: 0.8rem;
    color: #94a3b8;
    font-family: 'Lora', serif;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}

.sidebar-tech-item:last-child { border-bottom: none; }
.sidebar-tech-icon { font-size: 0.95rem; }

/* ── Stats bar ── */
.stats-bar {
    display: flex;
    gap: 2rem;
    padding: 1rem 0;
    margin: 1.5rem 0;
    border-top: 1px solid rgba(14,165,233,0.1);
    border-bottom: 1px solid rgba(14,165,233,0.1);
    flex-wrap: wrap;
}

.stat-item {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 800;
    color: #38bdf8;
}

.stat-label {
    font-family: 'Fira Code', monospace;
    font-size: 0.68rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── Callout box ── */
.callout {
    background: rgba(14,165,233,0.06);
    border: 1px solid rgba(14,165,233,0.2);
    border-radius: 10px;
    padding: 1rem 1.3rem;
    margin: 1rem 0;
    font-size: 0.88rem;
    color: #94a3b8;
    line-height: 1.65;
}

.callout-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.82rem;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

/* ── Footer ── */
.footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(14,165,233,0.1);
    text-align: center;
    font-family: 'Fira Code', monospace;
    font-size: 0.72rem;
    color: #334155;
    line-height: 1.8;
}

/* ── Streamlit override: remove extra padding from columns ── */
[data-testid="column"] { padding: 0 !important; }

/* ── Streamlit expander style ── */
.streamlit-expanderHeader {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    color: #cbd5e1 !important;
    background: rgba(14,165,233,0.04) !important;
    border: 1px solid rgba(14,165,233,0.12) !important;
    border-radius: 8px !important;
}

.streamlit-expanderContent {
    background: rgba(255,255,255,0.01) !important;
    border: 1px solid rgba(14,165,233,0.1) !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
    color: #94a3b8 !important;
    font-size: 0.9rem !important;
    line-height: 1.7 !important;
}

/* ── Scroll-to-top hint ── */
.scroll-hint {
    font-family: 'Fira Code', monospace;
    font-size: 0.72rem;
    color: #334155;
    text-align: center;
    margin-top: 1rem;
}

/* ── No-result box ── */
.no-result {
    text-align: center;
    padding: 3rem 1rem;
    color: #475569;
    font-family: 'Fira Code', monospace;
    font-size: 0.85rem;
}
.no-result-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# ── Blog Data ─────────────────────────────────────────────────────────────────
BLOGS = [
    {
        "id": "bedrock-agentcore",
        "title": "Build an AI Agent using Claude Sonnet 4.6 with Amazon Bedrock AgentCore",
        "author": "CloudAI Pulse Editorial",
        "date": "May 28, 2026",
        "read_time": "18 min read",
        "tags": ["Claude Sonnet 4.6", "Amazon Bedrock", "AgentCore", "AI Agents", "AWS", "Python"],
        "category": "Deep Dive",
        "excerpt": (
            "Explore how Anthropic's Claude Sonnet 4.6 and Amazon Bedrock AgentCore combine "
            "to deliver production-grade AI agents — from zero-shot planning to multi-step tool "
            "orchestration — all without managing infrastructure."
        ),
        "featured": True,
    },
]

# ── Helper ────────────────────────────────────────────────────────────────────
def code_block(lang: str, filename: str, code: str):
    st.markdown(f"""
    <div class="code-wrapper">
        <div class="code-header">
            <span class="code-lang">{lang} · {filename}</span>
            <div class="code-dots">
                <div class="code-dot dot-red"></div>
                <div class="code-dot dot-yellow"></div>
                <div class="code-dot dot-green"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.code(code, language=lang.lower())

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0 0.5rem;">
        <div class="masthead-logo" style="font-size:1.3rem;">⚡ CloudAI Pulse</div>
        <div class="masthead-tagline" style="border:none; padding:0; margin-top:4px; font-size:0.65rem;">
            Where Cloud Meets Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    search_query = st.text_input("🔍  Search articles…", placeholder="e.g. Bedrock, Claude, agents")

    st.markdown("""
    <div style="margin-top: 1.2rem;">
        <div class="sidebar-widget-title" style="font-family:'Syne',sans-serif; font-size:0.7rem;
             font-weight:700; color:#38bdf8; letter-spacing:.1em; text-transform:uppercase;
             margin-bottom:.8rem;">Navigation</div>
    </div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("🏠", "Home"),
        ("📰", "Featured"),
        ("☁️", "Cloud AI"),
        ("🤖", "AI Agents"),
        ("🔧", "Tutorials"),
        ("📚", "Resources"),
    ]

    if "nav" not in st.session_state:
        st.session_state.nav = "Home"

    for icon, label in nav_items:
        if st.button(f"{icon}  {label}", key=f"nav_{label}", use_container_width=True):
            st.session_state.nav = label

    st.markdown("""
    <div class="sidebar-widget" style="margin-top:1.5rem;">
        <div class="sidebar-widget-title">Tech Stack</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">🔶</span> AWS Bedrock</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">🧠</span> Claude Sonnet 4.6</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">🐍</span> Python 3.12+</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">⚡</span> Streamlit</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">🔗</span> LangChain</div>
        <div class="sidebar-tech-item"><span class="sidebar-tech-icon">🗂️</span> boto3</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-widget" style="margin-top:1rem;">
        <div class="sidebar-widget-title">About</div>
        <div style="font-size:0.78rem; color:#64748b; line-height:1.6; font-family:'Lora',serif;">
            CloudAI Pulse covers the intersection of cloud computing and AI — tutorials,
            deep dives, and real-world architecture for builders.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="font-family:'Fira Code',monospace; font-size:0.65rem; color:#334155;
         text-align:center; margin-top:2rem; padding-top:1rem;
         border-top:1px solid rgba(14,165,233,0.1);">
        © {datetime.datetime.now().year} CloudAI Pulse<br>
        All rights reserved
    </div>
    """, unsafe_allow_html=True)

# ── Main content ──────────────────────────────────────────────────────────────

# ── Masthead ──
st.markdown("""
<div class="masthead">
    <div>
        <div class="masthead-logo">⚡ CloudAI Pulse</div>
    </div>
    <div class="masthead-tagline">Enterprise Cloud &amp; AI Technology · Deep Dives · Tutorials · Architecture</div>
</div>
""", unsafe_allow_html=True)

# ── Search filter ──
active_blogs = BLOGS
if search_query:
    q = search_query.lower()
    active_blogs = [
        b for b in BLOGS
        if q in b["title"].lower()
        or q in b["excerpt"].lower()
        or any(q in t.lower() for t in b["tags"])
        or q in b["category"].lower()
    ]

# ── No results ──
if not active_blogs:
    st.markdown(f"""
    <div class="no-result">
        <div class="no-result-icon">🔭</div>
        No articles found for <strong style="color:#38bdf8;">"{search_query}"</strong><br>
        Try searching for: Claude, Bedrock, AgentCore, Python
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ════════════════════════════════════════════════════════════════════════════════
# FEATURED BLOG
# ════════════════════════════════════════════════════════════════════════════════
blog = active_blogs[0]

# ── Hero card ──
tags_html = "".join(f'<span class="tag">{t}</span>' for t in blog["tags"])
st.markdown(f"""
<div class="featured-badge">⭐ Featured Article</div>
<div class="hero-card">
    <div class="hero-title">{blog["title"]}</div>
    <div class="hero-meta">
        <div class="hero-meta-item">✍️ <span>{blog["author"]}</span></div>
        <div class="hero-meta-item">📅 <span>{blog["date"]}</span></div>
        <div class="hero-meta-item">⏱️ <span>{blog["read_time"]}</span></div>
        <div class="hero-meta-item">📂 <span>{blog["category"]}</span></div>
    </div>
    <div class="tag-row">{tags_html}</div>
    <div class="hero-excerpt">{blog["excerpt"]}</div>
</div>
""", unsafe_allow_html=True)

# ── Stats bar ──
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-value">4.6</div>
        <div class="stat-label">Claude Version</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">200K</div>
        <div class="stat-label">Context Window</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">3</div>
        <div class="stat-label">Code Examples</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">6</div>
        <div class="stat-label">Use Cases</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">5</div>
        <div class="stat-label">Setup Steps</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 1 — What is Claude Sonnet 4.6
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">01</span> What is Claude Sonnet 4.6?
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <div class="info-card-title">🧠 Claude Sonnet 4.6 — Anthropic's Production Powerhouse</div>
    <p>
        Claude Sonnet 4.6 is Anthropic's flagship mid-tier language model in the Claude 4.x family,
        engineered for enterprise workloads that demand both intelligence and speed. It sits between
        the ultra-capable Claude Opus and the lightweight Claude Haiku — delivering a best-in-class
        balance of reasoning depth, output quality, and inference latency.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="info-card" style="border-left-color:#6366f1;">
        <div class="info-card-title" style="color:#818cf8;">🔑 Key Capabilities</div>
        <p>
            ✦ <strong style="color:#cbd5e1;">200K token context window</strong> — process entire codebases,
            legal documents, or research papers in a single call.<br><br>
            ✦ <strong style="color:#cbd5e1;">Extended thinking</strong> — multi-step chain-of-thought reasoning
            for complex problem-solving.<br><br>
            ✦ <strong style="color:#cbd5e1;">Tool use &amp; function calling</strong> — natively orchestrate
            APIs, databases, and external services.<br><br>
            ✦ <strong style="color:#cbd5e1;">Vision &amp; multimodal</strong> — analyze images, charts,
            and documents alongside text.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="border-left-color:#06b6d4;">
        <div class="info-card-title" style="color:#22d3ee;">📊 Model Specs</div>
        <p>
            ✦ <strong style="color:#cbd5e1;">Model ID:</strong> claude-sonnet-4-6<br><br>
            ✦ <strong style="color:#cbd5e1;">Input:</strong> Text, images, PDFs, documents<br><br>
            ✦ <strong style="color:#cbd5e1;">Output:</strong> Up to 64K tokens per response<br><br>
            ✦ <strong style="color:#cbd5e1;">Latency:</strong> Optimised for near-real-time
            agentic loops<br><br>
            ✦ <strong style="color:#cbd5e1;">Safety:</strong> Built-in Constitutional AI alignment
            and enterprise guardrails.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="callout">
    <div class="callout-title">💡 Why Sonnet 4.6 for agents?</div>
    Claude Sonnet 4.6 is purpose-built for agentic use cases: it understands ambiguous instructions,
    decomposes multi-step goals, recovers gracefully from tool errors, and produces structured outputs
    (JSON, XML, Markdown) that downstream systems can parse reliably — making it the go-to choice for
    production AI agents deployed at scale.
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 2 — What is Amazon Bedrock AgentCore
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">02</span> What is Amazon Bedrock AgentCore?
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <div class="info-card-title">🔶 Amazon Bedrock AgentCore — Managed Agent Runtime on AWS</div>
    <p>
        Amazon Bedrock AgentCore is AWS's fully managed runtime for deploying, scaling, and monitoring
        AI agents in production. It abstracts away the undifferentiated heavy lifting of agent
        infrastructure — session management, memory persistence, tool orchestration, observability,
        and multi-agent coordination — so engineers can focus on building agent logic rather than
        plumbing.
    </p>
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="medium")
with col3:
    st.markdown("""
    <div class="info-card" style="border-left-color:#f59e0b;">
        <div class="info-card-title" style="color:#fbbf24;">⚙️ Core Components</div>
        <p>
            ✦ <strong style="color:#cbd5e1;">Agent Runtime</strong> — serverless execution
            environment with automatic scaling.<br><br>
            ✦ <strong style="color:#cbd5e1;">Memory Store</strong> — long-term and short-term
            agent memory backed by DynamoDB or OpenSearch.<br><br>
            ✦ <strong style="color:#cbd5e1;">Action Groups</strong> — connect agents to Lambda
            functions, APIs, and S3 data sources.<br><br>
            ✦ <strong style="color:#cbd5e1;">Knowledge Bases</strong> — RAG integration with
            vector stores for grounded responses.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card" style="border-left-color:#22c55e;">
        <div class="info-card-title" style="color:#4ade80;">🔒 Enterprise Features</div>
        <p>
            ✦ <strong style="color:#cbd5e1;">IAM integration</strong> — fine-grained permissions
            per agent and action.<br><br>
            ✦ <strong style="color:#cbd5e1;">CloudWatch observability</strong> — traces, logs,
            and metrics for every agent invocation.<br><br>
            ✦ <strong style="color:#cbd5e1;">VPC support</strong> — run agents inside your
            private network for data sovereignty.<br><br>
            ✦ <strong style="color:#cbd5e1;">Multi-agent orchestration</strong> — supervisor
            and sub-agent patterns out of the box.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 3 — AWS Setup Steps
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">03</span> AWS Setup Steps
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-grid">
    <div class="step-card">
        <div class="step-number">01</div>
        <div class="step-title">Enable Bedrock Access</div>
        <div class="step-desc">Go to AWS Console → Amazon Bedrock → Model Access. Enable Claude Sonnet 4.6 for your region (us-east-1 recommended).</div>
    </div>
    <div class="step-card">
        <div class="step-number">02</div>
        <div class="step-title">Create IAM Role</div>
        <div class="step-desc">Create a role with AmazonBedrockFullAccess + AWSLambdaBasicExecutionRole. Attach it to your agent and Lambda functions.</div>
    </div>
    <div class="step-card">
        <div class="step-number">03</div>
        <div class="step-title">Configure AgentCore</div>
        <div class="step-desc">In Bedrock console, create an Agent. Select claude-sonnet-4-6 as the model. Write your system prompt defining the agent's persona.</div>
    </div>
    <div class="step-card">
        <div class="step-number">04</div>
        <div class="step-title">Add Action Groups</div>
        <div class="step-desc">Define OpenAPI schemas for your tools. Link each action to a Lambda function that executes the real logic.</div>
    </div>
    <div class="step-card">
        <div class="step-number">05</div>
        <div class="step-title">Deploy & Test</div>
        <div class="step-desc">Prepare a draft alias, then create a production alias. Test with the console playground before integrating with your application.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Install deps code ──
st.markdown("""
<div class="section-heading" style="font-size:1.1rem; margin-top:1.5rem;">
    <span class="accent">→</span> Install Dependencies
</div>
""", unsafe_allow_html=True)

code_block("bash", "terminal", """\
# Create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Linux/macOS
# python -m venv .venv && .venv\\Scripts\\activate   # Windows

# Install required packages
pip install boto3 anthropic streamlit python-dotenv

# Configure AWS credentials
aws configure
# AWS Access Key ID:     <your-key>
# AWS Secret Access Key: <your-secret>
# Default region name:   us-east-1
# Default output format: json
""")

# ── .env setup ──
code_block("bash", ".env", """\
AWS_REGION=us-east-1
BEDROCK_AGENT_ID=XXXXXXXXXX
BEDROCK_AGENT_ALIAS_ID=TSTALIASID
""")

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 4 — Example Python Code
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">04</span> Example Python Code
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">
    <div class="callout-title">📌 Three Approaches</div>
    The examples below cover: (1) calling Claude Sonnet 4.6 directly via Bedrock,
    (2) invoking a Bedrock Agent with session management, and (3) building a local
    tool-use agent loop with the Anthropic SDK.
</div>
""", unsafe_allow_html=True)

# Example 1
code_block("python", "bedrock_claude_direct.py", """\
import boto3
import json

def call_claude_sonnet(prompt: str, system: str = "") -> str:
    \"\"\"Invoke Claude Sonnet 4.6 directly via Amazon Bedrock.\"\"\"
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    messages = [{"role": "user", "content": prompt}]
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": messages,
    }
    if system:
        body["system"] = system

    response = client.invoke_model(
        modelId="us.anthropic.claude-sonnet-4-6-20250514-v1:0",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]


if __name__ == "__main__":
    answer = call_claude_sonnet(
        prompt="Explain Amazon Bedrock AgentCore in 3 bullet points.",
        system="You are a senior AWS solutions architect. Be concise and precise.",
    )
    print(answer)
""")

# Example 2
code_block("python", "bedrock_agent_invoke.py", """\
import boto3
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

def invoke_bedrock_agent(user_message: str, session_id: str | None = None) -> dict:
    \"\"\"Invoke a Bedrock Agent and return the response with metadata.\"\"\"
    client = boto3.client("bedrock-agent-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))

    agent_id       = os.getenv("BEDROCK_AGENT_ID")
    agent_alias_id = os.getenv("BEDROCK_AGENT_ALIAS_ID")
    session_id     = session_id or str(uuid.uuid4())

    response = client.invoke_agent(
        agentId=agent_id,
        agentAliasId=agent_alias_id,
        sessionId=session_id,
        inputText=user_message,
        enableTrace=True,   # capture reasoning steps
    )

    completion_text = ""
    traces = []

    for event in response["completion"]:
        if "chunk" in event:
            chunk = event["chunk"]
            completion_text += chunk["bytes"].decode("utf-8")
        if "trace" in event:
            trace = event["trace"].get("trace", {})
            if "orchestrationTrace" in trace:
                traces.append(trace["orchestrationTrace"])

    return {
        "response": completion_text,
        "session_id": session_id,
        "traces": traces,
    }


if __name__ == "__main__":
    session = str(uuid.uuid4())

    # Multi-turn conversation
    turns = [
        "What is my current AWS bill for this month?",
        "Which service is the most expensive?",
        "How can I reduce those costs?",
    ]

    for turn in turns:
        print(f"\\nUser: {turn}")
        result = invoke_bedrock_agent(turn, session_id=session)
        print(f"Agent: {result['response']}")
""")

# Example 3
code_block("python", "local_tool_agent.py", """\
import anthropic
import json
from datetime import datetime

# ── Tool definitions ──────────────────────────────────────────────────────────
tools = [
    {
        "name": "get_weather",
        "description": "Retrieve current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["city"],
        },
    },
    {
        "name": "query_database",
        "description": "Run a read-only SQL query on the company analytics DB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "sql": {"type": "string", "description": "SQL SELECT statement"},
            },
            "required": ["sql"],
        },
    },
]

def execute_tool(name: str, inputs: dict) -> str:
    \"\"\"Route tool calls to their implementations.\"\"\"
    if name == "get_weather":
        # Replace with a real weather API call
        return json.dumps({
            "city": inputs["city"],
            "temp": 22,
            "unit": inputs.get("unit", "celsius"),
            "condition": "Partly cloudy",
            "timestamp": datetime.utcnow().isoformat(),
        })
    elif name == "query_database":
        # Replace with a real DB connection
        return json.dumps({"rows": [], "query": inputs["sql"], "note": "mock result"})
    return json.dumps({"error": f"Unknown tool: {name}"})


def run_agent(user_request: str, max_iterations: int = 10) -> str:
    \"\"\"Agentic loop: Claude plans → calls tools → synthesises answer.\"\"\"
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": user_request}]

    system = (
        "You are an intelligent assistant with access to weather data and a company "
        "analytics database. Use tools when needed. Think step by step."
    )

    for iteration in range(max_iterations):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=system,
            tools=tools,
            messages=messages,
        )

        # Check stop reason
        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return "Agent completed without a text response."

        if response.stop_reason != "tool_use":
            break

        # Execute all tool calls in this response
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []

        for block in response.content:
            if block.type == "tool_use":
                print(f"  [tool] {block.name}({json.dumps(block.input, indent=2)})")
                output = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": output,
                })

        messages.append({"role": "user", "content": tool_results})

    return "Agent reached maximum iterations."


if __name__ == "__main__":
    answer = run_agent("What's the weather in Bengaluru and summarise last month's top 5 products by revenue?")
    print("\\nFinal Answer:\\n", answer)
""")

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 5 — Real-World Use Cases
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">05</span> Real-World Use Cases
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="usecase-grid">
    <div class="usecase-chip">
        <span class="usecase-chip-icon">💼</span>
        <div class="usecase-chip-title">Enterprise IT Helpdesk</div>
        <div class="usecase-chip-desc">Auto-resolve tier-1 tickets, escalate complex issues, and update ITSM systems — all without human intervention.</div>
    </div>
    <div class="usecase-chip">
        <span class="usecase-chip-icon">📊</span>
        <div class="usecase-chip-title">Business Intelligence Agent</div>
        <div class="usecase-chip-desc">Natural language to SQL, chart generation, and executive summaries from live data warehouses (Redshift, Athena).</div>
    </div>
    <div class="usecase-chip">
        <span class="usecase-chip-icon">⚖️</span>
        <div class="usecase-chip-title">Legal Document Review</div>
        <div class="usecase-chip-desc">Clause extraction, risk flagging, and contract comparison across thousands of pages using the 200K context window.</div>
    </div>
    <div class="usecase-chip">
        <span class="usecase-chip-icon">🛒</span>
        <div class="usecase-chip-title">E-commerce Assistant</div>
        <div class="usecase-chip-desc">Personalised product recommendations, order tracking, refund processing, and inventory queries — all conversational.</div>
    </div>
    <div class="usecase-chip">
        <span class="usecase-chip-icon">🏥</span>
        <div class="usecase-chip-title">Healthcare Triage</div>
        <div class="usecase-chip-desc">Symptom intake, appointment scheduling, and clinical-note pre-drafting — HIPAA-ready when deployed in a VPC.</div>
    </div>
    <div class="usecase-chip">
        <span class="usecase-chip-icon">🔐</span>
        <div class="usecase-chip-title">Security Operations</div>
        <div class="usecase-chip-desc">Alert triage, threat correlation across CloudWatch and GuardDuty, and automated runbook execution on confirmed incidents.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 6 — Architecture Diagram (ASCII-style)
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">06</span> Reference Architecture
</div>
""", unsafe_allow_html=True)

code_block("text", "architecture.txt", """\
┌─────────────────────────────────────────────────────────────────────────┐
│                       Your Application Layer                            │
│              (Streamlit / FastAPI / React / Mobile)                     │
└────────────────────────────┬────────────────────────────────────────────┘
                             │  HTTPS / WebSocket
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   Amazon Bedrock AgentCore                              │
│  ┌─────────────────────┐   ┌──────────────────────────────────────┐    │
│  │  Agent Runtime      │   │  Orchestration Engine                │    │
│  │  claude-sonnet-4-6  │◄──┤  • Tool selection & planning        │    │
│  │  (200K ctx window)  │   │  • Chain-of-thought reasoning        │    │
│  └─────────────────────┘   │  • Error recovery & retry logic      │    │
│                            └──────────────────────────────────────┘    │
│  ┌─────────────────────┐   ┌──────────────────────────────────────┐    │
│  │  Memory Store       │   │  Action Groups                       │    │
│  │  (DynamoDB /        │   │  • Lambda functions                  │    │
│  │   OpenSearch)       │   │  • API Gateway endpoints             │    │
│  └─────────────────────┘   │  • S3 data sources                   │    │
│                            └──────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Knowledge Bases  (Bedrock KB → OpenSearch Serverless / FAISS)  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         CloudWatch     AWS X-Ray      IAM / VPC
         (Logs &        (Distributed   (Security &
          Metrics)       Tracing)       Isolation)
""")

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 7 — FAQ
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">07</span> Frequently Asked Questions
</div>
""", unsafe_allow_html=True)

faqs = [
    (
        "What regions support Claude Sonnet 4.6 on Bedrock?",
        "Claude Sonnet 4.6 is available in us-east-1 (N. Virginia) and us-west-2 (Oregon) "
        "with cross-region inference profiles. Check the Bedrock console for the latest "
        "regional availability as AWS continues to expand."
    ),
    (
        "How is Bedrock AgentCore different from plain Bedrock model invocation?",
        "Direct Bedrock invocations are stateless single-turn API calls. AgentCore adds a full "
        "agentic runtime on top: persistent session memory, multi-step planning, automatic tool "
        "orchestration, built-in retry logic, and CloudWatch observability — removing weeks of "
        "undifferentiated infrastructure work."
    ),
    (
        "What does a Bedrock Agent cost?",
        "Pricing has two components: (1) the Claude Sonnet 4.6 token cost (input + output) and "
        "(2) AgentCore orchestration charges per invocation. There are no idle costs. Check the "
        "AWS Bedrock Pricing page for the latest rates, as they vary by region and model version."
    ),
    (
        "Can I bring my own tools / APIs to AgentCore?",
        "Yes. Action Groups let you define any API surface via an OpenAPI 3.0 schema. "
        "Each action maps to an AWS Lambda function that you control, giving full flexibility "
        "to integrate proprietary databases, SaaS platforms, or internal microservices."
    ),
    (
        "Is AgentCore production-ready for regulated industries?",
        "AWS has positioned Bedrock (including AgentCore) for regulated use cases. It supports "
        "VPC deployment, AWS PrivateLink, encryption at rest and in transit, CloudTrail audit "
        "logging, and IAM-based access control. For HIPAA or PCI workloads, review the AWS "
        "compliance documentation and enable the appropriate BAA."
    ),
    (
        "How do I handle multi-turn conversations and memory?",
        "Pass the same `sessionId` across API calls — AgentCore maintains session context "
        "automatically. For long-term memory across sessions, configure a Knowledge Base "
        "backed by OpenSearch Serverless and have your agent write/read memory records as "
        "part of its action group."
    ),
]

for q, a in faqs:
    with st.expander(f"❓  {q}"):
        st.markdown(f"""
        <div style="color:#94a3b8; font-size:0.9rem; line-height:1.75; font-family:'Lora',serif; padding: 0.3rem 0;">
            {a}
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════════
# SECTION 8 — Resources
# ════════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-heading">
    <span class="accent">08</span> Further Resources
</div>
""", unsafe_allow_html=True)

resources = [
    ("📖", "Anthropic Claude Sonnet 4.6 Docs", "https://docs.anthropic.com"),
    ("📖", "Amazon Bedrock Developer Guide",    "https://docs.aws.amazon.com/bedrock/latest/userguide/"),
    ("📖", "Bedrock AgentCore Documentation",   "https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html"),
    ("🐙", "Anthropic SDK (GitHub)",            "https://github.com/anthropics/anthropic-sdk-python"),
    ("💰", "Amazon Bedrock Pricing",            "https://aws.amazon.com/bedrock/pricing/"),
    ("🎓", "AWS AI/ML Blog",                    "https://aws.amazon.com/blogs/machine-learning/"),
]

cols = st.columns(3, gap="small")
for i, (icon, label, url) in enumerate(resources):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="info-card" style="border-left-color:#334155; padding: 1rem;">
            <div style="font-size:1.3rem; margin-bottom:0.4rem;">{icon}</div>
            <div style="font-family:'Syne',sans-serif; font-size:0.82rem; font-weight:700;
                 color:#94a3b8; margin-bottom:0.3rem;">{label}</div>
            <a href="{url}" target="_blank"
               style="font-family:'Fira Code',monospace; font-size:0.68rem;
                      color:#38bdf8; text-decoration:none; word-break:break-all;">{url}</a>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ──
st.markdown(f"""
<div class="footer">
    <strong style="color:#38bdf8; font-family:'Syne',sans-serif;">⚡ CloudAI Pulse</strong><br>
    Covering the intersection of Cloud &amp; Artificial Intelligence<br>
    Published {datetime.datetime.now().strftime("%B %d, %Y")} · All code samples MIT licensed<br><br>
    <span style="color:#1e293b;">Built with Python · Streamlit · Claude Sonnet 4.6 · Amazon Bedrock</span>
</div>
""", unsafe_allow_html=True)
