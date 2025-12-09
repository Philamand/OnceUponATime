<script>
    import { getContext } from "svelte";

    let currentIndex = $state(0);
    let autoplay = $state(false);
    let width = $state(0);
    let height = $state(0);
    let colClass = $derived(width > height ? "flex-row" : "flex-col");
    const pages = JSON.parse(document.getElementById("pages-data").textContent);

    function onclick(event) {
        if (currentIndex > 0) {
            let audioPlayer = document.getElementById(`audio-${currentIndex}`);
            if (audioPlayer) {
                audioPlayer.pause();
                audioPlayer.currentTime = 0;
            }
        }

        if (
            event.clientX > window.screen.width / 2 &&
            currentIndex < pages.length - 1
        ) {
            currentIndex++;
            let audioPlayer = document.getElementById(`audio-${currentIndex}`);
            if (audioPlayer) {
                audioPlayer.play();
            }
        } else if (
            event.clientX < window.screen.width / 2 &&
            currentIndex > 0
        ) {
            currentIndex--;
        }
    }
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />

<svelte:head>
    {#each pages as page}
        <link rel="preload" as="image" href={page.image} />
    {/each}
</svelte:head>

<main>
    <div
        role="link"
        tabindex={currentIndex}
        {onclick}
        onkeyup={(e) =>
            e.key === "ArrowLeft"
                ? onclick({ clientX: 0 })
                : onclick({ clientX: 10000 })}
        aria-label="Change Page"
        class={["h-screen flex", colClass]}
    >
        <img src={pages[currentIndex].image} alt="Illustration" />
        <div class="h-full w-full flex flex-col justify-center text-center">
            <div class="p-6">
                <p>{pages[currentIndex].text}</p>
                {#if currentIndex === 0}
                    <div class="mt-6 w-full flex justify-center">
                        <fieldset
                            class="fieldset bg-base-100 border-base-300 rounded-box w-64 border p-4"
                        >
                            <legend class="fieldset-legend"
                                >Lecture Automatique</legend
                            >
                            <label class="label">
                                <input
                                    type="checkbox"
                                    bind:checked={autoplay}
                                    class="toggle"
                                />
                                {#if autoplay}
                                    Activée
                                {:else}
                                    Désactivée
                                {/if}
                            </label>
                        </fieldset>
                    </div>
                {/if}
            </div>
        </div>
    </div>
    {#each pages as page}
        {#if page.audio}
            <audio
                id={page.audio.id}
                src={page.audio.url}
                preload="auto"
                onended={() => {
                    autoplay && onclick({ clientX: 10000 });
                }}
            ></audio>
        {/if}
    {/each}
</main>
