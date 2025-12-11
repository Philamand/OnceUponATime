import { mount } from 'svelte';
import Dock from './Dock.svelte';

mount(Dock, {
    target: document.getElementById("dock"), 
    props: {
        autoplay: document.getElementById("dock").dataset.autoplay
    }
})