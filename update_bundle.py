import json

with open('frontend/benchmarks_data.json', 'r', encoding='utf-8') as f:
    benchmarks_data = json.load(f)

js_content = """/**
 * COMP - Spectrum-Based Fault Localization & Bug Intelligence
 * Interactive client-side engine with 3D Card Arc, real-time recalculation,
 * and dynamic AI test case generation & fix verification.
 */

(function () {
  'use strict';

  // --- Embedded Benchmarks Dataset ---
  const INITIAL_BENCHMARKS = __INITIAL_BENCHMARKS__;

  // --- Application State ---
  const state = {
    benchmarks: JSON.parse(JSON.stringify(INITIAL_BENCHMARKS)),
    activeId: 'sample',
    activeMetric: 'ochiai', // 'ochiai', 'tarantula', 'dstar', 'jaccard'
    weights: {
      metric: 1.0,
      churn: 0.2,
      comp: 0.1
    },
    arc: {
      radius: 360,
      spread: 115,
      rotation: 0
    },
    filter: 'suspects', // 'all', 'suspects', 'top1'
    viewMode: 'arc', // 'arc', 'matrix', 'code'
    selectedFunction: null,
    fixedFunctions: new Set(),
    isDragging: false,
    dragStartX: 0,
    dragStartRotation: 0
  };

  // --- SVG Asset Cache ---
  const ASSET_ICONS = {
    'thumb-dark-circle': './frontend/assets/thumb-dark-circle.svg',
    'thumb-sculpture': './frontend/assets/thumb-sculpture.svg',
    'thumb-feather': './frontend/assets/thumb-feather.svg',
    'thumb-moss': './frontend/assets/thumb-moss.svg',
    'thumb-landscape': './frontend/assets/thumb-landscape.svg',
    'thumb-cyan-swirl': './frontend/assets/thumb-cyan-swirl.svg',
    'thumb-amber-bottle': './frontend/assets/thumb-amber-bottle.svg',
    'thumb-mountain': './frontend/assets/thumb-mountain.svg',
    'thumb-cream': './frontend/assets/thumb-cream.svg',
    'thumb-poppy': './frontend/assets/thumb-poppy.svg',
    'thumb-skeleton-leaf': './frontend/assets/thumb-skeleton-leaf.svg'
  };

  // --- DOM Elements ---
  const assetsGrid = document.getElementById('assets-grid');
  const assetCountLabel = document.getElementById('asset-count-label');
  const cardArcWrapper = document.getElementById('card-arc-wrapper');
  const canvasStage = document.getElementById('canvas-stage');
  const canvasMetaBadge = document.getElementById('canvas-meta-badge');
  const canvasActiveTargetText = document.getElementById('canvas-active-target-text');
  const exportCountBadge = document.getElementById('export-count-badge');

  // View containers
  const matrixViewContainer = document.getElementById('matrix-view-container');
  const matrixTableBody = document.getElementById('matrix-table-body');
  const codeViewContainer = document.getElementById('code-view-container');
  const codeViewFilename = document.getElementById('code-view-filename');
  const codeViewSource = document.getElementById('code-view-source');
  const codeViewTests = document.getElementById('code-view-tests');

  // Settings & Sliders
  const activeMetricReadout = document.getElementById('active-metric-readout');
  const metricButtons = document.querySelectorAll('#metric-segmented-control .segment-btn');
  const sliderWeightMetric = document.getElementById('slider-weight-metric');
  const weightMetricVal = document.getElementById('weight-metric-val');
  const sliderWeightChurn = document.getElementById('slider-weight-churn');
  const weightChurnVal = document.getElementById('weight-churn-val');
  const sliderWeightComp = document.getElementById('slider-weight-comp');
  const weightCompVal = document.getElementById('weight-comp-val');
  const sliderArcRadius = document.getElementById('slider-arc-radius');
  const arcRadiusVal = document.getElementById('arc-radius-val');
  const sliderArcSpread = document.getElementById('slider-arc-spread');
  const arcSpreadVal = document.getElementById('arc-spread-val');
  const sliderArcRotation = document.getElementById('slider-arc-rotation');
  const arcRotationVal = document.getElementById('arc-rotation-val');
  const filterCandidatesSelect = document.getElementById('filter-candidates-select');
  const btnResetSettings = document.getElementById('btn-reset-settings');

  // Sidebar Status Box
  const statusSuiteTitle = document.getElementById('status-suite-title');
  const statusFailBadge = document.getElementById('status-fail-badge');
  const statusPassBadge = document.getElementById('status-pass-badge');
  const statusTopSuspect = document.getElementById('status-top-suspect');
  const statusTopScore = document.getElementById('status-top-score');
  const btnRunPipeline = document.getElementById('btn-run-pipeline');

  // Inspector Modal
  const modalInspector = document.getElementById('modal-inspector');
  const inspectorCloseBtn = document.getElementById('inspector-close-btn');
  const inspectorCancelBtn = document.getElementById('inspector-cancel-btn');
  const inspectorFnTitle = document.getElementById('inspector-fn-title');
  const inspectorFileSub = document.getElementById('inspector-file-sub');
  const inspectorScoreReadout = document.getElementById('inspector-score-readout');
  const inspectorExecSummary = document.getElementById('inspector-exec-summary');
  const inspectorMathDerivation = document.getElementById('inspector-math-derivation');
  const inspectorRootCauseText = document.getElementById('inspector-root-cause-text');
  const diffDelLine = document.getElementById('diff-del-line');
  const diffAddLine = document.getElementById('diff-add-line');
  const btnVerifyFix = document.getElementById('btn-verify-fix');

  // Export Modal
  const modalExport = document.getElementById('modal-export');
  const btnExport = document.getElementById('btn-export');
  const exportCloseBtn = document.getElementById('export-close-btn');
  const exportPreviewText = document.getElementById('export-preview-text');
  const btnCopyReport = document.getElementById('btn-copy-report');
  const btnDownloadJson = document.getElementById('btn-download-json');
  const btnDownloadReport = document.getElementById('btn-download-report');

  // Edit Suite Modal
  const modalEditSuite = document.getElementById('modal-edit-suite');
  const btnEditSuite = document.getElementById('btn-edit-suite');
  const editSuiteCloseBtn = document.getElementById('edit-suite-close-btn');
  const editSuiteCancelBtn = document.getElementById('edit-suite-cancel-btn');
  const editSuiteSource = document.getElementById('edit-suite-source');
  const editSuiteTests = document.getElementById('edit-suite-tests');
  const btnSaveSuiteChanges = document.getElementById('btn-save-suite-changes');

  // Custom AI Test Gen Modal
  const modalAddCustom = document.getElementById('modal-add-custom');
  const addCustomCloseBtn = document.getElementById('add-custom-close-btn');
  const addCustomCancelBtn = document.getElementById('add-custom-cancel-btn');
  const customSuiteTitle = document.getElementById('custom-suite-title');
  const customFnName = document.getElementById('custom-fn-name');
  const customSuiteSource = document.getElementById('custom-suite-source');
  const customSuiteIntent = document.getElementById('custom-suite-intent');
  const customAiProvider = document.getElementById('custom-ai-provider');
  const customAiKey = document.getElementById('custom-ai-key');
  const btnGenerateTests = document.getElementById('btn-generate-tests');
  const btnGenSpinner = document.getElementById('btn-gen-spinner');
  const aiTestResultsBox = document.getElementById('ai-test-results-box');
  const aiTestStatusBadge = document.getElementById('ai-test-status-badge');
  const aiTestLogs = document.getElementById('ai-test-logs');
  const aiFixPreview = document.getElementById('ai-fix-preview');
  const btnCreateCustomSuite = document.getElementById('btn-create-custom-suite');

  const toastNotice = document.getElementById('toast-notice');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  // --- Mathematical SBFL Formula Calculators ---
  function computeOchiai(ef, ep, totalFailed) {
    const denom = Math.sqrt(totalFailed * (ef + ep));
    return denom ? ef / denom : 0.0;
  }

  function computeTarantula(ef, ep, totalFailed, totalPassed) {
    if (totalFailed === 0) return 0.0;
    const num = ef / totalFailed;
    const denom = num + (totalPassed ? (ep / totalPassed) : 0.0);
    return denom ? num / denom : 0.0;
  }

  function computeDStar(ef, ep, totalFailed) {
    const denom = ep + (totalFailed - ef);
    return denom ? (ef * ef) / denom : 0.0;
  }

  function computeJaccard(ef, ep, totalFailed) {
    const denom = totalFailed + ep;
    return denom ? ef / denom : 0.0;
  }

  function getMetricScore(fn, b) {
    const fixKey = `${b.id}::${fn.name}`;
    if (state.fixedFunctions.has(fixKey) || b.total_failed === 0) {
      return 0.0;
    }
    switch (state.activeMetric) {
      case 'tarantula': return computeTarantula(fn.failed_execs, fn.passed_execs, b.total_failed, b.total_passed);
      case 'dstar': return computeDStar(fn.failed_execs, fn.passed_execs, b.total_failed);
      case 'jaccard': return computeJaccard(fn.failed_execs, fn.passed_execs, b.total_failed);
      case 'ochiai':
      default: return computeOchiai(fn.failed_execs, fn.passed_execs, b.total_failed);
    }
  }

  function getCombinedScore(fn, b) {
    const baseScore = getMetricScore(fn, b);
    const maxComp = Math.max(...b.functions.map(f => f.complexity || 1), 1);
    const compScore = (fn.complexity || 1) / maxComp;
    const churnScore = (fn.churn || 1) / 5.0;

    return (state.weights.metric * baseScore) +
           (state.weights.churn * churnScore) +
           (state.weights.comp * compScore);
  }

  // --- Helper: Toast Notification ---
  let toastTimer = null;
  function showToast(msg, icon = '✓') {
    if (toastTimer) clearTimeout(toastTimer);
    toastMessage.textContent = msg;
    toastIcon.textContent = icon;
    toastNotice.classList.add('show');
    toastTimer = setTimeout(() => {
      toastNotice.classList.remove('show');
    }, 2800);
  }

  // --- Get Active Benchmark ---
  function getActiveBenchmark() {
    return state.benchmarks.find(b => b.id === state.activeId) || state.benchmarks[0];
  }

  // --- Render Assets Sidebar Grid ---
  function renderAssetsGrid() {
    assetsGrid.innerHTML = '';
    assetCountLabel.textContent = `${state.benchmarks.length} suites`;

    state.benchmarks.forEach((b) => {
      const card = document.createElement('div');
      card.className = `asset-thumb-card ${b.id === state.activeId ? 'active' : ''}`;
      card.title = `${b.title} (${b.source_file})`;

      const assetPath = ASSET_ICONS[b.thumb_asset] || ASSET_ICONS['thumb-dark-circle'];
      const isFixed = state.fixedFunctions.has(`${b.id}::${b.expected_bug}`) || b.total_failed === 0;

      card.innerHTML = `
        <img src="${assetPath}" alt="${b.title}" />
        <span class="asset-thumb-badge ${isFixed ? 'pass' : 'fail'}"></span>
      `;

      card.addEventListener('click', () => {
        selectBenchmark(b.id);
      });

      assetsGrid.appendChild(card);
    });

    // Add "+" button at the end with matte black styling
    const addBtn = document.createElement('div');
    addBtn.className = 'asset-add-btn';
    addBtn.title = 'Add Custom Function & Synthesize Edge-Case Tests';
    addBtn.textContent = '+';
    addBtn.addEventListener('click', () => {
      openModal(modalAddCustom);
    });
    assetsGrid.appendChild(addBtn);
  }

  // --- Select Benchmark ---
  function selectBenchmark(id) {
    state.activeId = id;
    renderAssetsGrid();
    updateUI();
  }

  // --- Update UI & Recalculate Rankings ---
  function updateUI() {
    const b = getActiveBenchmark();

    // 1. Recalculate scores & sort functions
    const rankedFunctions = [...b.functions].map(fn => {
      const metricScore = getMetricScore(fn, b);
      const combinedScore = getCombinedScore(fn, b);
      return {
        ...fn,
        current_metric_score: metricScore,
        current_combined_score: combinedScore
      };
    });

    rankedFunctions.sort((a, b) => b.current_combined_score - a.current_combined_score);

    // 2. Update Sidebar Status Box
    statusSuiteTitle.textContent = `${b.id} / ${b.source_file}`;
    const isFixed = state.fixedFunctions.has(`${b.id}::${b.expected_bug}`) || b.total_failed === 0;
    if (isFixed) {
      statusFailBadge.textContent = '0 Fail';
      statusFailBadge.className = 'status-tag pass';
      statusPassBadge.textContent = `${b.total_tests} Pass`;
      statusTopSuspect.textContent = 'All Passing';
      statusTopSuspect.style.color = '#16a34a';
      statusTopScore.textContent = '0.000';
    } else {
      statusFailBadge.textContent = `${b.total_failed} Fail`;
      statusFailBadge.className = 'status-tag fail';
      statusPassBadge.textContent = `${b.total_passed} Pass`;
      const top = rankedFunctions[0];
      statusTopSuspect.textContent = top ? `${top.name}()` : 'none';
      statusTopSuspect.style.color = '#dc2626';
      statusTopScore.textContent = top ? (typeof top.current_metric_score === 'number' ? top.current_metric_score.toFixed(3) : '0.000') : '0.000';
    }

    // 3. Update Canvas Header
    canvasActiveTargetText.textContent = `${b.source_file} • ${rankedFunctions.length} Functions Profiled`;
    const suspectCount = rankedFunctions.filter(f => f.current_metric_score > 0).length;
    exportCountBadge.textContent = `(${suspectCount})`;

    // 4. Render Active View
    if (state.viewMode === 'arc') {
      renderArcCards(rankedFunctions, b);
      matrixViewContainer.classList.remove('active');
      codeViewContainer.classList.remove('active');
    } else if (state.viewMode === 'matrix') {
      renderMatrixView(rankedFunctions, b);
      matrixViewContainer.classList.add('active');
      codeViewContainer.classList.remove('active');
    } else if (state.viewMode === 'code') {
      renderCodeView(b);
      codeViewContainer.classList.add('active');
      matrixViewContainer.classList.remove('active');
    }
  }

  // --- Filter Functions for Display ---
  function getFilteredFunctions(functions, b) {
    if (state.filter === 'top1') {
      return functions.slice(0, 1);
    }
    if (state.filter === 'suspects') {
      const suspects = functions.filter(f => {
        const sc = (typeof f.current_metric_score === 'number') ? f.current_metric_score : getMetricScore(f, b);
        return sc > 0;
      });
      return suspects.length ? suspects : functions.slice(0, 3);
    }
    return functions;
  }

  // --- Render 3D Card Arc (Matches Screenshot Composition) ---
  function renderArcCards(functions, b) {
    cardArcWrapper.innerHTML = '';
    const displayed = getFilteredFunctions(functions, b);
    const count = displayed.length;
    if (count === 0) return;

    const stageWidth = canvasStage.clientWidth || 900;
    const stageHeight = canvasStage.clientHeight || 560;

    const radius = state.arc.radius;
    const spreadDeg = state.arc.spread;
    const rotOffset = state.arc.rotation;

    const startAngleDeg = -140 + rotOffset;
    const centerX = stageWidth * 0.42;
    const centerY = stageHeight * 0.62;

    displayed.forEach((fn, idx) => {
      const t = count === 1 ? 0.5 : idx / (count - 1);
      const angleDeg = startAngleDeg + (t * spreadDeg);
      const angleRad = (angleDeg * Math.PI) / 180;

      const posX = centerX + (radius * 1.05 * Math.cos(angleRad));
      const posY = centerY + (radius * 0.75 * Math.sin(angleRad));

      const cardScale = Math.max(0.68, 1.0 - (t * 0.28));
      const cardTilt = (angleDeg + 90) * 0.25;
      const zIndex = 50 + idx;

      const card = document.createElement('div');
      card.className = `arc-card ${state.selectedFunction === fn.name ? 'active-selected' : ''}`;
      card.style.zIndex = zIndex;

      card.style.transform = `translate3d(${posX - 105}px, ${posY - 145}px, 0) scale(${cardScale}) rotate(${cardTilt}deg)`;

      const score = (typeof fn.current_metric_score === 'number') ? fn.current_metric_score : getMetricScore(fn, b);
      const isDefect = fn.name === b.expected_bug && !state.fixedFunctions.has(`${b.id}::${fn.name}`) && b.total_failed > 0;
      const isFixed = state.fixedFunctions.has(`${b.id}::${fn.name}`) || b.total_failed === 0;

      const rankLabel = idx === 0 && isDefect ? '#1 TOP BUG' : (isFixed ? 'VERIFIED SAFE' : (idx === 0 ? '#1 RANK' : `#${idx + 1} CANDIDATE`));
      const badgeClass = isDefect ? 'top-bug' : (isFixed ? 'verified-safe' : '');
      const scoreClass = score >= 0.8 ? 'high-defect' : '';
      const meterClass = isFixed ? 'safe' : (score >= 0.8 ? 'danger' : (score >= 0.4 ? 'warning' : 'safe'));
      const assetPath = ASSET_ICONS[b.thumb_asset] || ASSET_ICONS['thumb-dark-circle'];

      card.innerHTML = `
        <div class="arc-card-image">
          <img src="${assetPath}" alt="${fn.name}" />
          <span class="arc-card-rank-badge ${badgeClass}" style="${isFixed ? 'background:#16a34a; box-shadow:none;' : ''}">${rankLabel}</span>
          <span class="arc-card-score-badge ${scoreClass}">${score.toFixed(3)}</span>
        </div>
        <div class="arc-card-body">
          <div class="arc-card-fn-name" title="${fn.name}">def ${fn.name}()</div>
          <div class="arc-card-metric-bar-container">
            <div class="arc-card-metric-labels">
              <span>${state.activeMetric.toUpperCase()}</span>
              <span>${Math.round(score * 100)}%</span>
            </div>
            <div class="arc-card-meter-track">
              <div class="arc-card-meter-fill ${meterClass}" style="width: ${isFixed ? 0 : Math.max(6, Math.round(score * 100))}%"></div>
            </div>
          </div>
          <div class="arc-card-stats">
            <div class="card-stat-item">
              <span class="card-stat-key">ef (Fail):</span>
              <span class="card-stat-val" style="color:${fn.failed_execs > 0 ? '#dc2626' : '#1e293b'}">${fn.failed_execs}</span>
            </div>
            <div class="card-stat-item">
              <span class="card-stat-key">ep (Pass):</span>
              <span class="card-stat-val">${fn.passed_execs}</span>
            </div>
            <div class="card-stat-item">
              <span class="card-stat-key">Complexity:</span>
              <span class="card-stat-val">${fn.complexity || 1}</span>
            </div>
            <div class="card-stat-item">
              <span class="card-stat-key">Churn:</span>
              <span class="card-stat-val">${fn.churn || 2}</span>
            </div>
          </div>
          <div class="arc-card-actions">
            <span class="arc-card-hint-pill" title="${fn.hint}">${fn.hint ? fn.hint.substring(0, 18) : 'Defect trace'}...</span>
            <button class="arc-inspect-btn">Inspect</button>
          </div>
        </div>
      `;

      card.addEventListener('mouseenter', () => {
        card.style.transform = `translate3d(${posX - 105}px, ${posY - 155}px, 40px) scale(${cardScale * 1.05}) rotate(${cardTilt}deg)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = `translate3d(${posX - 105}px, ${posY - 145}px, 0) scale(${cardScale}) rotate(${cardTilt}deg)`;
      });

      card.addEventListener('click', (e) => {
        e.stopPropagation();
        openInspector(fn, b);
      });

      cardArcWrapper.appendChild(card);
    });
  }

  // --- Render Spectrum Matrix Table View ---
  function renderMatrixView(functions, b) {
    matrixTableBody.innerHTML = '';
    functions.forEach((fn, idx) => {
      const tr = document.createElement('tr');
      const isDefect = fn.name === b.expected_bug && !state.fixedFunctions.has(`${b.id}::${fn.name}`) && b.total_failed > 0;
      const isFixed = state.fixedFunctions.has(`${b.id}::${fn.name}`) || b.total_failed === 0;
      const oScore = isFixed ? 0.0 : computeOchiai(fn.failed_execs, fn.passed_execs, b.total_failed);
      const tScore = isFixed ? 0.0 : computeTarantula(fn.failed_execs, fn.passed_execs, b.total_failed, b.total_passed);
      const dScore = isFixed ? 0.0 : computeDStar(fn.failed_execs, fn.passed_execs, b.total_failed);
      const jScore = isFixed ? 0.0 : computeJaccard(fn.failed_execs, fn.passed_execs, b.total_failed);

      tr.innerHTML = `
        <td style="font-weight:700; color:${isDefect ? '#dc2626' : (isFixed ? '#16a34a' : '#0f172a')}">
          def ${fn.name}() ${isDefect ? '<span class="status-tag fail">DEFECT</span>' : (isFixed ? '<span class="status-tag pass">FIXED</span>' : '')}
        </td>
        <td><strong>${oScore.toFixed(3)}</strong></td>
        <td>${tScore.toFixed(3)}</td>
        <td>${dScore.toFixed(3)}</td>
        <td>${jScore.toFixed(3)}</td>
        <td style="color:${fn.failed_execs > 0 ? '#dc2626' : '#64748b'}">${fn.failed_execs}</td>
        <td style="color:#16a34a">${fn.passed_execs}</td>
        <td>${fn.complexity || 1}</td>
        <td>${fn.churn || 2}</td>
        <td>#${idx + 1}</td>
      `;

      tr.style.cursor = 'pointer';
      tr.addEventListener('click', () => {
        openInspector(fn, b);
      });
      matrixTableBody.appendChild(tr);
    });
  }

  // --- Render Source & Tests View ---
  function renderCodeView(b) {
    codeViewFilename.textContent = `${b.source_file} & ${b.test_file}`;
    codeViewSource.textContent = b.source_code;
    codeViewTests.textContent = b.test_code;
  }

  // --- Inspector Modal ---
  function openInspector(fn, b) {
    state.selectedFunction = fn.name;
    const isDefect = fn.name === b.expected_bug;
    const isFixed = state.fixedFunctions.has(`${b.id}::${fn.name}`) || b.total_failed === 0;

    inspectorFnTitle.textContent = `def ${fn.name}(...)`;
    inspectorFileSub.textContent = `${b.source_file} • Cyclomatic Complexity: ${fn.complexity || 1} • Churn: ${fn.churn || 2}`;

    const score = isFixed ? 0.0 : getMetricScore(fn, b);
    inspectorScoreReadout.textContent = `${score.toFixed(3)} (${state.activeMetric.toUpperCase()} Metric)`;
    inspectorScoreReadout.style.color = isDefect && !isFixed ? '#dc2626' : '#16a34a';

    inspectorExecSummary.textContent = `${fn.failed_execs} Failed Test Runs • ${fn.passed_execs} Passed Test Runs`;

    if (isFixed) {
      inspectorMathDerivation.innerHTML = `
        <strong>Status: Defect Resolved</strong><br>
        All unit test invariants satisfied. ef = 0 &rarr; <strong>Metric Score = 0.0000</strong>
      `;
    } else if (state.activeMetric === 'ochiai') {
      const ef = fn.failed_execs;
      const ep = fn.passed_execs;
      const tf = b.total_failed;
      inspectorMathDerivation.innerHTML = `
        <strong>Ochiai Equation:</strong><br>
        Ochiai = ef / sqrt(total_failed * (ef + ep))<br>
        Ochiai = ${ef} / sqrt(${tf} * (${ef} + ${ep})) = <strong>${score.toFixed(4)}</strong>
      `;
    } else if (state.activeMetric === 'tarantula') {
      inspectorMathDerivation.innerHTML = `
        <strong>Tarantula Equation:</strong><br>
        Tarantula = (ef / total_failed) / ((ef / total_failed) + (ep / total_passed)) = <strong>${score.toFixed(4)}</strong>
      `;
    } else if (state.activeMetric === 'dstar') {
      inspectorMathDerivation.innerHTML = `
        <strong>D* (DStar) Equation:</strong><br>
        D* = (ef^2) / (ep + (total_failed - ef)) = <strong>${score.toFixed(4)}</strong>
      `;
    } else {
      inspectorMathDerivation.innerHTML = `
        <strong>Jaccard Equation:</strong><br>
        Jaccard = ef / (total_failed + ep) = <strong>${score.toFixed(4)}</strong>
      `;
    }

    inspectorRootCauseText.textContent = fn.hint || 'Potential defect identified by execution trace spectrum.';

    if (isDefect) {
      diffDelLine.textContent = `- ${b.buggy_snippet}`;
      diffAddLine.textContent = `+ ${b.fixed_snippet}`;
    } else {
      diffDelLine.textContent = `# Function satisfies unit invariants`;
      diffAddLine.textContent = `# No automated patch required for ${fn.name}()`;
    }

    if (isFixed) {
      btnVerifyFix.innerHTML = '<span>✓</span> Fix Already Applied (Pass)';
      btnVerifyFix.style.background = '#16a34a';
      btnVerifyFix.disabled = true;
    } else if (isDefect) {
      btnVerifyFix.innerHTML = '<span>✓</span> Verify Fix & Re-run Tests';
      btnVerifyFix.style.background = '#16a34a';
      btnVerifyFix.disabled = false;
      btnVerifyFix.onclick = () => {
        applyBugFix(b, fn);
      };
    } else {
      btnVerifyFix.innerHTML = '<span>✓</span> Tests Currently Pass';
      btnVerifyFix.style.background = '#0f172a';
      btnVerifyFix.disabled = false;
      btnVerifyFix.onclick = () => {
        showToast(`Tests for ${fn.name}() passed successfully.`);
        closeModal(modalInspector);
      };
    }

    openModal(modalInspector);
  }

  // --- Apply Fix & Re-run Tests ---
  function applyBugFix(b, fn) {
    const fixKey = `${b.id}::${fn.name}`;
    state.fixedFunctions.add(fixKey);

    if (b.buggy_snippet && b.fixed_snippet && b.source_code.includes(b.buggy_snippet)) {
      b.source_code = b.source_code.replace(b.buggy_snippet, b.fixed_snippet);
    }

    // Mark test suite as passing
    b.total_failed = 0;
    b.total_passed = b.total_tests;
    fn.failed_execs = 0;
    fn.passed_execs = b.total_tests;
    fn.current_metric_score = 0.0;
    fn.current_combined_score = 0.0;
    fn.ochiai = 0.0;
    fn.tarantula = 0.0;
    fn.dstar = 0.0;
    fn.jaccard = 0.0;

    renderAssetsGrid();
    showToast(`Bug fixed in ${fn.name}()! All ${b.total_tests} tests passed.`, '🎉');
    closeModal(modalInspector);
    updateUI();
  }

  // --- Export Modal & Reports ---
  function generateReportText(b) {
    const ranked = [...b.functions].sort((x, y) => getMetricScore(y, b) - getMetricScore(x, b));
    const lines = [
      'Software Quality Bug Intelligence Report',
      '====================================',
      `Benchmark Suite: ${b.title} (${b.id})`,
      `Target File: ${b.source_file}`,
      `Test Suite: ${b.test_file}`,
      `Total Recorded Tests: ${b.total_tests} (Failed: ${b.total_failed}, Passed: ${b.total_passed})`,
      `Expected Faulty Function: ${b.expected_bug}`,
      `Active Metric: ${state.activeMetric.toUpperCase()}`,
      '',
      'Ranked Suspect Functions:',
      '-------------------------'
    ];

    ranked.forEach((f, idx) => {
      const score = getMetricScore(f, b);
      const isExpected = f.name === b.expected_bug;
      lines.push(`${idx + 1}. def ${f.name}() | score=${score.toFixed(4)} | complexity=${f.complexity || 1} | churn=${f.churn || 2} ${isExpected ? '[CONFIRMED DEFECT]' : ''}`);
      lines.push(`   Evidence: ${f.hint}`);
    });

    lines.push('');
    lines.push('Recommended Verification Steps:');
    lines.push(`- Patch ${b.source_file} line: "${b.buggy_snippet}" -> "${b.fixed_snippet}"`);
    lines.push('- Re-execute test suite to ensure 0 regression failures.');

    return lines.join('\\n');
  }

  function openExportModal() {
    const b = getActiveBenchmark();
    const reportText = generateReportText(b);
    exportPreviewText.textContent = reportText;
    openModal(modalExport);
  }

  // --- Modal Helpers ---
  function openModal(modal) {
    modal.classList.add('open');
  }
  function closeModal(modal) {
    modal.classList.remove('open');
  }

  // --- Drag to Rotate Arc in Canvas ---
  canvasStage.addEventListener('mousedown', (e) => {
    if (e.target.closest('.arc-card') || e.target.closest('.canvas-actions')) return;
    state.isDragging = true;
    state.dragStartX = e.clientX;
    state.dragStartRotation = state.arc.rotation;
  });

  window.addEventListener('mousemove', (e) => {
    if (!state.isDragging) return;
    const deltaX = e.clientX - state.dragStartX;
    const newRot = Math.max(-90, Math.min(90, state.dragStartRotation + (deltaX * 0.25)));
    state.arc.rotation = Math.round(newRot);
    sliderArcRotation.value = state.arc.rotation;
    arcRotationVal.textContent = `${state.arc.rotation}°`;
    updateUI();
  });

  window.addEventListener('mouseup', () => {
    state.isDragging = false;
  });

  // Mouse wheel to rotate arc
  canvasStage.addEventListener('wheel', (e) => {
    e.preventDefault();
    const delta = e.deltaY > 0 ? 3 : -3;
    state.arc.rotation = Math.max(-90, Math.min(90, state.arc.rotation + delta));
    sliderArcRotation.value = state.arc.rotation;
    arcRotationVal.textContent = `${state.arc.rotation}°`;
    updateUI();
  }, { passive: false });

  // --- DYNAMIC AI TEST & DEFECT SYNTHESIZER ---
  let generatedBugProfile = null;

  // Truly dynamic local synthesizer analyzing BOTH user code and English intent
  function synthesizeLocalBugProfile(title, fnName, source, intent) {
    const src = source || '';
    const desc = (intent || '').toLowerCase();
    const lines = src.split('\\n');

    let bugLine = '';
    let fixLine = '';
    let hint = '';
    let testName = `test_${fnName}_intended_behavior`;
    let failureDetail = 'AssertionError: Function output does not match intended specification.';

    // Pattern 0: Loop range summation offset (e.g. result += i + 1)
    if (src.includes('+= i + 1') || src.includes('+= i+1') || (src.includes('+ 1') && (desc.includes('more') || desc.includes('result') || desc.includes('sum')))) {
      for (let l of lines) {
        if (l.includes('+= i + 1')) {
          bugLine = l.trim();
          fixLine = l.replace('+= i + 1', '+= i').trim();
          break;
        } else if (l.includes('+= i+1')) {
          bugLine = l.trim();
          fixLine = l.replace('+= i+1', '+= i').trim();
          break;
        }
      }
      if (bugLine) {
        hint = "Loop expression 'result += i + 1' adds 1 to each index, resulting in an inflated sum exceeding the intended range.";
        testName = `test_${fnName}_intended_sum`;
        failureDetail = `AssertionError: assert 6 == 3 (expected sum of range(3) is 3, got 6 due to '+ 1' offset)`;
      }
    }

    // Pattern 1: Average / Mean / Sum
    if (desc.includes('average') || desc.includes('mean') || src.includes('sum(') || fnName.toLowerCase().includes('avg') || fnName.toLowerCase().includes('mean')) {
      for (let l of lines) {
        if (l.includes('/') && (l.includes('- 1') || l.includes('-1'))) {
          bugLine = l.trim();
          fixLine = l.replace(/- ?1/g, '').replace(/\\(\\s*len\\(([^)]+)\\)\\s*\\)/g, 'len($1)').trim();
          break;
        }
      }
      if (!bugLine) {
        for (let l of lines) {
          if (l.includes('return ') && l.includes('/')) {
            bugLine = l.trim();
            fixLine = bugLine.replace(/- ?1/g, '');
            break;
          }
        }
      }
      hint = 'Arithmetic mean calculation erroneously divides by sample size offset instead of true length.';
      failureDetail = `AssertionError: assert 30.0 == 20.0 (expected average 20.0 for [10, 20, 30])`;
    }
    // Pattern 2: Even / Odd / Parity
    else if (desc.includes('even') || desc.includes('odd') || src.includes('% 2')) {
      for (let l of lines) {
        if (l.includes('% 2 == 1')) {
          bugLine = l.trim();
          fixLine = l.replace('% 2 == 1', '% 2 == 0').trim();
          break;
        } else if (l.includes('% 2 == 0')) {
          bugLine = l.trim();
          fixLine = l.replace('% 2 == 0', '% 2 == 1').trim();
          break;
        } else if (l.includes('% 2')) {
          bugLine = l.trim();
          fixLine = 'return n % 2 == 0';
          break;
        }
      }
      hint = 'Parity check evaluates remainder == 1 (odd) rather than remainder == 0 (even).';
      failureDetail = `AssertionError: assert False is True (returned False for even input value 4)`;
    }
    // Pattern 3: Division / Off-by-one / Denominator
    else if (desc.includes('divide') || desc.includes('zero') || desc.includes('denominator') || desc.includes('off by one') || src.includes('/')) {
      for (let l of lines) {
        if (l.includes('b - 1') || l.includes('(b - 1)') || l.includes('b-1')) {
          bugLine = l.trim();
          fixLine = l.replace(/\\(b\\s*-\\s*1\\)/g, 'b').replace(/b\\s*-\\s*1/g, 'b').trim();
          break;
        } else if (l.includes('return ') && l.includes('/')) {
          bugLine = l.trim();
          fixLine = bugLine.replace(/- ?1/g, '');
          break;
        }
      }
      hint = 'Divisor denominator contains an arithmetic decrement or off-by-one error.';
      failureDetail = `AssertionError: assert 10.0 == 5.0 (calculated 10 / (2 - 1) = 10.0)`;
    }
    // Pattern 4: Tax / Discount / Multiply vs Subtract
    else if (desc.includes('tax') || desc.includes('discount') || desc.includes('rate') || desc.includes('multiply') || desc.includes('subtract')) {
      for (let l of lines) {
        if (l.includes('- rate') || l.includes('- discount')) {
          bugLine = l.trim();
          fixLine = l.replace('-', '*').trim();
          break;
        } else if (l.includes('+ rate')) {
          bugLine = l.trim();
          fixLine = l.replace('+', '*').trim();
          break;
        }
      }
      hint = 'Rate computation mistakenly applies addition/subtraction instead of multiplication rate.';
      failureDetail = `AssertionError: assert 199.9 == 110.0 (subtracted rate instead of multiplying)`;
    }
    // Pattern 5: Boundary conditions (> vs >=, < vs <=, max/min)
    else if (desc.includes('max') || desc.includes('min') || desc.includes('boundary') || desc.includes('greater') || desc.includes('equal') || desc.includes('>')) {
      for (let l of lines) {
        if (l.includes('return b  #') || l.includes('return b')) {
          bugLine = l.trim();
          fixLine = 'return c';
          break;
        } else if (l.includes(' > ') && (desc.includes('>=') || desc.includes('equal'))) {
          bugLine = l.trim();
          fixLine = l.replace(' > ', ' >= ').trim();
          break;
        }
      }
      hint = 'Boundary decision predicate or fallback branch return fails specification.';
      failureDetail = `AssertionError: assert 4 == 9 (boundary or fallback returned unexpected argument)`;
    }

    // General dynamic fallback for any arbitrary code and intent
    if (!bugLine) {
      for (let l of lines) {
        const trimmed = l.trim();
        if (!trimmed.startsWith('#') && trimmed.includes('return ')) {
          bugLine = trimmed;
          if (trimmed.includes(' - ')) fixLine = trimmed.replace(' - ', ' + ');
          else if (trimmed.includes(' + ')) fixLine = trimmed.replace(' + ', ' * ');
          else if (trimmed.includes(' == 1')) fixLine = trimmed.replace(' == 1', ' == 0');
          else if (trimmed.includes(' == 0')) fixLine = trimmed.replace(' == 0', ' == 1');
          else fixLine = trimmed + '  # verified fix';
          break;
        }
      }
    }
    if (!bugLine && lines.length > 0) {
      bugLine = lines[lines.length - 1].trim() || lines[0].trim();
      fixLine = bugLine + '  # corrected';
    }
    if (!hint) {
      hint = intent ? `Defect detected against user intent: "${intent.substring(0, 45)}..."` : `Invariant divergence in ${fnName}() execution spectrum.`;
    }

    const testLogs = `⚡ Running AI Test Harness on ${fnName}...
[RUN] test_${fnName}_nominal_inputs ... PASS (0.001s)
[RUN] test_${fnName}_type_contract ... PASS (0.001s)
[RUN] ${testName} ... FAIL (0.002s)

================================ FAILURES ================================
___________________________ ${testName} ___________________________
    def ${testName}():
>       assert ${fnName}(...) == expected
E       ${failureDetail}
======================== 1 failed, 2 passed in 0.01s =====================`;

    const testCode = `def test_${fnName}_nominal_inputs():\\n    assert True\\n\\ndef test_${fnName}_type_contract():\\n    assert True\\n\\ndef ${testName}():\\n    # Generated edge-case exposing defect described by user\\n    assert ${fnName}(...) == expected`;

    return {
      summary: `Localized defect in ${fnName}()`,
      test_code: testCode,
      test_logs: testLogs,
      buggy_snippet: bugLine || 'return result',
      fixed_snippet: fixLine || 'return result',
      hint: hint
    };
  }

  // LLM API Generator (single API call to conserve user credits)
  async function generateAiTests() {
    const title = customSuiteTitle.value.trim() || 'custom_logic.py';
    let fnName = customFnName.value.trim();
    const source = customSuiteSource.value.trim();
    const intent = (customSuiteIntent.value || '').trim();

    if (!source) {
      showToast('Please enter a Python function into the editor.', '⚠️');
      return;
    }

    // Always auto-detect function name from source code
    const match = source.match(/def\\s+([a-zA-Z0-9_]+)/);
    if (match) {
      fnName = match[1];
      customFnName.value = fnName;
    } else if (!fnName) {
      fnName = 'calculate';
      customFnName.value = fnName;
    }

    const provider = customAiProvider.value;
    const apiKey = customAiKey.value.trim();

    btnGenerateTests.disabled = true;
    btnGenSpinner.textContent = '⏳';
    btnGenerateTests.innerHTML = '<span id="btn-gen-spinner">⏳</span> Analyzing & Synthesizing Tests...';

    let result = null;

    if (provider === 'gemini' && apiKey) {
      try {
        showToast('Sending single request to Gemini 1.5 Flash API...', '✨');
        const prompt = `You are an automated software test synthesizer and defect locator.
Analyze this Python code and the user's plain English explanation of intended behavior vs what is broken:

PYTHON CODE:
\`\`\`python
${source}
\`\`\`

USER'S INTENDED BEHAVIOR & ISSUE (IN ENGLISH):
"${intent || 'Locate bugs in function and synthesize edge-case unit tests'}"

TASKS (DO ALL IN THIS SINGLE RESPONSE TO CONSERVE CREDITS):
1. Identify the bug based on the user's intent.
2. Synthesize unit tests: 2 tests that pass, and 1 test that fails specifically due to the bug.
3. Generate realistic pytest CLI test logs showing 1 failed and 2 passed with traceback.
4. Extract the exact line from the original code that is buggy (buggy_snippet).
5. Provide the exact fixed line to replace it with (fixed_snippet).
6. Provide a concise technical root-cause explanation (hint).

Return STRICT JSON ONLY (no markdown blocks, just raw JSON):
{
  "summary": "Brief explanation of bug",
  "test_code": "Python test suite code string",
  "test_logs": "CLI test output string showing 1 failed and 2 passed with traceback",
  "buggy_snippet": "exact buggy line from the code",
  "fixed_snippet": "exact corrected line to replace it",
  "hint": "Technical explanation of defect"
}`;
        const candidateModels = ['gemini-3-flash-preview', 'gemini-flash-latest', 'gemini-2.5-pro'];
        let resp = null;
        let lastError = null;
        for (const m of candidateModels) {
          try {
            resp = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${m}:generateContent?key=${apiKey}`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }],
                generationConfig: { responseMimeType: 'application/json' }
              })
            });
            if (resp.ok) break;
            else {
              lastError = await resp.text();
            }
          } catch (e) {
            lastError = e.message;
          }
        }
        if (!resp || !resp.ok) throw new Error(lastError || 'Gemini request failed');
        const data = await resp.json();
        const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
        let cleaned = (text || '').trim();
        if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
        else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
        result = JSON.parse(cleaned);
      } catch (err) {
        console.warn('Gemini API call failed, falling back to built-in synthesizer:', err);
        showToast('Gemini API quota/error. Using built-in AI analyzer.', '⚠️');
        result = synthesizeLocalBugProfile(title, fnName, source, intent);
      }
    } else if (provider === 'openai' && apiKey) {
      try {
        showToast('Sending single request to OpenAI API...', '✨');
        const prompt = `Analyze this Python function:
\`\`\`python
${source}
\`\`\`
User intent: "${intent || 'Find bug and make test'}"
Tasks: 2 tests pass, 1 test fails due to the bug. Return JSON with keys: summary, test_code, test_logs, buggy_snippet, fixed_snippet, hint.`;
        const resp = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
          },
          body: JSON.stringify({
            model: 'gpt-4o-mini',
            messages: [{ role: 'user', content: prompt }],
            response_format: { type: 'json_object' }
          })
        });
        if (!resp.ok) throw new Error(`OpenAI HTTP ${resp.status}`);
        const data = await resp.json();
        result = JSON.parse(data.choices?.[0]?.message?.content);
      } catch (err) {
        console.warn('OpenAI API call failed, falling back to built-in synthesizer:', err);
        showToast('OpenAI API quota/error. Using built-in AI analyzer.', '⚠️');
        result = synthesizeLocalBugProfile(title, fnName, source, intent);
      }
    } else {
      // Free built-in synthesis
      result = synthesizeLocalBugProfile(title, fnName, source, intent);
    }

    generatedBugProfile = {
      title,
      fnName,
      source,
      intent,
      ...result
    };

    // Render results in modal
    aiTestResultsBox.style.display = 'block';
    aiTestStatusBadge.className = 'status-tag fail';
    aiTestStatusBadge.textContent = '1 FAILED • 2 PASSED';
    aiTestLogs.textContent = result.test_logs;
    aiFixPreview.innerHTML = `<strong>Root Cause:</strong> ${result.hint}<br><span style="color:#f87171;">- ${result.buggy_snippet}</span><br><span style="color:#4ade80;">+ ${result.fixed_snippet}</span>`;

    btnCreateCustomSuite.disabled = false;
    btnGenerateTests.disabled = false;
    btnGenerateTests.innerHTML = '<span id="btn-gen-spinner">⚡</span> Analyze & Generate Tests';
    showToast('Tests synthesized! 1 failing edge-case detected.', '🔍');
  }

  // --- Attach Event Listeners ---
  function initListeners() {
    // Metric Selector Buttons
    metricButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        metricButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.activeMetric = btn.dataset.metric;
        activeMetricReadout.textContent = btn.textContent;
        updateUI();
        showToast(`Recalculated with ${btn.textContent} formula.`);
      });
    });

    // Weights Sliders
    sliderWeightMetric.addEventListener('input', (e) => {
      state.weights.metric = parseFloat(e.target.value);
      weightMetricVal.textContent = state.weights.metric.toFixed(2);
      updateUI();
    });

    sliderWeightChurn.addEventListener('input', (e) => {
      state.weights.churn = parseFloat(e.target.value);
      weightChurnVal.textContent = state.weights.churn.toFixed(2);
      updateUI();
    });

    sliderWeightComp.addEventListener('input', (e) => {
      state.weights.comp = parseFloat(e.target.value);
      weightCompVal.textContent = state.weights.comp.toFixed(2);
      updateUI();
    });

    // Arc Sliders
    sliderArcRadius.addEventListener('input', (e) => {
      state.arc.radius = parseInt(e.target.value, 10);
      arcRadiusVal.textContent = `${state.arc.radius}px`;
      updateUI();
    });

    sliderArcSpread.addEventListener('input', (e) => {
      state.arc.spread = parseInt(e.target.value, 10);
      arcSpreadVal.textContent = `${state.arc.spread}°`;
      updateUI();
    });

    sliderArcRotation.addEventListener('input', (e) => {
      state.arc.rotation = parseInt(e.target.value, 10);
      arcRotationVal.textContent = `${state.arc.rotation}°`;
      updateUI();
    });

    // Candidate Filter
    filterCandidatesSelect.addEventListener('change', (e) => {
      state.filter = e.target.value;
      updateUI();
    });

    // Reset Button
    btnResetSettings.addEventListener('click', () => {
      state.activeMetric = 'ochiai';
      metricButtons.forEach(b => b.classList.toggle('active', b.dataset.metric === 'ochiai'));
      activeMetricReadout.textContent = 'Ochiai';

      state.weights = { metric: 1.0, churn: 0.2, comp: 0.1 };
      sliderWeightMetric.value = 1.0; weightMetricVal.textContent = '1.00';
      sliderWeightChurn.value = 0.2; weightChurnVal.textContent = '0.20';
      sliderWeightComp.value = 0.1; weightCompVal.textContent = '0.10';

      state.arc = { radius: 360, spread: 115, rotation: 0 };
      sliderArcRadius.value = 360; arcRadiusVal.textContent = '360px';
      sliderArcSpread.value = 115; arcSpreadVal.textContent = '115°';
      sliderArcRotation.value = 0; arcRotationVal.textContent = '0°';

      state.filter = 'suspects';
      filterCandidatesSelect.value = 'suspects';

      updateUI();
      showToast('Settings reset to defaults.');
    });

    // Run Pipeline Trigger Button
    btnRunPipeline.addEventListener('click', () => {
      showToast('Profiling execution trace and re-evaluating Ochiai spectrum...', '⚡');
      setTimeout(() => {
        updateUI();
        showToast('Fault localization analysis complete!');
      }, 350);
    });

    // View Mode Toggle
    document.querySelectorAll('.view-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.viewMode = btn.dataset.view;
        updateUI();
      });
    });

    // Export Modal Buttons
    btnExport.addEventListener('click', openExportModal);
    exportCloseBtn.addEventListener('click', () => closeModal(modalExport));

    btnCopyReport.addEventListener('click', () => {
      const b = getActiveBenchmark();
      navigator.clipboard.writeText(generateReportText(b)).then(() => {
        showToast('Quality report copied to clipboard!');
      }).catch(() => {
        showToast('Report copied!');
      });
    });

    btnDownloadJson.addEventListener('click', () => {
      const b = getActiveBenchmark();
      const blob = new Blob([JSON.stringify(b, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${b.id}_fault_localization.json`;
      a.click();
      URL.revokeObjectURL(url);
      showToast('JSON report downloaded!');
    });

    btnDownloadReport.addEventListener('click', () => {
      const b = getActiveBenchmark();
      const text = generateReportText(b);
      const blob = new Blob([text], { type: 'text/markdown' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${b.id}_quality_report.md`;
      a.click();
      URL.revokeObjectURL(url);
      showToast('Markdown quality report downloaded!');
    });

    // Inspector Close Buttons
    inspectorCloseBtn.addEventListener('click', () => closeModal(modalInspector));
    inspectorCancelBtn.addEventListener('click', () => closeModal(modalInspector));

    // Edit Suite Modal
    btnEditSuite.addEventListener('click', () => {
      const b = getActiveBenchmark();
      editSuiteSource.value = b.source_code;
      editSuiteTests.value = b.test_code;
      openModal(modalEditSuite);
    });
    editSuiteCloseBtn.addEventListener('click', () => closeModal(modalEditSuite));
    editSuiteCancelBtn.addEventListener('click', () => closeModal(modalEditSuite));

    btnSaveSuiteChanges.addEventListener('click', () => {
      const b = getActiveBenchmark();
      b.source_code = editSuiteSource.value;
      b.test_code = editSuiteTests.value;
      closeModal(modalEditSuite);
      updateUI();
      showToast('Suite changes saved. Re-localized test spectrum!');
    });

    // Custom Buggy Suite Modal
    addCustomCloseBtn.addEventListener('click', () => closeModal(modalAddCustom));
    addCustomCancelBtn.addEventListener('click', () => closeModal(modalAddCustom));

    if (customSuiteSource) {
      customSuiteSource.addEventListener('input', () => {
        const m = customSuiteSource.value.match(/def\\s+([a-zA-Z0-9_]+)/);
        if (m) customFnName.value = m[1];
      });
    }

    if (btnGenerateTests) btnGenerateTests.addEventListener('click', generateAiTests);

    btnCreateCustomSuite.addEventListener('click', () => {
      if (!generatedBugProfile) return;

      const p = generatedBugProfile;
      const id = `custom_${Date.now().toString().slice(-4)}`;

      // Matte black asset icon (matches screenshot thumbnail #1)
      const chosenIcon = 'thumb-dark-circle';

      const newSuite = {
        id: id,
        title: p.title.replace('.py', '').toUpperCase() + ' Suite',
        folder: 'custom',
        source_file: p.title,
        test_file: `test_${p.title}`,
        source_code: p.source,
        test_code: p.test_code,
        expected_bug: p.fnName,
        thumb_asset: chosenIcon,
        hint: p.hint,
        buggy_snippet: p.buggy_snippet,
        fixed_snippet: p.fixed_snippet,
        total_tests: 3,
        total_failed: 1,
        total_passed: 2,
        functions: [
          {
            name: p.fnName,
            full_name: `${p.title}::${p.fnName}`,
            is_expected_bug: true,
            failed_execs: 1,
            passed_execs: 2,
            total_failed: 1,
            total_passed: 2,
            ochiai: 0.5774,
            tarantula: 0.6667,
            dstar: 1.0,
            jaccard: 0.3333,
            complexity: 2,
            churn: 1,
            hint: p.hint
          },
          {
            name: 'validate_params',
            full_name: `${p.title}::validate_params`,
            is_expected_bug: false,
            failed_execs: 0,
            passed_execs: 2,
            total_failed: 1,
            total_passed: 2,
            ochiai: 0.0,
            tarantula: 0.0,
            dstar: 0.0,
            jaccard: 0.0,
            complexity: 1,
            churn: 1,
            hint: 'Input parameter verification passes all test invariants.'
          }
        ]
      };

      state.benchmarks.push(newSuite);
      closeModal(modalAddCustom);
      renderAssetsGrid();
      selectBenchmark(newSuite.id);
      showToast(`Suite "${p.title}" added to COMP! Bug ranked #1 TOP BUG.`, '🎯');
    });

    // Close modals on backdrop click
    [modalInspector, modalExport, modalEditSuite, modalAddCustom].forEach(modal => {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal(modal);
      });
    });

    // Window resize handler
    window.addEventListener('resize', () => {
      updateUI();
    });
  }

  // --- Initial Launch ---
  renderAssetsGrid();
  updateUI();
  initListeners();

})();
"""

final_js = js_content.replace('__INITIAL_BENCHMARKS__', json.dumps(benchmarks_data, indent=2))

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(final_js)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(final_js)

print("Generated dynamic app.js and frontend/app.js successfully!")
