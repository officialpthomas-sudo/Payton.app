<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Review Forensics Fake Review Detector</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Courier+Prime:wght@400;700&family=Inter:wght@400;500;600;700&display=swap');

:root{
  --desk: #24312B;
  --desk-dark: #1B2621;
  --paper: #E9E2CF;
  --ink: #2B2620;
  --ink-soft: #5A5142;
  --amber: #C98A2B;
  --amber-bg: #F0C878;
  --coral: #A6321F;
  --coral-bg: #E8A896;
  --teal: #2F6B5A;
  --teal-bg: #9FCBBE;
  --twine: #8A6D3B;
  --purple-bg: #C9B7E0;
  --gold-bg: #F5E6A8;
  --peach-bg: #F0C8A8;
}

*{box-sizing:border-box;}
html,body{margin:0;padding:0;}

body{
  min-height:100vh;
  background:
    radial-gradient(ellipse at 30% 0%, rgba(255,255,255,0.04), transparent 60%),
    repeating-linear-gradient(45deg, rgba(0,0,0,0.015) 0px, rgba(0,0,0,0.015) 2px, transparent 2px, transparent 4px),
    linear-gradient(180deg, var(--desk) 0%, var(--desk-dark) 100%);
  font-family:'Inter', sans-serif;
  color:var(--paper);
  padding:32px 16px 80px;
  display:flex;
  flex-direction:column;
  align-items:center;
}

.header{
  width:100%;
  max-width:800px;
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  margin-bottom:22px;
  border-bottom:2px solid rgba(233,226,207,0.25);
  padding-bottom:14px;
  flex-wrap:wrap;
  gap:10px;
}

.header h1{
  font-family:'Special Elite', cursive;
  font-size:1.7rem;
  letter-spacing:1px;
  margin:0;
  color:var(--paper);
  text-shadow: 1px 1px 0 rgba(0,0,0,0.3);
}

.header .sub{
  font-size:0.72rem;
  letter-spacing:2px;
  text-transform:uppercase;
  color:rgba(233,226,207,0.55);
  margin-top:4px;
}

.case-no{
  font-family:'Courier Prime', monospace;
  font-size:0.8rem;
  color:rgba(233,226,207,0.6);
  text-align:right;
  white-space:nowrap;
}

.folder{
  width:100%;
  max-width:800px;
  position:relative;
}

.tab{
  display:inline-block;
  background:var(--twine);
  color:#F3ECD8;
  font-family:'Special Elite', cursive;
  font-size:0.72rem;
  letter-spacing:2px;
  padding:6px 18px 8px;
  border-radius:6px 6px 0 0;
  transform:translateY(2px);
  box-shadow: 0 -1px 0 rgba(0,0,0,0.15) inset;
}

.paper{
  background:
    repeating-linear-gradient(180deg, rgba(0,0,0,0.02) 0px, rgba(0,0,0,0.02) 1px, transparent 1px, transparent 28px),
    var(--paper);
  border-radius:2px 10px 10px 10px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.45), 0 2px 0 rgba(0,0,0,0.15);
  padding:26px 26px 22px;
  color:var(--ink);
}

label.field-label{
  display:block;
  font-family:'Courier Prime', monospace;
  font-weight:700;
  font-size:0.78rem;
  letter-spacing:1.5px;
  text-transform:uppercase;
  color:var(--ink-soft);
  margin-bottom:8px;
}

textarea{
  width:100%;
  min-height:160px;
  resize:vertical;
  font-family:'Courier Prime', monospace;
  font-size:0.95rem;
  line-height:1.55;
  color:var(--ink);
  background:rgba(255,255,255,0.35);
  border:1px solid rgba(43,38,32,0.25);
  border-radius:4px;
  padding:14px;
}

textarea:focus-visible, button:focus-visible{
  outline:3px solid var(--teal);
  outline-offset:2px;
}

.controls{
  display:flex;
  align-items:center;
  gap:14px;
  margin-top:16px;
  flex-wrap:wrap;
}

