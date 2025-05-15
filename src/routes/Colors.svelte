<script lang="ts">
  import colorcodes from '../assets/colorcodes.json';

  // 평탄화: dye + key + hex로 하나의 객체 배열
  const flattened = Object.entries(colorcodes).flatMap(([dye, variants]) =>
    Object.entries(variants).map(([key, hex]) => ({ dye, key, hex }))
  );

  // 3개씩 나누는 함수
  function chunk<T>(arr: T[], size: number): T[][] {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
      result.push(arr.slice(i, i + size));
    }
    return result;
  }

  const rows = chunk(flattened, 8);
</script>

<style>
  .row {
    display: flex;
    gap: 20px;
    margin-bottom: 12px;
  }

  .color-box {
    flex: 1;
    height: 130px;
    border: 1px solid #aaa;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    font-family: monospace;
    text-align: center;
    padding: 8px;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
  }

  .swatch {
    width: 100%;
    height: 70%;
    border-bottom: 1px solid #888;
    border-radius: 6px 6px 0 0;
  }

  .label {
    margin-top: 8px;
  }
</style>

{#each rows as row}
  <div class="row">
    {#each row as { dye, key, hex }}
      <div class="color-box">
        <div class="swatch" style="background-color: {hex};"></div>
        <div class="label">{dye} {key}<br />{hex}</div>
      </div>
    {/each}
  </div>
{/each}
