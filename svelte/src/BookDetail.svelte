<script>
    import { onMount } from "svelte";
    import { useSwipe } from "svelte-gestures";
    import { dockData } from "./dock_data.svelte";

    let loading = $state(true);
    let width = $state(0);
    let height = $state(0);
    let colClass = $derived(width > height ? "flex-row" : "flex-col");
    const pages = JSON.parse(document.getElementById("pages-data").textContent);
    let progress_count = $state(0);
    let last_time = 0;

    onMount(async () => {
        const promises = pages.map((page) => {
            return new Promise((resolve, reject) => {
                const img = new Image();
                img.src = page.image;

                img.onload = () => {
                    progress_count++;
                    resolve(page.image);
                };

                img.onerror = () => {
                    progress_count++;
                    console.log(`Failed to fetch ${page.image}`);
                    resolve(page.image);
                };
            });
        });

        await Promise.all(promises);
        await new Promise((resolve) => setTimeout(resolve, 300));
        loading = false;
    });

    function onclick(event) {
        const current_time = performance.now();
        if (current_time - last_time > 500) {
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
                event.clientX > window.screen.width / 4 &&
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
                event.clientX < window.screen.width / 4 &&
                dockData.currentIndex > 0
            ) {
                dockData.currentIndex--;
            }
            last_time = current_time;
        }
    }

    function swipeHandler(event) {
        if (event.detail.direction === "right") {
            onclick({ clientX: 0 });
        } else {
            onclick({ clientX: 10000 });
        }
    }

    const { swipe, onswipe } = useSwipe(
        swipeHandler,
        () => ({ timeframe: 500, minSwipeDistance: 50, touchAction: "pan-y" }),
        {},
        true,
    );
</script>

<svelte:window bind:innerWidth={width} bind:innerHeight={height} />

<main>
    {#if !loading}
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
            {@attach swipe}
            {onswipe}
        >
            <img src={pages[dockData.currentIndex].image} alt="Illustration" />
            <div class="h-full w-full flex flex-col justify-center text-center">
                <div class="p-6">
                    <p>{pages[dockData.currentIndex].text}</p>
                </div>
                <div class="h-18"></div>
            </div>
        </div>
    {:else}
        <div class="h-screen w-full flex flex-col justify-center">
            <div class="w-full flex justify-center mb-4">
                <span class="loading loading-ring loading-xl"></span>
            </div>
            <div class="w-full flex justify-center">
                <progress
                    class="progress progress-primary w-56"
                    value={progress_count}
                    max={pages.length}
                ></progress>
            </div>
        </div>
    {/if}

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
