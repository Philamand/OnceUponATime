<script>
    import { dockData } from "./dock_data.svelte";

    let width = $state(0);
    let height = $state(0);
    let colClass = $derived(width > height ? "flex-row" : "flex-col");
    const pages = JSON.parse(document.getElementById("pages-data").textContent);

    function onclick(event) {
        if (dockData.currentIndex > 0) {
            let audioPlayer = document.getElementById(
                `audio-${dockData.currentIndex}`,
            );
            if (audioPlayer) {
                audioPlayer.pause();
                audioPlayer.currentTime = 0;
            }
        }

        if (
            event.clientX > window.screen.width / 2 &&
            dockData.currentIndex < pages.length - 1
        ) {
            dockData.currentIndex++;
            let audioPlayer = document.getElementById(
                `audio-${dockData.currentIndex}`,
            );
            if (audioPlayer && dockData.sound) {
                audioPlayer.play();
            }
        } else if (
            event.clientX < window.screen.width / 2 &&
            dockData.currentIndex > 0
        ) {
            dockData.currentIndex--;
        }
    }
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />

<main>
    <div
        role="link"
        tabindex={dockData.currentIndex}
        {onclick}
        onkeyup={(e) =>
            e.key === "ArrowLeft"
                ? onclick({ clientX: 0 })
                : onclick({ clientX: 10000 })}
        aria-label="Change Page"
        class={["h-screen flex", colClass]}
    >
        <img src={pages[dockData.currentIndex].image} alt="Illustration" />
        <div class="h-full w-full flex flex-col justify-center text-center">
            <div class="p-6">
                <p>{pages[dockData.currentIndex].text}</p>
            </div>
            <div class="h-18"></div>
        </div>
    </div>
    {#each pages as page}
        {#if page.audio}
            <audio
                id={page.audio.id}
                src={page.audio.url}
                preload="auto"
                onended={() => {
                    dockData.autoplay && onclick({ clientX: 10000 });
                }}
            ></audio>
        {/if}
    {/each}
</main>
