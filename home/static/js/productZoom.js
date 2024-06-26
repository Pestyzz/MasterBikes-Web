document.addEventListener("DOMContentLoaded", () => {
    const img = document.querySelector('.image-container img');
    let scale = 1;
    const scaleStep = 0.1;
    const minScale = 1;
    const maxScale = 3;

    img.addEventListener('wheel', (event) => {
        event.preventDefault();
        if (event.deltaY < 0) {
            scale = Math.min(scale + scaleStep, maxScale);
        } else {
            scale = Math.max(scale - scaleStep, minScale);
        }
        img.style.transform = `translate(-50%, -50%) scale(${scale})`;
    });
});
