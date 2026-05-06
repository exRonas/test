import json

with open('questions1_fixed.json', 'r', encoding='utf-8') as f:
    q1 = json.load(f)
with open('questions2_fixed.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)

q1_js = json.dumps(q1, ensure_ascii=False)
q2_js = json.dumps(q2, ensure_ascii=False)

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: "Google Sans", Roboto, Arial, sans-serif;
  background: #f0ebf8;
  min-height: 100vh;
  color: #202124;
}

/* ===== MENU ===== */
#menu-screen {
  max-width: 700px;
  margin: 0 auto;
  padding: 28px 16px 48px;
}

.menu-banner {
  background: linear-gradient(135deg, #5e35b1 0%, #8e24aa 100%);
  border-radius: 12px 12px 0 0;
  padding: 36px 28px 24px;
  color: white;
}

.menu-banner h1 { font-size: 28px; font-weight: 400; margin-bottom: 8px; }
.menu-banner p { font-size: 14px; opacity: 0.82; }

.menu-card {
  background: white;
  border-radius: 0 0 12px 12px;
  padding-bottom: 12px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.14);
  margin-bottom: 16px;
}

.test-section { padding: 0; }

.test-section-header {
  padding: 22px 28px 10px;
}

.test-section-header h2 {
  font-size: 17px;
  font-weight: 500;
  color: #1a73e8;
  margin-bottom: 3px;
}

.test-section-header p {
  font-size: 13px;
  color: #5f6368;
}

.divider { height: 1px; background: #f1f3f4; margin: 0 28px; }

.btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 8px 20px 14px;
}

.sub-btn {
  padding: 9px 18px;
  border: 1.5px solid #c5cae9;
  border-radius: 20px;
  background: white;
  color: #5e35b1;
  font-size: 14px;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.15s;
  white-space: nowrap;
}

