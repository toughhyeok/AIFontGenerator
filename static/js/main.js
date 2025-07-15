document.addEventListener('DOMContentLoaded', function () {
    const keywordBtns = document.querySelectorAll('.keyword-btn');
    const keywordInput = document.getElementById('keywordInput');
    const generateBtn = document.getElementById('generate-btn');
    const fontPreviewText = document.getElementById('font-preview-text');

    let selectedKeywords = [];

    keywordBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const keyword = btn.textContent;
            if (selectedKeywords.includes(keyword)) {
                selectedKeywords = selectedKeywords.filter(k => k !== keyword);
                btn.classList.remove('btn-success');
                btn.classList.add('btn-primary');
            } else {
                selectedKeywords.push(keyword);
                btn.classList.remove('btn-primary');
                btn.classList.add('btn-success');
            }
            keywordInput.value = selectedKeywords.join(', ');
        });
    });

    generateBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const keywords = keywordInput.value.split(',').map(k => k.trim()).filter(k => k);
        if (keywords.length === 0) {
            alert('Please select or enter at least one keyword.');
            return;
        }

        fontPreviewText.textContent = `Generating font with keywords: ${keywords.join(', ')}...`;
        fontPreviewText.style.fontFamily = 'sans-serif';

        fetch('/generate-font', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ keywords: keywords }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.font_path) {
                const fontName = `GeneratedFont_${Date.now()}`;
                const newStyle = document.createElement('style');
                newStyle.appendChild(document.createTextNode(`
                    @font-face {
                        font-family: '${fontName}';
                        src: url('${data.font_path}');
                    }
                `));
                document.head.appendChild(newStyle);

                fontPreviewText.textContent = 'The quick brown fox jumps over the lazy dog';
                fontPreviewText.style.fontFamily = `'${fontName}', sans-serif`;
            } else {
                fontPreviewText.textContent = 'Error generating font.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            fontPreviewText.textContent = 'Error generating font.';
        });
    });
});
