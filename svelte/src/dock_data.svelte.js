let autoplay = localStorage.getItem("autoplay") === "true" ? true : false;
let sound = localStorage.getItem("sound") === "false" ? false : true;
let theme = localStorage.getItem("theme") === "dark" ? true : false;

export const dockData = $state({
    autoplay: autoplay,
    sound: sound,
    theme: theme,
    currentIndex: 0
})