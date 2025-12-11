import { mount } from 'svelte';
import DocumentaryCard from './DocumentaryCard.svelte';

document.querySelectorAll('[data-svelte="documentary-card"]').forEach(el => {
    mount(DocumentaryCard, {
        target: el,
        props: {
            id: el.dataset.documentaryId,
            title: el.dataset.documentaryTitle,
            image: el.dataset.documentaryImage
        }
    })
})