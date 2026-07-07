document.addEventListener("DOMContentLoaded", () => {
    if (typeof gsap === 'undefined' || typeof Draggable === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    const cardsContainer = document.querySelector('.why-choose-cards');
    if (!cardsContainer) return;
    
    let originalCards = gsap.utils.toArray('.why-choose-cards .strength-card');
    if (originalCards.length === 0) return;

    // Clone cards once so we have enough items for a wide screen seamless loop (10 cards total)
    originalCards.forEach(card => {
        let clone = card.cloneNode(true);
        cardsContainer.appendChild(clone);
    });

    let iteration = 0; 
    gsap.set('.why-choose-cards .strength-card', {xPercent: 400, opacity: 0, scale: 0});

    const spacing = 0.1, 
          snapTime = gsap.utils.snap(spacing),
          cards = gsap.utils.toArray('.why-choose-cards .strength-card'),
          animateFunc = element => {
              const tl = gsap.timeline();
              tl.fromTo(element, {scale: 0, opacity: 0}, {scale: 1, opacity: 1, zIndex: 100, duration: 0.5, yoyo: true, repeat: 1, ease: "power1.in", immediateRender: false})
                .fromTo(element, {xPercent: 400}, {xPercent: -400, duration: 1, ease: "none", immediateRender: false}, 0);
              return tl;
          },
          seamlessLoop = buildSeamlessLoop(cards, spacing, animateFunc);

    let playhead = {offset: 0},
        wrapTime = gsap.utils.wrap(0, seamlessLoop.duration()),
        scrub = gsap.to(playhead, {
            offset: 0,
            onUpdate() {
                seamlessLoop.time(wrapTime(playhead.offset));
            },
            duration: 0.5,
            ease: "power3",
            paused: true
        });

    // Handle button clicks to move the slider forward/backward without jumping scroll
    function moveSlider(direction) {
        scrub.vars.offset = playhead.offset + (spacing * direction);
        scrub.invalidate().restart();
    }

    const nextBtn = document.querySelector(".wc-next");
    const prevBtn = document.querySelector(".wc-prev");
    if (nextBtn) nextBtn.addEventListener("click", () => moveSlider(1));
    if (prevBtn) prevBtn.addEventListener("click", () => moveSlider(-1));

    Draggable.create(".drag-proxy", {
        type: "x",
        trigger: ".why-choose-gallery",
        onPress() {
            this.startOffset = playhead.offset;
        },
        onDrag() {
            scrub.vars.offset = this.startOffset + (this.startX - this.x) * 0.001;
            scrub.invalidate().restart();
        }
    });

    function buildSeamlessLoop(items, spacing, animateFunc) {
        let overlap = Math.ceil(1 / spacing), 
            startTime = items.length * spacing + 0.5, 
            loopTime = (items.length + overlap) * spacing + 1, 
            rawSequence = gsap.timeline({paused: true}), 
            seamlessLoop = gsap.timeline({ 
                paused: true,
                repeat: -1, 
                onRepeat() { 
                    this._time === this._dur && (this._tTime += this._dur - 0.01);
                }
            }),
            l = items.length + overlap * 2,
            time, i, index;

        for (i = 0; i < l; i++) {
            index = i % items.length;
            time = i * spacing;
            rawSequence.add(animateFunc(items[index]), time);
            i <= items.length && seamlessLoop.add("label" + i, time); 
        }

        rawSequence.time(startTime);
        seamlessLoop.to(rawSequence, {
            time: loopTime,
            duration: loopTime - startTime,
            ease: "none"
        }).fromTo(rawSequence, {time: overlap * spacing + 1}, {
            time: startTime,
            duration: startTime - (overlap * spacing + 1),
            immediateRender: false,
            ease: "none"
        });
        return seamlessLoop;
    }
});
