
export async function downloadSnapshot(snapshot_id: string, num_parts: number, filename: string) {
    const chunks = [];
    
    // Make requests to the API to download each chunk
    for (let i = 1; i <= num_parts; i++) {
      const xhr = new XMLHttpRequest();
      xhr.open('GET', `/api-v2/snapshot/${snapshot_id}/download?part=${i}`, false);
      xhr.overrideMimeType('application/octet-stream');
      xhr.send(null);
      const chunk = xhr.response;
      
      // Convert the chunk to a Uint8Array and add it to the array
      const uint8Array = new Uint8Array(chunk);
      chunks.push(uint8Array);
    }
    
    // Concatenate the byte arrays into a single array
    const concatenated = new Uint8Array(chunks.reduce((acc, chunk) => acc + chunk.length, 0));
    let offset = 0;
    for (let i = 0; i < chunks.length; i++) {
      concatenated.set(chunks[i], offset);
      offset += chunks[i].length;
    }
    
    // Create a blob object from the concatenated array
    const blob = new Blob([concatenated], { type: 'application/zip' });
    
    // Download the blob with the specified filename
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.click();
}

export function formatBytes(bytes: number): string {

    if (bytes < 1024) {
        return bytes + " bytes";
    } else if (bytes < 1048576) {
        return (bytes / 1024).toFixed(2) + " KB";
    } else if (bytes < 1073741824) {
        return (bytes / 1048576).toFixed(2) + " MB";
    } else {
        return (bytes / 1073741824).toFixed(2) + " GB";
    }
}

export function formatDifficulty(difficulty: number): string {
    let parsed_difficulty = "Peaceful"

    if (difficulty == 0){
        parsed_difficulty = "Peaceful"
    } else if (difficulty == 1){
        parsed_difficulty = "Easy"
    } else if (difficulty == 2){
        parsed_difficulty = "Normal"
    } else if (difficulty == 3){
        parsed_difficulty = "Hard"
    } else {
        parsed_difficulty = "Hardcore"
    }

    return parsed_difficulty
}