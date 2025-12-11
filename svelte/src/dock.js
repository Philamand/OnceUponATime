import { mount } from 'svelte';
import Dock from './Dock.svelte';

const el = document.getElementById("dock");

mount(Dock, {
    target: el, 
    props: {
        autoplay: el
    }
})