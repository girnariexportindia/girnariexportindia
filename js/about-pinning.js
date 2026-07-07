document.addEventListener("DOMContentLoaded", () => {
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        let panels = gsap.utils.toArray(".pin-panel");

        panels.forEach((panel, i) => {
            // Check if there is a next panel to layer over this one
            let nextPanel = panels[i + 1];

            // If there's a next panel, scale this panel down as the next one scrolls up over it
            if (nextPanel) {
                gsap.to(panel, {
                    scale: 0.92,
                    opacity: 0.5,
                    ease: "none",
                    scrollTrigger: {
                        trigger: nextPanel,
                        start: "top bottom", // Animation starts when the next panel's top hits the bottom of the viewport
                        end: "top top",      // Animation ends when the next panel's top hits the top of the viewport
                        scrub: true
                    }
                });
            }

            // Pin the panel itself when it reaches the top
            ScrollTrigger.create({
                trigger: panel,
                start: "top top",
                pin: true,
                pinSpacing: false // Important: Allows the next section to scroll over it instead of pushing it down
            });
        });
    }
});
