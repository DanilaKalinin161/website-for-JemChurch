const productContainers = [...document.querySelectorAll('.slider-container-main')];
const nxtBtn = [...document.querySelectorAll('.nxt-button')];
const preBtn = [...document.querySelectorAll('.pre-button')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})