const savedCharacterData = JSON.parse(localStorage.getItem('characterData'));
//Just checking if the data transfered over and is successful
if (savedCharacterData) {
    console.log("Character Data:", savedCharacterData);
    } else {
        console.log("No character data found.");
        alert('No Character Data Avaliable: Redirecting to Character Creation...')
        window.location.href = '../personal.html';
}
savedCharacterData.phase = '1';
function downloadChar() {
    const filename = prompt("Enter the filename to save under:", `${savedCharacterData.name}.json`);
    if (filename) {
        const characterDataJSON = JSON.stringify(savedCharacterData, null, 2);
        const fileData = filename.endsWith('.txt') ? `Character Data:\n\n${characterDataJSON}` : characterDataJSON;
        const blob = new Blob([fileData], { type: filename.endsWith('.txt') ? 'text/plain' : 'application/json' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        link.click();
    } else {
        alert("Download Cancelled, or filename not found.");
    }
}
