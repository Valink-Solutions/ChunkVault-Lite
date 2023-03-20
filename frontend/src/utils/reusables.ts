import { toast } from '@zerodevx/svelte-toast';
 
function concatenateUint8Arrays(arrays: Uint8Array[]): Uint8Array {
	const totalLength = arrays.reduce((acc, arr) => acc + arr.length, 0);
	const result = new Uint8Array(totalLength);
	let offset = 0;
	for (let i = 0; i < arrays.length; i++) {
		result.set(arrays[i], offset);
		offset += arrays[i].length;
	}
	return result;
}

export async function downloadSnapshot(snapshot_id: string, num_parts: number, filename: string) {
  const chunks: Uint8Array[] = [];

  const loadingToastId = toast.push('Downloading...', {
    duration: 0,
    initial: 0,
    next: 0,
    dismissable: false,
  });

  // Divide the parts into groups of 5 and download each group in parallel
  const num_groups = Math.ceil(num_parts / 20);
  const group_promises = [];
  for (let i = 0; i < num_groups; i++) {
    const start_part = i * 20 + 1;
    const end_part = Math.min(start_part + 19, num_parts);
    const group_promise = Promise.all(
      Array.from({ length: end_part - start_part + 1 }, async (_, j) => {
        const response = await fetch(`/api/snapshots/${snapshot_id}/download?part=${start_part + j}`);
        const buffer = await response.arrayBuffer();
        const uint8Array = new Uint8Array(buffer);

        // Update the loading toast progress
        const progress = (i * 20 + j + 1) / num_parts;
        toast.set(loadingToastId, { next: progress });

        return uint8Array;
      })
    );
    group_promises.push(group_promise);
  }

  // Concatenate the byte arrays for each group into a single byte array
  const group_chunks = await Promise.all(group_promises);
  for (let i = 0; i < num_groups; i++) {
    chunks.push(concatenateUint8Arrays(group_chunks[i]));
  }
  const concatenated = concatenateUint8Arrays(chunks);

  // Create a blob object from the concatenated array
  const blob = new Blob([concatenated], { type: 'application/zip' });

  // Download the blob with the specified filename
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename;

  // Dismiss the loading toast
  toast.set(loadingToastId, { next: 1 });

  // Delay the download for 1 second to ensure the blob is fully created
  setTimeout(() => {
    link.click();
  }, 1000);
}

  

export function formatBytes(bytes: number): string {
	if (bytes < 1024) {
		return bytes + ' bytes';
	} else if (bytes < 1048576) {
		return (bytes / 1024).toFixed(2) + ' KB';
	} else if (bytes < 1073741824) {
		return (bytes / 1048576).toFixed(2) + ' MB';
	} else {
		return (bytes / 1073741824).toFixed(2) + ' GB';
	}
}

export function formatDifficulty(difficulty: number): string {
	let parsed_difficulty = 'Peaceful';

	if (difficulty == 0) {
		parsed_difficulty = 'Peaceful';
	} else if (difficulty == 1) {
		parsed_difficulty = 'Easy';
	} else if (difficulty == 2) {
		parsed_difficulty = 'Normal';
	} else if (difficulty == 3) {
		parsed_difficulty = 'Hard';
	} else {
		parsed_difficulty = 'Hardcore';
	}

	return parsed_difficulty;
}