.sub-btn:hover { background: #ede7f6; border-color: #5e35b1; }

.sub-btn.all-btn {
  background: #5e35b1;
  color: white;
  border-color: #5e35b1;
  font-weight: 500;
}

.sub-btn.all-btn:hover { background: #4527a0; border-color: #4527a0; }

/* ===== QUIZ ===== */
#quiz-screen { display: none; }

.sticky-header {
  position: sticky;
  top: 0;
  z-index: 200;
  background: #5e35b1;
  box-shadow: 0 2px 8px rgba(0,0,0,0.22);
}

.top-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px 10px;
  color: white;
}

.back-btn {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 50%;
  line-height: 1;
  transition: background 0.15s;
  flex-shrink: 0;
}
.back-btn:hover { background: rgba(255,255,255,0.18); }

.top-info { flex: 1; min-width: 0; }
.top-info h2 {
  font-size: 15px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 2px;
}
.top-info span { font-size: 12px; opacity: 0.8; }

.prog-track { height: 4px; background: rgba(255,255,255,0.28); }
.prog-fill { height: 100%; background: #ffeb3b; transition: width 0.35s ease; }

.qlist {
  max-width: 720px;
  margin: 0 auto;
  padding: 18px 16px 8px;
}

.q-card {
  background: white;
  border-radius: 10px;
  padding: 22px 22px 16px;
  margin-bottom: 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-left: 4px solid #e0e0e0;
  transition: border-color 0.2s;
}

.q-card.done { border-left-color: #5e35b1; }

.q-num { font-size: 12px; color: #80868b; margin-bottom: 8px; }
.q-text { font-size: 15px; line-height: 1.55; margin-bottom: 14px; }

.opt-label {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 9px 10px;
  border-radius: 7px;
  cursor: pointer;
  margin-bottom: 2px;
  transition: background 0.12s;
}
.opt-label:hover { background: #f5f5f5; }

.opt-label input[type=radio] {
  width: 18px;
  height: 18px;
  margin-top: 1px;
  flex-shrink: 0;
  accent-color: #5e35b1;
  cursor: pointer;
}

.opt-text { font-size: 14px; line-height: 1.45; color: #3c4043; }

.submit-row {
  max-width: 720px;
  margin: 0 auto;
  padding: 12px 16px 40px;
  display: flex;
  justify-content: flex-end;
}

.submit-btn {
  background: #5e35b1;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 24px;
  font-size: 15px;
  font-family: inherit;
  font-weight: 500;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(94,53,177,0.4);
  transition: all 0.15s;
}
.submit-btn:hover { background: #4527a0; box-shadow: 0 4px 12px rgba(94,53,177,0.45); }

/* ===== RESULTS ===== */
#result-screen { display: none; }

.res-header {
  background: linear-gradient(135deg, #5e35b1 0%, #8e24aa 100%);
  color: white;
  padding: 28px 20px 24px;
  text-align: center;
  box-shadow: 0 3px 8px rgba(94,53,177,0.35);
}

.res-header h2 { font-size: 18px; font-weight: 400; margin-bottom: 14px; }

.big-score {
  font-size: 60px;
  font-weight: 300;
  line-height: 1;
  margin-bottom: 6px;
}

.score-sub { font-size: 14px; opacity: 0.85; margin-bottom: 16px; }

.score-track { height: 8px; background: rgba(255,255,255,0.28); border-radius: 4px; overflow: hidden; margin-bottom: 18px; }
.score-fill { height: 100%; background: #ffeb3b; border-radius: 4px; transition: width 0.7s ease; }

.res-actions { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }

.res-btn {
  padding: 10px 22px;
  border-radius: 20px;
  border: 2px solid rgba(255,255,255,0.65);
  background: transparent;
  color: white;
  font-size: 14px;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s;
}
.res-btn:hover { background: rgba(255,255,255,0.18); }
.res-btn.solid { background: rgba(255,255,255,0.22); border-color: white; }
.res-btn.solid:hover { background: rgba(255,255,255,0.32); }

.res-list {
  max-width: 720px;
  margin: 0 auto;
  padding: 16px 16px 48px;
}

.res-card {
  background: white;
  border-radius: 10px;
  padding: 18px 22px;
  margin-bottom: 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.res-card.ok { border-left: 4px solid #0f9d58; }
.res-card.bad { border-left: 4px solid #d93025; }

.res-qnum { font-size: 12px; color: #80868b; margin-bottom: 5px; }
.res-qtext { font-size: 14px; line-height: 1.5; margin-bottom: 10px; color: #202124; }

.ans-row {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 6px 10px;
  border-radius: 6px;
  margin-bottom: 4px;
  font-size: 13.5px;
  line-height: 1.4;
}
.ans-row.ok-ans { background: #e6f4ea; color: #137333; }
.ans-row.bad-ans { background: #fce8e6; color: #c5221f; }
.ans-row.correct-hint { background: #e6f4ea; color: #137333; }

.ans-icon { flex-shrink: 0; font-weight: bold; min-width: 16px; }

/* Result options */
.res-options {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-top: 8px;
}

.res-option {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 6px;
  font-size: 13.5px;
  line-height: 1.4;
  background: #f5f5f5;
  color: #3c4043;
}

.res-option.correct {
  background: #e6f4ea;
  color: #137333;
}

.res-option.wrong {
  background: #fce8e6;
  color: #c5221f;
}

.res-opt-icon {
  flex-shrink: 0;
  font-weight: bold;
  min-width: 16px;
}

/* ===== ANSWERS ===== */
#answers-screen { display: none; }

.answers-top {
  background: #5e35b1;
  color: white;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  position: sticky;
  top: 0;
  z-index: 200;
  box-shadow: 0 2px 8px rgba(0,0,0,0.22);
}

.answers-top button {
  background: none;
  border: none;
  color: white;
  font-size: 22px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 50%;
  line-height: 1;
  flex-shrink: 0;
  transition: background 0.15s;
}

.answers-top button:hover { background: rgba(255,255,255,0.18); }

.search-box {
  flex: 1;
  display: flex;
  align-items: center;
  background: rgba(255,255,255,0.15);
  border-radius: 20px;
  padding: 0 12px;
  height: 36px;
}

.search-box input {
  background: none;
  border: none;
  color: white;
  font-size: 14px;
  font-family: inherit;
  outline: none;
  width: 100%;
  padding: 0;
}

.search-box input::placeholder { color: rgba(255,255,255,0.6); }

.search-box input::-webkit-input-placeholder { color: rgba(255,255,255,0.6); }

.answers-container {
  max-width: 720px;
  margin: 0 auto;
  padding: 14px 12px 40px;
}

.answer-card {
  background: white;
  border-radius: 10px;
  padding: 14px 16px;
  margin-bottom: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-left: 4px solid #5e35b1;
}

.answer-test {
  font-size: 11px;
  color: #5e35b1;
  font-weight: 600;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.answer-num {
  font-size: 12px;
  color: #80868b;
  margin-bottom: 6px;
}

.answer-q {
  font-size: 14px;
  line-height: 1.45;
  color: #202124;
  margin-bottom: 8px;
  font-weight: 500;
}

.answer-a {
  font-size: 13.5px;
  line-height: 1.4;
  color: #137333;
  background: #e6f4ea;
  padding: 8px 10px;
  border-radius: 6px;
}

@media (max-width: 600px) {
  #menu-screen { padding: 12px 10px 40px; }
  .menu-banner { padding: 24px 18px 18px; }
  .menu-banner h1 { font-size: 22px; }
  .test-section-header { padding: 16px 18px 8px; }
  .btn-row { padding: 6px 14px 10px; }
  .q-card { padding: 18px 16px 12px; }
  .big-score { font-size: 46px; }
  .res-header { padding: 22px 14px 18px; }
  .top-info h2 { font-size: 13.5px; }
}
"""

JS = """
const T1 = Q1DATA;
const T2 = Q2DATA;

const TESTS = [
  { name: 'Инклюзивное образование', questions: T1, color: '#5e35b1' },
  { name: 'Основы НИД и академическое письмо', questions: T2, color: '#7e57c2' }
];

let curTest, curSub, qList, varList, answers, allAnswersData = [];

function buildMenu() {
  // Построить все ответы для справочника
  allAnswersData = [];
  TESTS.forEach((t, ti) => {
    t.questions.forEach((q, qi) => {
      allAnswersData.push({
        testIdx: ti,
        testName: t.name,
        qNum: qi + 1,
        question: q.question,
        answer: q.variants[0]
      });
    });
  });

  TESTS.forEach((t, ti) => {
    const row = document.getElementById('row-' + ti);
    const n = t.questions.length;
    const subs = Math.ceil(n / 20);
    for (let s = 0; s < subs; s++) {
      const a = s * 20 + 1, b = Math.min((s + 1) * 20, n);
      const btn = document.createElement('button');
      btn.className = 'sub-btn';
      btn.textContent = a + '–' + b;
      btn.onclick = () => startQuiz(ti, s);
      row.appendChild(btn);
    }
    const all = document.createElement('button');
    all.className = 'sub-btn all-btn';
    all.textContent = 'Все вопросы (' + n + ')';
    all.onclick = () => startQuiz(ti, -1);
    row.appendChild(all);
  });
}

function shuffle(a) {
  const b = [...a];
  for (let i = b.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [b[i], b[j]] = [b[j], b[i]];
  }
  return b;
}

function startQuiz(ti, si) {
  curTest = ti; curSub = si;
  const t = TESTS[ti];
  let pool = si === -1 ? [...t.questions] : t.questions.slice(si * 20, Math.min((si + 1) * 20, t.questions.length));
  qList = shuffle(pool);
  varList = qList.map(q => shuffle(q.variants.map((v, i) => ({ text: v, correct: i === 0 }))));
  answers = new Array(qList.length).fill(null);

  document.getElementById('quiz-title').textContent = t.name;
  renderQ();
  show('quiz-screen');
  window.scrollTo(0, 0);
}

function renderQ() {
  const n = qList.length;
  const si = curSub;
  const t = TESTS[curTest];
  const range = si === -1 ? 'Все вопросы' : (si * 20 + 1) + '–' + Math.min((si + 1) * 20, t.questions.length);
  document.getElementById('prog-text').textContent = range + ' · ' + n + ' вопросов';
  document.getElementById('prog-fill').style.width = '0%';

  const cnt = document.getElementById('qlist');
  cnt.innerHTML = '';

  qList.forEach((q, qi) => {
    const card = document.createElement('div');
    card.className = 'q-card';
    card.id = 'c' + qi;

    const num = document.createElement('div');
    num.className = 'q-num';
    num.textContent = 'Вопрос ' + (qi + 1) + ' из ' + n;

    const txt = document.createElement('div');
    txt.className = 'q-text';
    txt.textContent = q.question;

    card.appendChild(num);
    card.appendChild(txt);

    varList[qi].forEach((v, vi) => {
      const lbl = document.createElement('label');
      lbl.className = 'opt-label';
      lbl.htmlFor = 'r' + qi + '_' + vi;

      const radio = document.createElement('input');
      radio.type = 'radio';
      radio.name = 'q' + qi;
      radio.id = 'r' + qi + '_' + vi;
      radio.value = vi;
      radio.onchange = () => onPick(qi, vi);

      const sp = document.createElement('span');
      sp.className = 'opt-text';
      sp.textContent = v.text;

      lbl.appendChild(radio);
      lbl.appendChild(sp);
      card.appendChild(lbl);
    });

    cnt.appendChild(card);
  });
}

function onPick(qi, vi) {
  answers[qi] = vi;
  document.getElementById('c' + qi).classList.add('done');
  const done = answers.filter(a => a !== null).length;
  document.getElementById('prog-fill').style.width = Math.round(done / qList.length * 100) + '%';
  const si = curSub, t = TESTS[curTest];
  const range = si === -1 ? 'Все вопросы' : (si * 20 + 1) + '–' + Math.min((si + 1) * 20, t.questions.length);
  document.getElementById('prog-text').textContent = range + ' · Отвечено ' + done + '/' + qList.length;
}

function submitQuiz() {
  const skip = answers.filter(a => a === null).length;
  if (skip && !confirm('Пропущено вопросов: ' + skip + '. Отправить всё равно?')) return;

  let ok = 0;
  const data = qList.map((q, qi) => {
    const ui = answers[qi];
    const correct = ui !== null && varList[qi][ui].correct;
    if (correct) ok++;
    return {
      question: q.question,
      correct,
      userAns: ui !== null ? varList[qi][ui].text : null,
      rightAns: varList[qi].find(v => v.correct).text,
      allVariants: varList[qi]
    };
  });

  showResults(data, ok, qList.length);
}

function showResults(data, ok, total) {
  const pct = Math.round(ok / total * 100);
  document.getElementById('res-title').textContent = TESTS[curTest].name;
  document.getElementById('big-pct').textContent = pct;
  document.getElementById('score-ok').textContent = ok;
  document.getElementById('score-tot').textContent = total;

  const list = document.getElementById('res-list');
  list.innerHTML = '';

  data.forEach((d, i) => {
    const card = document.createElement('div');
    card.className = 'res-card ' + (d.correct ? 'ok' : 'bad');

    const qn = document.createElement('div');
    qn.className = 'res-qnum';
    qn.textContent = 'Вопрос ' + (i + 1);

    const qt = document.createElement('div');
    qt.className = 'res-qtext';
    qt.textContent = d.question;

    card.appendChild(qn);
    card.appendChild(qt);

    // Показываем все варианты ответов
    const opts = document.createElement('div');
    opts.className = 'res-options';
    d.allVariants.forEach(v => {
      const opt = document.createElement('div');
      let cls = 'res-option';
      let icon = '○';

      if (v.text === d.rightAns) {
        cls += ' correct';
        icon = '✓';
      } else if (v.text === d.userAns) {
        cls += ' wrong';
        icon = '✗';
      }

      opt.className = cls;
      opt.innerHTML = '<span class="res-opt-icon">' + icon + '</span><span>' + v.text + '</span>';
      opts.appendChild(opt);
    });
    card.appendChild(opts);

    list.appendChild(card);
  });

  show('result-screen');
  window.scrollTo(0, 0);
  setTimeout(() => { document.getElementById('score-fill').style.width = pct + '%'; }, 80);
}

function retake() { startQuiz(curTest, curSub); }
function goMenu() { show('menu-screen'); window.scrollTo(0, 0); }

function showAnswers() {
  const list = document.getElementById('answers-list');
  list.innerHTML = '';
  allAnswersData.forEach(item => {
    const card = document.createElement('div');
    card.className = 'answer-card';
    card.innerHTML = `
      <div class="answer-test">${item.testName}</div>
      <div class="answer-num">Вопрос ${item.qNum}</div>
      <div class="answer-q">${item.question}</div>
      <div class="answer-a">✓ ${item.answer}</div>
    `;
    list.appendChild(card);
  });
  document.getElementById('search-input').value = '';
  show('answers-screen');
  window.scrollTo(0, 0);
}

function searchAnswers() {
  const q = document.getElementById('search-input').value.toLowerCase();
  const list = document.getElementById('answers-list');
  const cards = list.querySelectorAll('.answer-card');

  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(q) ? 'block' : 'none';
  });
}

function show(id) {
  ['menu-screen', 'quiz-screen', 'result-screen', 'answers-screen'].forEach(s => {
    document.getElementById(s).style.display = s === id ? 'block' : 'none';
  });
}

buildMenu();
""".replace('Q1DATA', q1_js).replace('Q2DATA', q2_js)

HTML = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Тесты — Инклюзивное образование и НИД</title>
<style>{CSS}</style>
</head>
<body>

<!-- MENU -->
<div id="menu-screen">
  <div class="menu-banner">
    <h1>Тесты</h1>
    <p>Выберите тест и раздел &nbsp;·&nbsp; Вопросы перемешиваются при каждом запуске</p>
  </div>
  <div style="max-width: 700px; margin: 0 auto; padding: 0 16px 12px;">
    <button onclick="showAnswers()" style="width: 100%; padding: 14px; background: linear-gradient(135deg, #1a73e8 0%, #1557b0 100%); color: white; border: none; border-radius: 10px; font-size: 15px; font-family: inherit; font-weight: 500; cursor: pointer; box-shadow: 0 2px 6px rgba(26,115,232,0.4); transition: all 0.15s;">📖 Справочник ответов (поиск)</button>
  </div>
  <div class="menu-card">
    <div class="test-section">
      <div class="test-section-header">
        <h2>Тест 1 — Инклюзивное образование</h2>
        <p>117 вопросов &nbsp;·&nbsp; 6 разделов по 20 вопросов</p>
      </div>
      <div class="btn-row" id="row-0"></div>
    </div>
    <div class="divider"></div>
    <div class="test-section">
      <div class="test-section-header">
        <h2>Тест 2 — Основы НИД и академическое письмо</h2>
        <p>120 вопросов &nbsp;·&nbsp; 6 разделов по 20 вопросов</p>
      </div>
      <div class="btn-row" id="row-1"></div>
    </div>
  </div>
</div>

<!-- QUIZ -->
<div id="quiz-screen">
  <div class="sticky-header">
    <div class="top-row">
      <button class="back-btn" onclick="goMenu()">&#8592;</button>
      <div class="top-info">
        <h2 id="quiz-title"></h2>
        <span id="prog-text"></span>
      </div>
    </div>
    <div class="prog-track">
      <div class="prog-fill" id="prog-fill"></div>
    </div>
  </div>
  <div class="qlist" id="qlist"></div>
  <div class="submit-row">
    <button class="submit-btn" onclick="submitQuiz()">Отправить</button>
  </div>
</div>

<!-- RESULTS -->
<div id="result-screen">
  <div class="res-header">
    <h2 id="res-title"></h2>
    <div class="big-score"><span id="big-pct"></span>%</div>
    <div class="score-sub"><span id="score-ok"></span> из <span id="score-tot"></span> правильно</div>
    <div class="score-track">
      <div class="score-fill" id="score-fill"></div>
    </div>
    <div class="res-actions">
      <button class="res-btn" onclick="retake()">&#8635;&nbsp;Пройти снова</button>
      <button class="res-btn solid" onclick="goMenu()">&#8592;&nbsp;К списку тестов</button>
    </div>
  </div>
  <div class="res-list" id="res-list"></div>
</div>

<!-- ANSWERS -->
<div id="answers-screen">
  <div class="answers-top">
    <button onclick="goMenu()" title="Назад">&#8592;</button>
    <div class="search-box">
      <input type="text" id="search-input" placeholder="Поиск по вопросам..." oninput="searchAnswers()">
    </div>
  </div>
  <div class="answers-container" id="answers-list"></div>
</div>

<script>{JS}</script>
</body>
</html>"""

with open('quiz.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'quiz.html created: {len(HTML):,} bytes')