button.analyze{
  font-family:'Special Elite', cursive;
  font-size:0.95rem;
  letter-spacing:1.5px;
  color:#F3ECD8;
  background:var(--coral);
  border:2px solid #7a2416;
  border-radius:4px;
  padding:11px 22px;
  cursor:pointer;
  transform:rotate(-1deg);
  transition:transform 0.15s ease, box-shadow 0.15s ease;
  box-shadow:0 3px 0 #7a2416;
}
button.analyze:hover{ transform:rotate(-1deg) translateY(-1px); box-shadow:0 4px 0 #7a2416; }
button.analyze:active{ transform:rotate(-1deg) translateY(2px); box-shadow:0 1px 0 #7a2416; }
button.analyze:disabled{ opacity:0.55; cursor:progress; }

button.reset{
  font-family:'Inter', sans-serif;
  font-size:0.82rem;
  color:var(--ink-soft);
  background:transparent;
  border:1px solid rgba(43,38,32,0.3);
  border-radius:4px;
  padding:9px 14px;
  cursor:pointer;
}
button.reset:hover{ background:rgba(43,38,32,0.06); }

.char-count{
  font-family:'Courier Prime', monospace;
  font-size:0.75rem;
  color:var(--ink-soft);
  margin-left:auto;
}

.status-line{
  font-family:'Courier Prime', monospace;
  font-size:0.85rem;
  color:var(--ink-soft);
  margin-top:14px;
  min-height:1.2em;
}

.error-box{
  margin-top:14px;
  border:1px dashed var(--coral);
  color:var(--coral);
  font-family:'Courier Prime', monospace;
  font-size:0.85rem;
  padding:10px 12px;
  border-radius:4px;
}

.results{
  margin-top:26px;
  padding-top:20px;
  border-top:2px dashed rgba(43,38,32,0.3);
  display:none;
}
.results.show{ display:block; }

.verdict-row{
  display:flex;
  align-items:center;
  gap:22px;
  flex-wrap:wrap;
  margin-bottom:14px;
}

.stamp{
  font-family:'Special Elite', cursive;
  border:4px double var(--stamp-color, var(--coral));
  color:var(--stamp-color, var(--coral));
  border-radius:8px;
  padding:10px 16px;
  text-align:center;
  transform:rotate(-7deg);
  display:inline-block;
  text-shadow:0.5px 0.5px 0 currentColor;
  animation: stamp-in 0.35s cubic-bezier(.2,1.5,.4,1) both;
}
.stamp .pct{ font-size:1.9rem; line-height:1; display:block; letter-spacing:1px; }
.stamp .label{ font-size:0.66rem; letter-spacing:1.5px; text-transform:uppercase; display:block; margin-top:2px; max-width:170px; }

@media (prefers-reduced-motion: reduce){
  .stamp{ animation:none; }
}
@keyframes stamp-in{
  0%{ opacity:0; transform:rotate(-7deg) scale(1.7); }
  100%{ opacity:1; transform:rotate(-7deg) scale(1); }
}

.summary-text{
  font-family:'Courier Prime', monospace;
  font-size:0.92rem;
  line-height:1.5;
  color:var(--ink);
  max-width:440px;
}

/* Pattern scan panel */
.scan-panel{
  margin-bottom:20px;
  background:rgba(255,255,255,0.28);
  border:1px solid rgba(43,38,32,0.2);
  border-radius:4px;
  padding:14px 16px;
}
.scan-panel h3{
  font-family:'Special Elite', cursive;
  font-size:0.82rem;
  letter-spacing:1px;
  text-transform:uppercase;
  margin:0 0 10px;
  color:var(--ink-soft);
}
.scan-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit, minmax(190px, 1fr));
  gap:10px;
}
.scan-item{
  font-family:'Inter', sans-serif;
  font-size:0.82rem;
  display:flex;
  align-items:baseline;
  gap:8px;
  color:var(--ink);
}
.scan-item .n{
  font-family:'Courier Prime', monospace;
  font-weight:700;
  font-size:1rem;
  min-width:22px;
}
.scan-item.flagged .n{ color:var(--coral); }
.scan-item.clear .n{ color:var(--teal); }

.legend{
  display:flex;
  gap:14px;
  flex-wrap:wrap;
  margin-bottom:14px;
  font-family:'Inter', sans-serif;
  font-size:0.72rem;
  color:var(--ink-soft);
}
.legend span{ display:inline-flex; align-items:center; gap:6px; }
.legend i{ width:14px; height:12px; border-radius:2px; display:inline-block; }
.legend i.dashed{ border-bottom:2px dashed var(--twine); background:var(--gold-bg); }

