<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Fahad Khan — Data Analyst & AI Builder</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Serif+Display:ital@0;1&family=Space+Mono:wght@400;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<style>
  :root {
    --bg: #050810;
    --bg2: #080d1a;
    --surface: #0d1526;
    --surface2: #111c35;
    --accent: #00f5d4;
    --accent2: #7b61ff;
    --accent3: #ff6b6b;
    --gold: #f5c518;
    --text: #e8eaf6;
    --muted: #6b7db3;
    --border: rgba(0,245,212,0.15);
    --glow: 0 0 40px rgba(0,245,212,0.25);
    --glow2: 0 0 40px rgba(123,97,255,0.3);
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Outfit', sans-serif;
    overflow-x: hidden;
    cursor: none;
  }

  /* ─── CUSTOM CURSOR ─── */
  #cursor {
    width: 12px; height: 12px;
    background: var(--accent);
    border-radius: 50%;
    position: fixed; top: 0; left: 0;
    pointer-events: none; z-index: 9999;
    transform: translate(-50%,-50%);
    transition: transform 0.1s, width 0.2s, height 0.2s, background 0.2s;
    mix-blend-mode: screen;
  }
  #cursor-ring {
    width: 36px; height: 36px;
    border: 1.5px solid rgba(0,245,212,0.5);
    border-radius: 50%;
    position: fixed; top: 0; left: 0;
    pointer-events: none; z-index: 9998;
    transform: translate(-50%,-50%);
    transition: all 0.15s ease;
  }
  body:hover #cursor { width: 12px; height: 12px; }
  a:hover ~ #cursor, button:hover ~ #cursor { width: 20px; height: 20px; }

  /* ─── NOISE OVERLAY ─── */
  body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none; opacity: 0.35;
  }

  /* ─── GRID BACKGROUND ─── */
  body::after {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background-image:
      linear-gradient(rgba(0,245,212,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,245,212,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
  }

  /* ─── SCROLLBAR ─── */
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 2px; }

  /* ─── NAV ─── */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 60px;
    background: rgba(5,8,16,0.7);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
  }
  .nav-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; letter-spacing: 4px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .nav-links { display: flex; gap: 40px; list-style: none; }
  .nav-links a {
    font-family: 'Space Mono', monospace;
    font-size: 12px; letter-spacing: 2px;
    color: var(--muted); text-decoration: none;
    text-transform: uppercase;
    transition: color 0.3s;
    position: relative;
  }
  .nav-links a::after {
    content: ''; position: absolute; bottom: -4px; left: 0;
    width: 0; height: 1px; background: var(--accent);
    transition: width 0.3s;
  }
  .nav-links a:hover { color: var(--accent); }
  .nav-links a:hover::after { width: 100%; }
  .nav-status {
    display: flex; align-items: center; gap: 8px;
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: #00e676; letter-spacing: 1px;
  }
  .status-dot {
    width: 8px; height: 8px; background: #00e676;
    border-radius: 50%;
    box-shadow: 0 0 12px #00e676;
    animation: pulse-dot 2s infinite;
  }
  @keyframes pulse-dot {
    0%,100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.4); }
  }

  /* ─── HERO ─── */
  #hero {
    min-height: 100vh;
    display: flex; align-items: center; justify-content: center;
    position: relative; overflow: hidden;
    padding: 120px 60px 60px;
  }
  .hero-orb {
    position: absolute; border-radius: 50%;
    filter: blur(120px); pointer-events: none;
  }
  .orb1 { width: 600px; height: 600px; background: rgba(0,245,212,0.08); top: -100px; right: -100px; }
  .orb2 { width: 500px; height: 500px; background: rgba(123,97,255,0.1); bottom: -100px; left: -100px; }
  .orb3 { width: 300px; height: 300px; background: rgba(255,107,107,0.06); top: 50%; left: 50%; transform: translate(-50%,-50%); }

  .hero-inner {
    max-width: 1200px; width: 100%;
    display: grid; grid-template-columns: 1fr auto;
    gap: 60px; align-items: center;
    position: relative; z-index: 1;
  }
  .hero-tag {
    font-family: 'Space Mono', monospace; font-size: 12px;
    letter-spacing: 4px; color: var(--accent); text-transform: uppercase;
    margin-bottom: 24px;
    display: flex; align-items: center; gap: 12px;
  }
  .hero-tag::before {
    content: ''; display: inline-block;
    width: 40px; height: 1px; background: var(--accent);
  }
  .hero-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(72px, 10vw, 130px);
    line-height: 0.9; letter-spacing: 2px;
    background: linear-gradient(135deg, #ffffff 0%, var(--accent) 50%, var(--accent2) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: shimmer 4s ease-in-out infinite alternate;
  }
  @keyframes shimmer {
    0% { filter: brightness(1); }
    100% { filter: brightness(1.15); }
  }
  .hero-title {
    font-family: 'DM Serif Display', serif; font-style: italic;
    font-size: 24px; color: var(--muted); margin: 16px 0 32px;
    letter-spacing: 0.5px;
  }
  .hero-title span { color: var(--text); font-style: normal; }
  .hero-quote {
    font-size: 14px; color: var(--muted); max-width: 520px;
    line-height: 1.8; border-left: 2px solid var(--accent);
    padding-left: 20px; margin-bottom: 40px;
    font-style: italic;
  }
  .hero-cta { display: flex; gap: 16px; flex-wrap: wrap; }
  .btn {
    padding: 14px 32px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    letter-spacing: 2px; text-transform: uppercase;
    text-decoration: none; border-radius: 3px;
    transition: all 0.3s; cursor: pointer; border: none;
    position: relative; overflow: hidden;
  }
  .btn-primary {
    background: var(--accent); color: var(--bg);
    font-weight: 700;
    box-shadow: 0 0 30px rgba(0,245,212,0.3);
  }
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 50px rgba(0,245,212,0.5);
  }
  .btn-outline {
    background: transparent; color: var(--accent);
    border: 1px solid var(--accent);
  }
  .btn-outline:hover {
    background: rgba(0,245,212,0.08);
    transform: translateY(-2px);
  }

  /* HERO CARD */
  .hero-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px; padding: 32px;
    width: 280px;
    box-shadow: var(--glow);
    position: relative; overflow: hidden;
  }
  .hero-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2), var(--accent3));
  }
  .hero-card-avatar {
    width: 70px; height: 70px; border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    display: flex; align-items: center; justify-content: center;
    font-family: 'Bebas Neue', sans-serif; font-size: 28px; color: var(--bg);
    margin-bottom: 16px;
    box-shadow: 0 0 30px rgba(0,245,212,0.4);
  }
  .hero-card h3 { font-size: 16px; font-weight: 600; margin-bottom: 4px; }
  .hero-card p { font-size: 12px; color: var(--muted); margin-bottom: 20px; }
  .hero-card-stat {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 12px; margin-top: 16px;
  }
  .stat-item {
    text-align: center; padding: 12px;
    background: var(--surface2); border-radius: 8px;
    border: 1px solid var(--border);
  }
  .stat-item .num {
    font-family: 'Bebas Neue', sans-serif; font-size: 24px;
    color: var(--accent); display: block;
  }
  .stat-item .lbl { font-size: 10px; color: var(--muted); font-family: 'Space Mono', monospace; }
  .available-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(0,230,118,0.1); border: 1px solid rgba(0,230,118,0.3);
    border-radius: 20px; padding: 6px 14px;
    font-family: 'Space Mono', monospace; font-size: 10px;
    color: #00e676; letter-spacing: 1px;
    margin-top: 16px;
  }

  /* ─── SECTION ─── */
  section { position: relative; z-index: 1; padding: 100px 60px; max-width: 1200px; margin: 0 auto; }
  .section-label {
    font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 5px; color: var(--accent);
    text-transform: uppercase; margin-bottom: 12px;
    display: flex; align-items: center; gap: 12px;
  }
  .section-label::before {
    content: ''; width: 30px; height: 1px; background: var(--accent);
  }
  .section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(48px, 6vw, 72px); letter-spacing: 2px;
    line-height: 1; margin-bottom: 60px;
  }
  .section-title span {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }

  /* ─── ABOUT / YAML ─── */
  .about-grid {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 60px; align-items: start;
  }
  .about-text { font-size: 16px; line-height: 1.8; color: var(--muted); }
  .about-text strong { color: var(--text); }
  .yaml-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px; overflow: hidden;
    box-shadow: var(--glow2);
  }
  .yaml-header {
    background: var(--surface2); padding: 12px 20px;
    display: flex; align-items: center; gap: 8px;
    border-bottom: 1px solid var(--border);
  }
  .yaml-dot { width: 12px; height: 12px; border-radius: 50%; }
  .yaml-dot.r { background: #ff5f57; }
  .yaml-dot.y { background: #ffbd2e; }
  .yaml-dot.g { background: #28c840; }
  .yaml-filename { font-family: 'Space Mono', monospace; font-size: 12px; color: var(--muted); margin-left: 8px; }
  .yaml-body { padding: 24px; font-family: 'Space Mono', monospace; font-size: 13px; line-height: 1.9; }
  .yaml-key { color: var(--accent); }
  .yaml-val { color: #a8d8ea; }
  .yaml-colon { color: var(--muted); }
  .yaml-string { color: #f5c518; }
  .yaml-comment { color: var(--muted); opacity: 0.6; }

  /* ─── TECH STACK ─── */
  .stack-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
  .stack-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px; padding: 28px;
    transition: all 0.3s;
    position: relative; overflow: hidden;
  }
  .stack-card::after {
    content: ''; position: absolute;
    inset: 0; border-radius: 12px;
    background: linear-gradient(135deg, rgba(0,245,212,0.05), transparent);
    opacity: 0; transition: opacity 0.3s;
  }
  .stack-card:hover { transform: translateY(-4px); border-color: var(--accent); box-shadow: var(--glow); }
  .stack-card:hover::after { opacity: 1; }
  .stack-icon { font-size: 32px; margin-bottom: 16px; }
  .stack-cat {
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 3px; color: var(--accent);
    text-transform: uppercase; margin-bottom: 12px;
  }
  .stack-title { font-size: 18px; font-weight: 600; margin-bottom: 12px; }
  .tag-list { display: flex; flex-wrap: wrap; gap: 8px; }
  .tag {
    padding: 4px 12px; border-radius: 20px;
    font-family: 'Space Mono', monospace; font-size: 11px;
    background: var(--surface2); border: 1px solid var(--border);
    color: var(--muted); transition: all 0.2s;
  }
  .tag:hover { border-color: var(--accent); color: var(--accent); }
  .tag.accent { background: rgba(0,245,212,0.1); border-color: rgba(0,245,212,0.3); color: var(--accent); }
  .tag.purple { background: rgba(123,97,255,0.1); border-color: rgba(123,97,255,0.3); color: #b8a9ff; }
  .tag.red { background: rgba(255,107,107,0.1); border-color: rgba(255,107,107,0.3); color: #ff9a9a; }
  .tag.gold { background: rgba(245,197,24,0.1); border-color: rgba(245,197,24,0.3); color: var(--gold); }

  /* ─── EXPERIENCE ─── */
  .exp-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px; overflow: hidden;
    box-shadow: var(--glow2);
  }
  .exp-header {
    padding: 36px 40px;
    background: linear-gradient(135deg, rgba(123,97,255,0.1), rgba(0,245,212,0.05));
    border-bottom: 1px solid var(--border);
    display: grid; grid-template-columns: 1fr auto; align-items: center; gap: 20px;
  }
  .exp-company { font-family: 'Bebas Neue', sans-serif; font-size: 36px; letter-spacing: 2px; }
  .exp-company span { color: var(--accent2); }
  .exp-meta { font-size: 14px; color: var(--muted); margin-top: 4px; }
  .exp-badge {
    padding: 8px 20px; border-radius: 20px;
    background: rgba(123,97,255,0.15); border: 1px solid rgba(123,97,255,0.4);
    color: #b8a9ff; font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 1px; white-space: nowrap;
  }
  .exp-body { padding: 36px 40px; }
  .exp-items { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .exp-item {
    padding: 20px; border-radius: 10px;
    background: var(--surface2); border: 1px solid var(--border);
    transition: all 0.3s;
  }
  .exp-item:hover { border-color: var(--accent); transform: translateX(4px); }
  .exp-item-head {
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: var(--accent); letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 8px;
  }
  .exp-item p { font-size: 14px; color: var(--muted); line-height: 1.6; }
  .exp-item p strong { color: var(--text); }

  /* ─── PROJECTS ─── */
  .projects-grid { display: flex; flex-direction: column; gap: 40px; }
  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px; overflow: hidden;
    display: grid; grid-template-columns: 1fr 2fr;
    transition: all 0.3s;
    position: relative;
  }
  .project-card:hover { border-color: var(--accent); box-shadow: var(--glow); transform: translateY(-2px); }
  .project-visual {
    background: linear-gradient(135deg, var(--surface2), var(--bg2));
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 40px 20px; gap: 16px;
    border-right: 1px solid var(--border);
    position: relative; overflow: hidden;
  }
  .project-visual::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at center, rgba(0,245,212,0.08), transparent 70%);
  }
  .project-emoji { font-size: 56px; }
  .project-num {
    font-family: 'Bebas Neue', sans-serif; font-size: 80px;
    line-height: 1; color: rgba(255,255,255,0.04);
    position: absolute; bottom: -10px; right: -5px;
    user-select: none;
  }
  .project-year {
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: var(--muted); letter-spacing: 2px;
  }
  .project-body { padding: 36px 40px; }
  .project-cat {
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 3px; color: var(--accent);
    text-transform: uppercase; margin-bottom: 10px;
  }
  .project-title { font-size: 24px; font-weight: 700; margin-bottom: 10px; }
  .project-desc { font-size: 14px; color: var(--muted); line-height: 1.7; margin-bottom: 24px; }
  .project-stats {
    display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 20px;
  }
  .p-stat {
    display: flex; align-items: center; gap: 6px;
    font-family: 'Space Mono', monospace; font-size: 11px; color: var(--accent);
    background: rgba(0,245,212,0.08); border: 1px solid rgba(0,245,212,0.2);
    border-radius: 6px; padding: 6px 12px;
  }
  .project-card:nth-child(2) .project-visual::before { background: radial-gradient(circle at center, rgba(123,97,255,0.1), transparent 70%); }
  .project-card:nth-child(2) .project-cat,
  .project-card:nth-child(2) .p-stat { color: var(--accent2); }
  .project-card:nth-child(2) .p-stat { background: rgba(123,97,255,0.08); border-color: rgba(123,97,255,0.2); }
  .project-card:nth-child(3) .project-visual::before { background: radial-gradient(circle at center, rgba(245,197,24,0.08), transparent 70%); }
  .project-card:nth-child(3) .project-cat,
  .project-card:nth-child(3) .p-stat { color: var(--gold); }
  .project-card:nth-child(3) .p-stat { background: rgba(245,197,24,0.08); border-color: rgba(245,197,24,0.2); }

  /* ─── CERTIFICATIONS ─── */
  .cert-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
  .cert-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px; padding: 32px;
    display: flex; gap: 24px; align-items: flex-start;
    transition: all 0.3s; position: relative; overflow: hidden;
  }
  .cert-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
  }
  .cert-card:nth-child(1)::before { background: linear-gradient(90deg, #1A73E8, #4285F4); }
  .cert-card:nth-child(2)::before { background: linear-gradient(90deg, #86BC25, #4CAF50); }
  .cert-card:hover { transform: translateY(-4px); box-shadow: var(--glow); }
  .cert-icon {
    width: 56px; height: 56px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 28px; flex-shrink: 0;
  }
  .cert-card:nth-child(1) .cert-icon { background: rgba(26,115,232,0.15); }
  .cert-card:nth-child(2) .cert-icon { background: rgba(134,188,37,0.15); }
  .cert-issuer {
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 2px; color: var(--accent); margin-bottom: 6px;
    text-transform: uppercase;
  }
  .cert-name { font-size: 16px; font-weight: 600; margin-bottom: 6px; }
  .cert-date { font-size: 12px; color: var(--muted); }

  /* ─── CONTACT ─── */
  .contact-inner {
    display: grid; grid-template-columns: 1fr 1fr; gap: 60px;
    align-items: center;
  }
  .contact-text h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 64px; letter-spacing: 2px; line-height: 1;
    margin-bottom: 20px;
  }
  .contact-text h2 span { color: var(--accent); }
  .contact-text p { font-size: 15px; color: var(--muted); line-height: 1.8; margin-bottom: 32px; }
  .contact-links { display: flex; flex-direction: column; gap: 16px; }
  .contact-link {
    display: flex; align-items: center; gap: 16px;
    padding: 20px 24px; border-radius: 12px;
    background: var(--surface); border: 1px solid var(--border);
    text-decoration: none; color: var(--text);
    transition: all 0.3s; group: true;
  }
  .contact-link:hover { border-color: var(--accent); transform: translateX(8px); box-shadow: var(--glow); }
  .contact-link-icon {
    width: 44px; height: 44px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
  }
  .contact-link:nth-child(1) .contact-link-icon { background: rgba(10,102,194,0.15); }
  .contact-link:nth-child(2) .contact-link-icon { background: rgba(209,72,54,0.15); }
  .contact-link:nth-child(3) .contact-link-icon { background: rgba(255,255,255,0.08); }
  .contact-link:nth-child(4) .contact-link-icon { background: rgba(255,0,0,0.12); }
  .contact-link-info small {
    display: block; font-family: 'Space Mono', monospace;
    font-size: 10px; color: var(--muted); letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 2px;
  }
  .contact-link-info span { font-size: 14px; font-weight: 500; }
  .contact-link-arrow {
    margin-left: auto; color: var(--muted); font-size: 18px;
    transition: transform 0.3s, color 0.3s;
  }
  .contact-link:hover .contact-link-arrow { transform: translateX(4px); color: var(--accent); }

  /* ─── FOOTER ─── */
  footer {
    border-top: 1px solid var(--border);
    padding: 40px 60px;
    display: flex; align-items: center; justify-content: space-between;
    position: relative; z-index: 1;
  }
  footer .logo {
    font-family: 'Bebas Neue', sans-serif; font-size: 24px;
    letter-spacing: 4px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  footer p { font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); letter-spacing: 1px; }

  /* ─── ANIMATIONS ─── */
  .fade-in { opacity: 0; transform: translateY(30px); transition: all 0.7s cubic-bezier(0.4, 0, 0.2, 1); }
  .fade-in.visible { opacity: 1; transform: translateY(0); }
  .fade-delay-1 { transition-delay: 0.1s; }
  .fade-delay-2 { transition-delay: 0.2s; }
  .fade-delay-3 { transition-delay: 0.3s; }
  .fade-delay-4 { transition-delay: 0.4s; }

  /* ─── DIVIDER ─── */
  .divider {
    height: 1px; max-width: 1200px; margin: 0 auto;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
  }

  /* ─── SCROLLING MARQUEE ─── */
  .marquee-wrap {
    overflow: hidden; padding: 20px 0;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: var(--surface);
    position: relative; z-index: 1;
  }
  .marquee-inner {
    display: flex; gap: 60px; width: max-content;
    animation: marquee 20s linear infinite;
    white-space: nowrap;
  }
  .marquee-item {
    font-family: 'Bebas Neue', sans-serif; font-size: 18px;
    letter-spacing: 4px; color: var(--muted);
    display: flex; align-items: center; gap: 20px;
  }
  .marquee-item::after { content: '◆'; color: var(--accent); font-size: 10px; }
  @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

  /* ─── GITHUB STATS ─── */
  .github-section { text-align: center; }
  .github-cards {
    display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;
  }
  .github-card { border-radius: 12px; overflow: hidden; border: 1px solid var(--border); }
  .github-card img { width: 100%; display: block; }
  .github-streak { border-radius: 12px; overflow: hidden; border: 1px solid var(--border); margin-bottom: 20px; }
  .github-streak img { width: 100%; display: block; }
  .github-activity { border-radius: 12px; overflow: hidden; border: 1px solid var(--border); }
  .github-activity img { width: 100%; display: block; }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 900px) {
    nav { padding: 16px 24px; }
    .nav-links { display: none; }
    section { padding: 60px 24px; }
    #hero { padding: 100px 24px 60px; }
    .hero-inner { grid-template-columns: 1fr; }
    .hero-card { width: 100%; max-width: 320px; }
    .about-grid, .contact-inner { grid-template-columns: 1fr; }
    .stack-grid { grid-template-columns: 1fr 1fr; }
    .project-card { grid-template-columns: 1fr; }
    .project-visual { padding: 30px; flex-direction: row; }
    .cert-grid { grid-template-columns: 1fr; }
    .github-cards { grid-template-columns: 1fr; }
    footer { flex-direction: column; gap: 16px; text-align: center; }
    .exp-items { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<!-- CURSOR -->
<div id="cursor"></div>
<div id="cursor-ring"></div>

<!-- NAV -->
<nav>
  <div class="nav-logo">FK</div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#stack">Stack</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <div class="nav-status">
    <div class="status-dot"></div>
    Open to Work
  </div>
</nav>

<!-- HERO -->
<section id="hero" style="max-width:100%; padding-top:120px;">
  <div class="hero-orb orb1"></div>
  <div class="hero-orb orb2"></div>
  <div class="hero-orb orb3"></div>
  <div class="hero-inner" style="max-width:1200px; margin:0 auto;">
    <div>
      <div class="hero-tag fade-in">Based in Hyderabad, India</div>
      <h1 class="hero-name fade-in fade-delay-1">FAHAD<br/>KHAN</h1>
      <p class="hero-title fade-in fade-delay-2">
        <span>Data Analyst</span> · BI Engineer · <span>AI Builder</span>
      </p>
      <p class="hero-quote fade-in fade-delay-3">
        "Data is the new oil — I don't just collect it, I refine it into decisions."
      </p>
      <div class="hero-cta fade-in fade-delay-4">
        <a href="mailto:khanfahad004x@gmail.com" class="btn btn-primary">Email Me</a>
        <a href="https://www.linkedin.com/in/fahad-khan-134a61252" class="btn btn-outline" target="_blank">LinkedIn</a>
        <a href="https://github.com/RixzFahad" class="btn btn-outline" target="_blank">GitHub</a>
      </div>
    </div>
    <div class="fade-in fade-delay-3">
      <div class="hero-card">
        <div class="hero-card-avatar">FK</div>
        <h3>Fahad Khan</h3>
        <p>📍 Hyderabad, India · BCA 2022–2025</p>
        <div class="hero-card-stat">
          <div class="stat-item"><span class="num">3+</span><span class="lbl">Projects</span></div>
          <div class="stat-item"><span class="num">21K+</span><span class="lbl">Rows Analyzed</span></div>
          <div class="stat-item"><span class="num">2K+</span><span class="lbl">AI Chunks</span></div>
          <div class="stat-item"><span class="num">80%</span><span class="lbl">Faster Search</span></div>
        </div>
        <div class="available-badge">
          <div class="status-dot"></div>
          OPEN TO WORK
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MARQUEE -->
<div class="marquee-wrap">
  <div class="marquee-inner">
    <div class="marquee-item">Power BI</div>
    <div class="marquee-item">SQL</div>
    <div class="marquee-item">Python</div>
    <div class="marquee-item">DAX</div>
    <div class="marquee-item">RAG / LLM</div>
    <div class="marquee-item">Data Analytics</div>
    <div class="marquee-item">KPI Dashboards</div>
    <div class="marquee-item">EDA</div>
    <div class="marquee-item">AI Pipelines</div>
    <div class="marquee-item">Tableau</div>
    <div class="marquee-item">OpenAI</div>
    <div class="marquee-item">Vector Embeddings</div>
    <!-- duplicate for seamless loop -->
    <div class="marquee-item">Power BI</div>
    <div class="marquee-item">SQL</div>
    <div class="marquee-item">Python</div>
    <div class="marquee-item">DAX</div>
    <div class="marquee-item">RAG / LLM</div>
    <div class="marquee-item">Data Analytics</div>
    <div class="marquee-item">KPI Dashboards</div>
    <div class="marquee-item">EDA</div>
    <div class="marquee-item">AI Pipelines</div>
    <div class="marquee-item">Tableau</div>
    <div class="marquee-item">OpenAI</div>
    <div class="marquee-item">Vector Embeddings</div>
  </div>
</div>

<!-- ABOUT -->
<section id="about">
  <div class="section-label fade-in">01 — About Me</div>
  <h2 class="section-title fade-in"><span>WHO</span> I AM</h2>
  <div class="about-grid">
    <div class="about-text fade-in">
      <p>I'm a <strong>Data Analyst from Hyderabad, India</strong> who turns messy, unstructured data into clean dashboards and compelling business stories. My toolkit spans <strong>Power BI</strong>, <strong>SQL</strong>, <strong>Python</strong>, and <strong>AI pipelines</strong> — from real-time API-driven dashboards to RAG-based LLM systems.</p>
      <br/>
      <p>Currently pursuing my <strong>BCA at Dr. RML Awadh University (2022–2025)</strong> and gaining real-world experience through a <strong>Deloitte Australia Data Analytics virtual internship</strong> via Forage.</p>
      <br/>
      <p>My focus areas include <strong>KPI Dashboards</strong>, <strong>Exploratory Data Analysis</strong>, <strong>Predictive Analytics</strong>, and cutting-edge <strong>RAG/LLM systems</strong> that bring AI into business intelligence.</p>
    </div>
    <div class="yaml-block fade-in fade-delay-2">
      <div class="yaml-header">
        <div class="yaml-dot r"></div>
        <div class="yaml-dot y"></div>
        <div class="yaml-dot g"></div>
        <span class="yaml-filename">fahad.yaml</span>
      </div>
      <div class="yaml-body">
        <div><span class="yaml-key">name</span><span class="yaml-colon"> : </span><span class="yaml-string">Fahad Khan</span></div>
        <div><span class="yaml-key">role</span><span class="yaml-colon"> : </span><span class="yaml-val">Data Analyst | BI Developer | AI Enthusiast</span></div>
        <div><span class="yaml-key">location</span><span class="yaml-colon"> : </span><span class="yaml-string">Hyderabad, India</span></div>
        <div><span class="yaml-key">education</span><span class="yaml-colon"> : </span><span class="yaml-val">BCA — Dr. RML Awadh University</span></div>
        <div style="padding-left:16px"><span class="yaml-comment"># 2022–2025</span></div>
        <div><span class="yaml-key">experience</span><span class="yaml-colon"> : </span><span class="yaml-val">Deloitte Australia (Forage)</span></div>
        <div style="padding-left:16px"><span class="yaml-comment"># Data Analytics Intern</span></div>
        <div><span class="yaml-key">focus</span><span class="yaml-colon"> :</span></div>
        <div style="padding-left:16px"><span class="yaml-val">- KPI Dashboards</span></div>
        <div style="padding-left:16px"><span class="yaml-val">- EDA & Predictive Analytics</span></div>
        <div style="padding-left:16px"><span class="yaml-val">- RAG / LLM Pipelines</span></div>
        <div><span class="yaml-key">contact</span><span class="yaml-colon"> :</span></div>
        <div style="padding-left:16px"><span class="yaml-key">email</span><span class="yaml-colon"> : </span><span class="yaml-string">khanfahad004x@gmail.com</span></div>
        <div style="padding-left:16px"><span class="yaml-key">phone</span><span class="yaml-colon"> : </span><span class="yaml-string">+91-7355710686</span></div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- TECH STACK -->
<section id="stack">
  <div class="section-label fade-in">02 — Technologies</div>
  <h2 class="section-title fade-in">TECH <span>STACK</span></h2>
  <div class="stack-grid">
    <div class="stack-card fade-in">
      <div class="stack-icon">🔤</div>
      <div class="stack-cat">Languages</div>
      <div class="stack-title">Core Languages</div>
      <div class="tag-list">
        <span class="tag accent">Python</span>
        <span class="tag accent">SQL</span>
        <span class="tag gold">DAX</span>
        <span class="tag">M Query</span>
      </div>
    </div>
    <div class="stack-card fade-in fade-delay-1">
      <div class="stack-icon">📊</div>
      <div class="stack-cat">BI & Visualization</div>
      <div class="stack-title">Business Intelligence</div>
      <div class="tag-list">
        <span class="tag gold">Power BI</span>
        <span class="tag">Tableau</span>
        <span class="tag accent">Looker Studio</span>
        <span class="tag">Alteryx</span>
      </div>
    </div>
    <div class="stack-card fade-in fade-delay-2">
      <div class="stack-icon">🐍</div>
      <div class="stack-cat">Python Libraries</div>
      <div class="stack-title">Data & AI Stack</div>
      <div class="tag-list">
        <span class="tag accent">Pandas</span>
        <span class="tag">NumPy</span>
        <span class="tag">Matplotlib</span>
        <span class="tag purple">OpenAI</span>
        <span class="tag">Scikit-learn</span>
      </div>
    </div>
    <div class="stack-card fade-in fade-delay-1">
      <div class="stack-icon">🗄️</div>
      <div class="stack-cat">Databases</div>
      <div class="stack-title">Data Storage</div>
      <div class="tag-list">
        <span class="tag accent">MySQL</span>
        <span class="tag accent">PostgreSQL</span>
        <span class="tag">Vector DB</span>
      </div>
    </div>
    <div class="stack-card fade-in fade-delay-2">
      <div class="stack-icon">🤖</div>
      <div class="stack-cat">AI / ML</div>
      <div class="stack-title">Intelligence Layer</div>
      <div class="tag-list">
        <span class="tag purple">RAG Pipelines</span>
        <span class="tag purple">LLM Prompting</span>
        <span class="tag">Whisper</span>
        <span class="tag">Embeddings</span>
      </div>
    </div>
    <div class="stack-card fade-in fade-delay-3">
      <div class="stack-icon">🛠️</div>
      <div class="stack-cat">Dev Tools</div>
      <div class="stack-title">Workflow & Design</div>
      <div class="tag-list">
        <span class="tag">Git</span>
        <span class="tag">GitHub</span>
        <span class="tag">MS Excel</span>
        <span class="tag red">Figma</span>
        <span class="tag">React</span>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- EXPERIENCE -->
<section id="experience">
  <div class="section-label fade-in">03 — Experience</div>
  <h2 class="section-title fade-in">WHERE I'VE <span>WORKED</span></h2>
  <div class="exp-block fade-in">
    <div class="exp-header">
      <div>
        <div class="exp-company">DELOITTE <span>AUSTRALIA</span></div>
        <div class="exp-meta">📌 Data Analytics Intern &nbsp;·&nbsp; June 2025 &nbsp;·&nbsp; Virtual (Forage)</div>
      </div>
      <div class="exp-badge">FORAGE VIRTUAL</div>
    </div>
    <div class="exp-body">
      <div class="exp-items">
        <div class="exp-item">
          <div class="exp-item-head">📈 Exploratory Data Analysis</div>
          <p>Executed EDA on <strong>3+ business datasets</strong>, surfacing trends, anomalies & patterns for strategic decisions.</p>
        </div>
        <div class="exp-item">
          <div class="exp-item-head">📊 KPI Dashboard Engineering</div>
          <p>Built executive-ready <strong>Power BI dashboards</strong> transforming complex metrics into compelling visual reports.</p>
        </div>
        <div class="exp-item">
          <div class="exp-item-head">🔍 Forensic Analytics</div>
          <p>Applied forensic analytics for <strong>financial irregularities</strong>, enabling faster root-cause identification.</p>
        </div>
        <div class="exp-item">
          <div class="exp-item-head">🎯 Stakeholder Delivery</div>
          <p>Delivered <strong>4 structured presentations</strong> on time with <strong>100% stakeholder satisfaction</strong> & quality benchmarks met.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- PROJECTS -->
<section id="projects">
  <div class="section-label fade-in">04 — Work</div>
  <h2 class="section-title fade-in">FEATURED <span>PROJECTS</span></h2>
  <div class="projects-grid">

    <!-- PROJECT 1 -->
    <div class="project-card fade-in">
      <div class="project-visual">
        <div class="project-emoji">🌦️</div>
        <div class="project-year">Jun–Jul 2025</div>
        <div class="project-num">01</div>
      </div>
      <div class="project-body">
        <div class="project-cat">Power BI · REST API · Time-Series</div>
        <div class="project-title">Weather Forecast Dashboard</div>
        <div class="project-desc">Real-time meteorological intelligence — live weather & AQI analytics at your fingertips. Integrated multiple live APIs into a dynamic Power BI dashboard with drill-down interactivity by city and date range.</div>
        <div class="project-stats">
          <span class="p-stat">📡 2+ REST APIs Integrated</span>
          <span class="p-stat">⚡ 10+ DAX Measures</span>
          <span class="p-stat">🗺️ City × Time Drill-down</span>
          <span class="p-stat">📈 Rolling Window Analysis</span>
        </div>
        <div class="tag-list">
          <span class="tag accent">Power BI</span>
          <span class="tag accent">DAX</span>
          <span class="tag">REST API</span>
          <span class="tag">Time-Series</span>
          <span class="tag">AQI Analytics</span>
        </div>
      </div>
    </div>

    <!-- PROJECT 2 -->
    <div class="project-card fade-in">
      <div class="project-visual">
        <div class="project-emoji">🤖</div>
        <div class="project-year">2025</div>
        <div class="project-num">02</div>
      </div>
      <div class="project-body">
        <div class="project-cat">Python · OpenAI · RAG · LLM</div>
        <div class="project-title">RAG-Based AI Teaching Assistant</div>
        <div class="project-desc">AI-powered knowledge retrieval system — ask any question, get timestamped answers from 50+ transcribed videos. Built a full end-to-end RAG pipeline with Whisper transcription, semantic chunking, and cosine similarity search.</div>
        <div class="project-stats">
          <span class="p-stat">🎙️ 50+ Videos Transcribed</span>
          <span class="p-stat">🧩 2,000+ Semantic Chunks</span>
          <span class="p-stat">🔍 Top-5 Cosine Similarity</span>
          <span class="p-stat">⚡ 80% Faster Discovery</span>
        </div>
        <div class="tag-list">
          <span class="tag purple">RAG Pipeline</span>
          <span class="tag purple">OpenAI Whisper</span>
          <span class="tag">Vector Embeddings</span>
          <span class="tag">LLM Prompting</span>
          <span class="tag">Python</span>
        </div>
      </div>
    </div>

    <!-- PROJECT 3 -->
    <div class="project-card fade-in">
      <div class="project-visual">
        <div class="project-emoji">📒</div>
        <div class="project-year">2026</div>
        <div class="project-num">03</div>
      </div>
      <div class="project-body">
        <div class="project-cat">Power BI · Python · SQL · Financial Analytics</div>
        <div class="project-title">Business Ledger Analytics Dashboard</div>
        <div class="project-desc">Real-world financial intelligence — 21,000+ transactions turned into actionable BI. Cleaned and normalized complex ledger data covering Accounts Receivable, Accounts Payable, and bank reconciliation records.</div>
        <div class="project-stats">
          <span class="p-stat">🏦 21,000+ Transactions</span>
          <span class="p-stat">🤝 1,200+ Business Partners</span>
          <span class="p-stat">🧹 Python + SQL Cleaning</span>
          <span class="p-stat">💼 Full AR · AP · Bank Coverage</span>
        </div>
        <div class="tag-list">
          <span class="tag gold">Power BI</span>
          <span class="tag gold">Financial Analytics</span>
          <span class="tag">Python</span>
          <span class="tag">SQL</span>
          <span class="tag">GST Normalization</span>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- CERTIFICATIONS -->
<section id="certs">
  <div class="section-label fade-in">05 — Credentials</div>
  <h2 class="section-title fade-in">CERTIFI<span>CATIONS</span></h2>
  <div class="cert-grid">
    <div class="cert-card fade-in">
      <div class="cert-icon">📊</div>
      <div>
        <div class="cert-issuer">TATA via Forage</div>
        <div class="cert-name">Data Visualisation: Empowering Business with Effective Insights</div>
        <div class="cert-date">🗓️ September 2025</div>
      </div>
    </div>
    <div class="cert-card fade-in fade-delay-2">
      <div class="cert-icon">🔐</div>
      <div>
        <div class="cert-issuer">Deloitte via Forage</div>
        <div class="cert-name">Cyber Job Simulation</div>
        <div class="cert-date">🗓️ June 2025</div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- GITHUB STATS -->
<section id="github" class="github-section">
  <div class="section-label fade-in" style="justify-content:center; margin-bottom:12px;">06 — Open Source</div>
  <h2 class="section-title fade-in" style="text-align:center;">GITHUB <span>ANALYTICS</span></h2>
  <div class="github-cards fade-in">
    <div class="github-card">
      <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=RixzFahad&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats"/>
    </div>
    <div class="github-card">
      <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=RixzFahad&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top Languages"/>
    </div>
  </div>
  <div class="github-streak fade-in">
    <img src="https://streak-stats.demolab.com?user=RixzFahad&theme=tokyonight&hide_border=true" alt="Streak"/>
  </div>
  <div class="github-activity fade-in">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=RixzFahad&theme=tokyo-night&hide_border=true&area=true" alt="Activity Graph"/>
  </div>
</section>

<div class="divider"></div>

<!-- CONTACT -->
<section id="contact">
  <div class="contact-inner">
    <div class="contact-text fade-in">
      <div class="section-label" style="margin-bottom:16px;">07 — Contact</div>
      <h2>LET'S <span>CONNECT</span></h2>
      <p>Open to Data Analyst roles, BI projects, and AI collaboration. Whether you have a project in mind or just want to say hello — my inbox is always open.</p>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <span class="tag accent">+91-7355710686</span>
        <span class="tag">Hyderabad, India</span>
        <span class="tag gold">Open to Work</span>
      </div>
    </div>
    <div class="contact-links fade-in fade-delay-2">
      <a href="https://www.linkedin.com/in/fahad-khan-134a61252" class="contact-link" target="_blank">
        <div class="contact-link-icon">🔵</div>
        <div class="contact-link-info">
          <small>LinkedIn</small>
          <span>fahad-khan-134a61252</span>
        </div>
        <div class="contact-link-arrow">→</div>
      </a>
      <a href="mailto:khanfahad004x@gmail.com" class="contact-link">
        <div class="contact-link-icon">📧</div>
        <div class="contact-link-info">
          <small>Gmail</small>
          <span>khanfahad004x@gmail.com</span>
        </div>
        <div class="contact-link-arrow">→</div>
      </a>
      <a href="https://github.com/RixzFahad" class="contact-link" target="_blank">
        <div class="contact-link-icon">⚫</div>
        <div class="contact-link-info">
          <small>GitHub</small>
          <span>RixzFahad</span>
        </div>
        <div class="contact-link-arrow">→</div>
      </a>
      <a href="https://www.youtube.com/@24kgoldnhunter14" class="contact-link" target="_blank">
        <div class="contact-link-icon">🔴</div>
        <div class="contact-link-info">
          <small>YouTube</small>
          <span>@24kgoldnhunter14</span>
        </div>
        <div class="contact-link-arrow">→</div>
      </a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="logo">FK</div>
  <p>© 2025 Fahad Khan · Hyderabad, India</p>
  <p style="font-family:'Space Mono',monospace; font-size:11px; color:var(--muted);">Built with 💚 & data-driven decisions</p>
</footer>

<script>
  // Custom cursor
  const cursor = document.getElementById('cursor');
  const ring = document.getElementById('cursor-ring');
  let mx = 0, my = 0, rx = 0, ry = 0;
  document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
  function animateCursor() {
    cursor.style.left = mx + 'px'; cursor.style.top = my + 'px';
    rx += (mx - rx) * 0.12; ry += (my - ry) * 0.12;
    ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
    requestAnimationFrame(animateCursor);
  }
  animateCursor();
  document.querySelectorAll('a, button, .stack-card, .contact-link').forEach(el => {
    el.addEventListener('mouseenter', () => { cursor.style.width = '20px'; cursor.style.height = '20px'; ring.style.width = '50px'; ring.style.height = '50px'; ring.style.borderColor = 'rgba(0,245,212,0.8)'; });
    el.addEventListener('mouseleave', () => { cursor.style.width = '12px'; cursor.style.height = '12px'; ring.style.width = '36px'; ring.style.height = '36px'; ring.style.borderColor = 'rgba(0,245,212,0.5)'; });
  });

  // Scroll reveal
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  // Number counter animation
  function animateNum(el, target, suffix = '') {
    let current = 0;
    const step = target / 60;
    const timer = setInterval(() => {
      current += step;
      if (current >= target) { current = target; clearInterval(timer); }
      el.textContent = (suffix === 'K+' ? Math.floor(current) + 'K+' : Math.floor(current) + suffix);
    }, 20);
  }
  const statsObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const nums = e.target.querySelectorAll('.num');
        nums.forEach(n => {
          const txt = n.textContent;
          if (txt.includes('K+')) animateNum(n, 21, 'K+');
          else if (txt.includes('%')) animateNum(n, 80, '%');
          else if (txt.includes('K+')) animateNum(n, 2, 'K+');
          else if (txt === '3+') animateNum(n, 3, '+');
          else if (txt === '2K+') animateNum(n, 2, 'K+');
        });
        statsObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });
  const heroCard = document.querySelector('.hero-card-stat');
  if (heroCard) statsObs.observe(heroCard);
</script>

</body>
</html>
