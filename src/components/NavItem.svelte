<script>
  import { link, useMatch } from "svelte-navigator";
  export let href;
  export let text;
  export let disabled = false;

  const match = useMatch(href);
</script>

<li class="nav-item">
  {#if disabled}
    <a class="nav-link disabled" aria-disabled="true" {href} use:link>{text}</a>
  {:else if $match}
    <a class="nav-link active" aria-current="page" {href} use:link>{text}</a>
  {:else}
    <a class="nav-link" {href} use:link>{text}</a>
  {/if}
</li>