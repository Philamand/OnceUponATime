<script>
    import { House, Play, Pause, Volume2, VolumeOff } from "@lucide/svelte";
    import { dockData } from "./dock_data.svelte";

    function switchAutoplay() {
        dockData.autoplay = !dockData.autoplay;
        if (dockData.autoplay) {
            dockData.sound = true;
        }
    }

    function switchSound() {
        dockData.sound = !dockData.sound;
        if (!dockData.sound) {
            dockData.autoplay = false;

            document.querySelectorAll("audio").forEach((audio) => {
                if (!audio.paused) {
                    audio.pause();
                    audio.currentTime = 0;
                }
            });
        } else {
            let audioPlayer = document.getElementById(
                `audio-${dockData.currentIndex}`,
            );

            if (audioPlayer) {
                audioPlayer.play();
            }
        }
    }
</script>

<div class="dock">
    <a href="/">
        <House />
        <span class="dock-label">Home</span>
    </a>

    <button onclick={switchAutoplay}>
        {#if dockData.autoplay}
            <Play />
        {:else}
            <Pause />
        {/if}
        <span class="dock-label">Lecture Auto</span>
    </button>

    <button onclick={switchSound}>
        {#if dockData.sound}
            <Volume2 />
        {:else}
            <VolumeOff />
        {/if}
        <span class="dock-label">Volume</span>
    </button>
</div>
