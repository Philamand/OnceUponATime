<script>
    import { dockData } from "./dock_data.svelte";

    let props = $props();

    function onclick() {
        document.getElementById(`modal_${props.id}`).showModal();
        let audio = document.getElementById(`audio_${props.id}`);

        if (audio && dockData.sound) {
            audio.play();
        }
    }
</script>

<button class="card bg-base-100 w-full h-full shadow-sm" {onclick}>
    <figure>
        <img src={props.image} alt="{props.title} cover" />
    </figure>
    <div class="card-body">
        <h2 class="card-title">{props.title}</h2>
    </div>
</button>
