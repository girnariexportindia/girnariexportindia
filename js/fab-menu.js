document.addEventListener("DOMContentLoaded", () => {
  const items = gsap.utils.toArray(".fab-item");
  const radius = 100;
  const startAngle = 0;
  const endAngle = -90;
  const angleStep = (endAngle - startAngle) / (items.length - 1);
  let isOpen = false;

  gsap.set(".fab-item", { x: 0, y: 0, scale: 0, opacity: 0 });

  const tl = gsap.timeline({ paused: true });

  items.forEach((item, i) => {
    const angle = (startAngle + angleStep * i) * (Math.PI / 180);
    const tx = Math.cos(angle) * radius;
    const ty = Math.sin(angle) * radius;
    tl.to(item, {
      x: tx,
      y: ty,
      scale: 1,
      opacity: 1,
      duration: 0.6,
      ease: "elastic.out(1, 0.5)",
      easeReverse: true
    }, i * 0.05);
  });

  tl.to("#fabBtn svg", {
    rotation: 135,
    duration: 0.35,
    ease: "back.out(1.7)",
    easeReverse: true
  }, 0);

  const fabBtn = document.querySelector("#fabBtn");
  fabBtn.addEventListener("click", () => {
    if (isOpen) {
      tl.reverse();
      fabBtn.setAttribute("aria-expanded", "false");
    } else {
      tl.play();
      fabBtn.setAttribute("aria-expanded", "true");
    }
    isOpen = !isOpen;
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen) {
      tl.reverse();
      fabBtn.setAttribute("aria-expanded", "false");
      isOpen = false;
    }
  });
});
