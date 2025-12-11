<script>
    import { useSwipe } from "svelte-gestures";

    let props = $props();

    function handler(event) {
        if (event.detail.direction === props.direction) {
            window.location.href = props.url;
        }
    }

    const { swipe, onswipe } = useSwipe(
        handler,
        () => ({ timeframe: 500, minSwipeDistance: 50, touchAction: "pan-y" }),
        {},
        true,
    );
</script>

<svelte:body {@attach swipe} {onswipe} />
