<script lang="ts">
    import colorcodes from '../assets/colorcodes.json';

    let canvas: HTMLCanvasElement;
    let ctx: CanvasRenderingContext2D;
    const SCALE = 100;

    function hexToRgb(hex: string) {
        const bigint = parseInt(hex.slice(1), 16);
        return {
            r: (bigint >> 16) & 255,
            g: (bigint >> 8) & 255,
            b: bigint & 255
        };
    }

    function colorDistance(c1: any, c2: any): number {
        return Math.sqrt(
            Math.pow(c1.r - c2.r, 2) +
            Math.pow(c1.g - c2.g, 2) +
            Math.pow(c1.b - c2.b, 2)
        );
    }

    function findNearestColor(r: number, g: number, b: number): string {
        let nearest = '';
        let minDist = Infinity;
        for (const dye of Object.values(colorcodes)) {
            for (const hex of Object.values(dye)) {
                const target = hexToRgb(hex);
                const dist = colorDistance({ r, g, b }, target);
                if (dist < minDist) {
                    minDist = dist;
                    nearest = hex;
                }
            }
        }
        return nearest;
    }

    function processImage(e: Event) {
        const file = (e.target as HTMLInputElement).files?.[0];
        if (!file) return;

        const img = new Image();
        img.onload = () => {
            const originalW = img.width;
            const originalH = img.height;

            // 캔버스 크기 → 100배 확대
            canvas.width = originalW * SCALE;
            canvas.height = originalH * SCALE;
            ctx = canvas.getContext('2d')!;

            // 임시 캔버스에서 원본 픽셀 가져오기
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = originalW;
            tempCanvas.height = originalH;
            const tempCtx = tempCanvas.getContext('2d')!;
            tempCtx.drawImage(img, 0, 0, originalW, originalH);

            const imageData = tempCtx.getImageData(0, 0, originalW, originalH);
            const data = imageData.data;

            for (let y = 0; y < originalH; y++) {
                for (let x = 0; x < originalW; x++) {
                    const i = (y * originalW + x) * 4;
                    const r = data[i];
                    const g = data[i + 1];
                    const b = data[i + 2];
                    const nearest = hexToRgb(findNearestColor(r, g, b));

                    ctx.fillStyle = `rgb(${nearest.r}, ${nearest.g}, ${nearest.b})`;
                    ctx.fillRect(x * SCALE, y * SCALE, SCALE, SCALE); // 픽셀 확대
                }
            }
        };
        img.src = URL.createObjectURL(file);
    }


    function handleDownload() {
        const link = document.createElement('a');
        link.download = 'converted_100x.png';
        link.href = canvas.toDataURL('image/png', 1.0);
        link.click();
    }
</script>

<style>
  canvas {
    max-width: 100%;
    border: 1px solid #ccc;
  }
</style>

<div class="alert alert-danger">
  <b>⚠️ 이용시 주의사항</b>
  <ul class="mb-0">
    <li><b>픽셀 이미지</b>만 업로드하세요. 큰 이미지는 브라우저가 멈출 수 있습니다.</li>
    <li>색상은 거리 기반으로 계산되므로 참고용입니다.</li>
    <li>다운로드시 <b>100배 확대된 이미지</b>가 저장됩니다.</li>
  </ul>
</div>

<input type="file" accept="image/*" on:change={processImage} class="mt-3" /><br />
<canvas bind:this={canvas} class="mt-4"></canvas><br />
<button class="btn btn-primary" on:click={handleDownload}>다운로드</button>