.exhibit-text{
  font-family:'Courier Prime', monospace;
  font-size:0.92rem;
  line-height:1.8;
  white-space:pre-wrap;
  color:var(--ink);
  background:rgba(255,255,255,0.3);
  border:1px solid rgba(43,38,32,0.2);
  border-radius:4px;
  padding:16px;
}

mark{
  border-radius:2px;
  padding:0 2px;
  cursor:help;
}
/* AI-judged categories: solid highlight */
mark.generic_praise{ background:var(--amber-bg); }
mark.unnatural_phrasing{ background:var(--coral-bg); }
mark.incentivized{ background:var(--teal-bg); }
mark.excessive_detail{ background:var(--purple-bg); }
mark.other{ background:#CFCAB8; }
/* Pattern-scan categories: dashed underline, lighter fill */
mark.repeated_phrase{ background:var(--gold-bg); border-bottom:2px dashed var(--twine); }
mark.exaggeration{ background:var(--peach-bg); border-bottom:2px dashed var(--twine); }

.notes{
  margin-top:18px;
  font-family:'Inter', sans-serif;
  font-size:0.85rem;
  color:var(--ink);
}
.notes h3{
  font-family:'Special Elite', cursive;
  font-size:0.85rem;
  letter-spacing:1px;
  color:var(--ink-soft);
  margin:0 0 8px;
  text-transform:uppercase;
}
.notes ul{ margin:0; padding-left:20px; }
.notes li{ margin-bottom:6px; }
.notes .cat-tag{
  font-size:0.68rem;
  text-transform:uppercase;
  letter-spacing:1px;
  color:var(--ink-soft);
  margin-right:6px;
}

footer{
  max-width:800px;
  width:100%;
  margin-top:24px;
  font-family:'Inter', sans-serif;
  font-size:0.7rem;
  color:rgba(233,226,207,0.4);
  text-align:center;
}

@media (max-width:600px){
  .header{ flex-direction:column; align-items:flex-start; gap:6px; }
  .case-no{ text-align:left; }
  .paper{ padding:18px 16px 16px; }
}
</style>
</head>
<body>

<div class="header">
  <div>
    <h1>REVIEW FORENSICS</h1>
    <div class="sub">Fake review analysis unit</div>
  </div>
  <div class="case-no" id="caseNo">CASE #000000</div>
</div>

<div class="folder">
  <div class="tab">EXHIBIT A — SUBMITTED TEXT</div>
  <div class="paper">
    <label class="field-label" for="reviewInput">Paste the review text below</label>
    <textarea id="reviewInput" placeholder="Paste a review from Amazon, Google, Yelp, or anywhere else here..."></textarea>

    <div class="controls">
      <button class="analyze" id="analyzeBtn">RUN ANALYSIS</button>
      <button class="reset" id="resetBtn">New case</button>
      <span class="char-count" id="charCount">0 characters</span>
    </div>

    <div class="status-line" id="statusLine"></div>
    <div class="error-box" id="errorBox" style="display:none;"></div>

    <div class="results" id="results">

      <div class="scan-panel" id="scanPanel">
        <h3>Pattern scan (deterministic)</h3>
        <div class="scan-grid" id="scanGrid"></div>
      </div>

      <div class="verdict-row">
        <div class="stamp" id="stamp">
          <span class="pct" id="stampPct">--%</span>
          <span class="label" id="stampLabel">PENDING</span>
        </div>
        <div class="summary-text" id="summaryText"></div>
      </div>

      <div class="legend">
        <span><i style="background:var(--amber-bg);"></i>Generic praise (AI)</span>
        <span><i style="background:var(--coral-bg);"></i>Unnatural phrasing (AI)</span>
        <span><i style="background:var(--teal-bg);"></i>Incentivized (AI)</span>
        <span><i style="background:var(--purple-bg);"></i>Excessive detail (AI)</span>
        <span><i class="dashed"></i>Repeated / exaggerated (pattern scan)</span>
      </div>

      <div class="exhibit-text" id="exhibitText"></div>

      <div class="notes" id="notes"></div>
    </div>
  </div>
</div>

<footer>Combines a deterministic pattern scan with AI contextual analysis. Treat results as an investigative lead, not a verdict.</footer>

<script>
const caseNoEl = document.getElementById('caseNo');
caseNoEl.textContent = 'CASE #' + Math.floor(100000 + Math.random()*900000);

const textarea = document.getElementById('reviewInput');
const charCount = document.getElementById('charCount');
const analyzeBtn = document.getElementById('analyzeBtn');
const resetBtn = document.getElementById('resetBtn');
const statusLine = document.getElementById('statusLine');
const errorBox = document.getElementById('errorBox');
const results = document.getElementById('results');
const stamp = document.getElementById('stamp');
const stampPct = document.getElementById('stampPct');
const stampLabel = document.getElementById('stampLabel');
const summaryText = document.getElementById('summaryText');
const exhibitText = document.getElementById('exhibitText');
const notesEl = document.getElementById('notes');
const scanGrid = document.getElementById('scanGrid');

textarea.addEventListener('input', () => {
  charCount.textContent = textarea.value.length + ' characters';
});

resetBtn.addEventListener('click', () => {
  textarea.value = '';
  charCount.textContent = '0 characters';
  results.classList.remove('show');
  errorBox.style.display = 'none';
  statusLine.textContent = '';
  caseNoEl.textContent = 'CASE #' + Math.floor(100000 + Math.random()*900000);
});

function escapeHtml(str){
  return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

const EXAGGERATION_PHRASES = [
  'amazing','incredible','unbelievable','life-changing','life changing',
  'game changer','game-changer','perfect','flawless','exceeded my expectations',
  'exceeded all expectations','highly recommend','best purchase','best product',
  'obsessed','changed my life','outstanding','phenomenal','superb',
  'excellent quality','top notch','top-notch','five stars','must buy',
  'must have','blown away','literally the best','absolutely love',
  'exceeded expectations','can\\'t believe','never disappoints'
];

/* ---------- Deterministic pattern scan (no API needed) ---------- */
function localScan(text){
  const wordMatches = [...text.matchAll(/[A-Za-z']+/g)];
  const words = wordMatches.map(m => ({ word: m[0], index: m.index }));

  // Repeated 3-word phrases (trigrams), require at least one word len >= 4 to cut noise
  const trigramMap = new Map();
  for(let i = 0; i <= words.length - 3; i++){
    const slice = words.slice(i, i+3);
    if(!slice.some(w => w.word.length >= 4)) continue;
    const key = slice.map(w => w.word.toLowerCase()).join(' ');
    const start = slice[0].index;
    const end = slice[2].index + slice[2].word.length;
    if(!trigramMap.has(key)) trigramMap.set(key, []);
    trigramMap.get(key).push({ start, end });
  }
  const repeatedPhrases = [...trigramMap.entries()]
    .filter(([,occ]) => occ.length >= 2)
    .map(([phrase, occ]) => ({ phrase, occurrences: occ }));

  // Exaggerated / hyperbolic language
  const lowerText = text.toLowerCase();
  const exaggerationHits = [];
  for(const phrase of EXAGGERATION_PHRASES){
    let fromIdx = 0;
    while(true){
      const idx = lowerText.indexOf(phrase, fromIdx);
      if(idx === -1) break;
      exaggerationHits.push({ phrase, start: idx, end: idx + phrase.length });
      fromIdx = idx + phrase.length;
    }
  }

  // ALL-CAPS words (len >= 3), formatting anomaly
  const capsWords = [...text.matchAll(/\b[A-Z]{3,}\b/g)]
    .filter(m => !['USA','USB','LED','TV'].includes(m[0]))
    .map(m => ({ word: m[0], start: m.index, end: m.index + m[0].length }));

  const exclamCount = (text.match(/!/g) || []).length;
  const wordCount = words.length || 1;
  const exclamPer100 = (exclamCount / wordCount) * 100;

  const uniqueExaggPhrases = new Set(exaggerationHits.map(h => h.phrase)).size;

  let score = 0;
  score += repeatedPhrases.length * 14;
  score += uniqueExaggPhrases * 9;
  if(capsWords.length >= 2) score += 10;
  if(exclamPer100 >= 3) score += 15;
  if(wordCount < 12 && (repeatedPhrases.length || uniqueExaggPhrases)) score += 8;
  score = Math.max(0, Math.min(100, Math.round(score)));

  return { repeatedPhrases, exaggerationHits, capsWords, exclamCount, exclamPer100, wordCount, score };
}

function renderScanPanel(scan){
  const items = [
    { label: 'Repeated phrases', n: scan.repeatedPhrases.length },
    { label: 'Exaggerated phrases', n: new Set(scan.exaggerationHits.map(h=>h.phrase)).size },
    { label: 'ALL-CAPS words', n: scan.capsWords.length },
    { label: 'Exclamation marks', n: scan.exclamCount },
  ];
  scanGrid.innerHTML = items.map(it => {
    const flagged = it.n > 0;
    return `<div class="scan-item ${flagged ? 'flagged' : 'clear'}"><span class="n">${it.n}</span><span>${it.label}</span></div>`;
  }).join('');
}

/* ---------- Rendering ---------- */
function renderExhibit(rawText, ranges){
  ranges.sort((a,b) => a.start - b.start);
  const clean = [];
  let lastEnd = -1;
  for(const r of ranges){
    if(r.start >= lastEnd){
      clean.push(r);
      lastEnd = r.end;
    }
  }
  let html = '';
  let pos = 0;
  for(const r of clean){
    html += escapeHtml(rawText.slice(pos, r.start));
    html += `<mark class="${r.category}" title="${escapeHtml(r.note)}">${escapeHtml(rawText.slice(r.start, r.end))}</mark>`;
    pos = r.end;
  }
  html += escapeHtml(rawText.slice(pos));
  exhibitText.innerHTML = html;
}

function buildLocalRanges(scan){
  const ranges = [];
  for(const rp of scan.repeatedPhrases){
    for(const occ of rp.occurrences){
      ranges.push({ start: occ.start, end: occ.end, category: 'repeated_phrase', note: `Repeated phrase — appears ${rp.occurrences.length}× in this review`, source: 'pattern' });
    }
  }
  for(const hit of scan.exaggerationHits){
    ranges.push({ start: hit.start, end: hit.end, category: 'exaggeration', note: 'Exaggerated / hyperbolic language', source: 'pattern' });
  }
  return ranges;
}

function buildAiRanges(rawText, flags){
  const ranges = [];
  for(const flag of flags){
    if(!flag.quote) continue;
    const idx = rawText.indexOf(flag.quote);
    if(idx === -1) continue;
    const cat = ['generic_praise','unnatural_phrasing','incentivized','excessive_detail'].includes(flag.category) ? flag.category : 'other';
    ranges.push({ start: idx, end: idx + flag.quote.length, category: cat, note: flag.note || '', source: 'ai' });
  }
  return ranges;
}

function renderNotes(localRanges, aiFlags){
  const catNames = {
    generic_praise: 'Generic praise', unnatural_phrasing: 'Unnatural phrasing',
    incentivized: 'Incentivized', excessive_detail: 'Excessive detail', other: 'Note',
    repeated_phrase: 'Repeated phrase', exaggeration: 'Exaggeration'
  };
  let items = [];
  // dedupe repeated-phrase notes (one line per unique phrase, not per occurrence)
  const seenPhrase = new Set();
  for(const r of localRanges){
    const key = r.category + '|' + r.note;
    if(seenPhrase.has(key)) continue;
    seenPhrase.add(key);
    items.push({ cat: r.category, note: r.note });
  }
  for(const f of aiFlags){
    if(!f.note) continue;
    items.push({ cat: catNames[f.category] ? f.category : 'other', note: f.note });
  }
  if(!items.length){ notesEl.innerHTML = ''; return; }
  let html = '<h3>Evidence notes</h3><ul>';
  for(const it of items){
    html += `<li><span class="cat-tag">${catNames[it.cat] || 'Note'}</span>${escapeHtml(it.note)}</li>`;
  }
  html += '</ul>';
  notesEl.innerHTML = html;
}

function setStamp(pct, label){
  let stampColor = 'var(--teal)';
  if(pct >= 66) stampColor = 'var(--coral)';
  else if(pct >= 34) stampColor = 'var(--amber)';
  stamp.style.setProperty('--stamp-color', stampColor);
  stamp.style.animation = 'none';
  void stamp.offsetWidth;
  stamp.style.animation = '';
  stampPct.textContent = pct + '%';
  stampLabel.textContent = label;
}

const loadingMessages = [
  'Dusting for prints...',
  'Scanning for repeated phrasing...',
  'Cross-checking against known patterns...',
  'Compiling the case file...'
];

function runLoadingMessages(){
  let i = 0;
  statusLine.textContent = loadingMessages[0];
  return setInterval(() => {
    i = (i + 1) % loadingMessages.length;
    statusLine.textContent = loadingMessages[i];
  }, 1300);
}

async function analyze(){
  const text = textarea.value.trim();
  if(!text){
    statusLine.textContent = '';
    errorBox.style.display = 'block';
    errorBox.textContent = 'Paste a review before running the analysis.';
    return;
  }

  errorBox.style.display = 'none';
  results.classList.remove('show');
  analyzeBtn.disabled = true;

  // Step 1: deterministic local scan, always runs, always available
  const scan = localScan(text);
  renderScanPanel(scan);
  const localRanges = buildLocalRanges(scan);

  const loadingHandle = runLoadingMessages();

  const systemPrompt = `You are a forensic analyst evaluating whether an online review (from Amazon, Google, Yelp, or similar) shows signs of being fake, AI-generated, incentivized, or otherwise inauthentic.

Respond with ONLY a raw JSON object, no markdown fences, no preamble. Schema:

{
  "fake_percentage": <integer 0-100>,
  "verdict": "<short 2-4 word label>",
  "summary": "<1-2 sentence plain-English rationale>",
  "flags": [
    {
      "quote": "<exact verbatim substring from the review, no more than ~12 words>",
      "category": "<one of: generic_praise, unnatural_phrasing, incentivized, excessive_detail, other>",
      "note": "<short reason, under 15 words>"
    }
  ]
}

Rules:
- "quote" MUST be an exact substring of the review text (same casing/punctuation).
- Include 0-6 flags, only for genuinely notable phrases beyond simple repetition or generic hype (a separate pattern scan already covers repeated phrases and stock hyperbole, so focus on contextual signals: implausible specificity, incentive/disclosure language, tone mismatches, unnatural structure).
- Be calibrated — most real reviews are genuine. Don't over-flag normal enthusiastic writing.`;

  try{
    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 1000,
        system: systemPrompt,
        messages: [ { role: "user", content: text } ]
      })
    });

    if(!response.ok) throw new Error('Request failed with status ' + response.status);

    const data = await response.json();
    const textBlock = (data.content || []).map(b => b.text || '').join('\n').trim();
    const cleaned = textBlock.replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/```\s*$/i, '').trim();

    let parsed;
    try{ parsed = JSON.parse(cleaned); }
    catch(e){ throw new Error('Could not parse analysis result.'); }

    const aiPct = Math.max(0, Math.min(100, Math.round(Number(parsed.fake_percentage) || 0)));
    const verdict = parsed.verdict || (aiPct >= 50 ? 'Likely Fake' : 'Likely Genuine');
    const aiFlags = Array.isArray(parsed.flags) ? parsed.flags : [];

    // Blend: AI judgment is primary, nudged by the deterministic pattern score
    const blended = Math.round(aiPct * 0.75 + scan.score * 0.25);
    const finalPct = Math.max(0, Math.min(100, blended));

    setStamp(finalPct, verdict);
    summaryText.textContent = parsed.summary || '';

    const aiRanges = buildAiRanges(text, aiFlags);
    renderExhibit(text, [...localRanges, ...aiRanges]);
    renderNotes(localRanges, aiFlags);

    results.classList.add('show');
    statusLine.textContent = 'Analysis complete.';
  } catch(err){
    // Fall back to pattern-scan-only result so the tool still works without the API
    setStamp(scan.score, 'Pattern-based estimate');
    const reasons = [];
    if(scan.repeatedPhrases.length) reasons.push(`${scan.repeatedPhrases.length} repeated phrase(s)`);
    const uniqExagg = new Set(scan.exaggerationHits.map(h=>h.phrase)).size;
    if(uniqExagg) reasons.push(`${uniqExagg} exaggerated phrase(s)`);
    if(scan.capsWords.length >= 2) reasons.push('unusual ALL-CAPS usage');
    if(scan.exclamPer100 >= 3) reasons.push('heavy exclamation-mark usage');
    summaryText.textContent = reasons.length
      ? `Deep AI analysis unavailable — estimate based on ${reasons.join(', ')}.`
      : 'Deep AI analysis unavailable — pattern scan found no strong red flags.';

    renderExhibit(text, localRanges);
    renderNotes(localRanges, []);

    results.classList.add('show');
    errorBox.style.display = 'block';
    errorBox.textContent = 'AI analysis unavailable (' + err.message + '). Showing pattern-scan-only results.';
    statusLine.textContent = '';
  } finally {
    clearInterval(loadingHandle);
    analyzeBtn.disabled = false;
  }
}

analyzeBtn.addEventListener('click', analyze);
</script>

</body>
</html>