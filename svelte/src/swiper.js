import { mount } from 'svelte';
import Swiper from './Swiper.svelte';

const el = document.getElementById("swiper");

mount(Swiper, {
    target: el,
    props: {
        direction: el.dataset.direction,
        url: el.dataset.url
    }
})