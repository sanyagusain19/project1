// ===================================
//   CUSTOM CURSOR + FADING TRAIL
//   Skips itself entirely on touch devices
//   and when the user prefers reduced motion.
// ===================================

(function () {
  const isTouch = window.matchMedia('(pointer: coarse)').matches;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (isTouch || prefersReducedMotion) return; // native cursor stays as-is

  document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('custom-cursor-active');

    // --- main dot + ring ---
    const dot = document.createElement('div');
    dot.className = 'cursor-dot';
    const ring = document.createElement('div');
    ring.className = 'cursor-ring';
    document.body.append(dot, ring);

    // --- trail dots (glittery pink glints, shrinking size,
    //     with every 3rd dot rendered as a tiny sparkle star) ---
    const TRAIL_LENGTH = 8;
    const trail = [];
    for (let i = 0; i < TRAIL_LENGTH; i++) {
      const el = document.createElement('div');
      el.className = 'cursor-trail-dot';
      if (i % 3 === 1) el.classList.add('sparkle-star'); // every 3rd-ish dot is a star

      const size = 8 - i * 0.6; // shrinks toward the tail
      el.style.width = `${Math.max(size, 3)}px`;
      el.style.height = `${Math.max(size, 3)}px`;

      // stagger the twinkle so dots don't all sparkle in unison
      el.style.animationDelay = `${(i * 0.12).toFixed(2)}s`;

      document.body.appendChild(el);
      trail.push({ el, x: 0, y: 0 });
    }

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let dotX = mouseX, dotY = mouseY;
    let ringX = mouseX, ringY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    // hover state on anything clickable
    const hoverTargets = 'a, button, .theme-toggle, .skills span, .contact-btn, input, textarea, [role="button"]';
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(hoverTargets)) ring.classList.add('cursor-hovering');
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(hoverTargets)) ring.classList.remove('cursor-hovering');
    });

    function animate() {
      // dot follows tightly, ring lags a touch, trail lags progressively
      dotX += (mouseX - dotX) * 0.9;
      dotY += (mouseY - dotY) * 0.9;
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;

      dot.style.transform = `translate(${dotX}px, ${dotY}px) translate(-50%,-50%)`;
      ring.style.transform = `translate(${ringX}px, ${ringY}px) translate(-50%,-50%)`;

      let prevX = mouseX, prevY = mouseY;
      trail.forEach((point, i) => {
        const ease = 0.35 - i * 0.02;
        point.x += (prevX - point.x) * Math.max(ease, 0.12);
        point.y += (prevY - point.y) * Math.max(ease, 0.12);
        point.el.style.transform = `translate(${point.x}px, ${point.y}px) translate(-50%,-50%)`;
        prevX = point.x;
        prevY = point.y;
      });

      requestAnimationFrame(animate);
    }

    requestAnimationFrame(animate);

    // hide everything while the cursor is off-window
    document.addEventListener('mouseleave', () => {
      dot.style.opacity = '0';
      ring.style.opacity = '0';
      trail.forEach(p => (p.el.style.opacity = '0'));
    });
    document.addEventListener('mouseenter', () => {
      dot.style.opacity = '1';
      ring.style.opacity = '.55';
      trail.forEach((p, i) => (p.el.style.opacity = String(0.45 - i * 0.05)));
    });
  });
})();