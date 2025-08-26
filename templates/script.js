
        const urlInput = document.getElementById('urlInput');
        const downloadBtn = document.getElementById('downloadBtn');
        const downloadAudioBtn = document.getElementById('downloadAudioBtn');
        const platformItems = document.querySelectorAll('.platform-item');

        // Download button handler (Video)
        downloadBtn.addEventListener('click', async () => {
            await handleDownload('video');
        });

        // Download button handler (Audio)
        downloadAudioBtn.addEventListener('click', async () => {
            await handleDownload('audio');
        });

        // Unified download handler
        // async function handleDownload(type) {
        //     const url = urlInput.value.trim();
        //     const currentBtn = type === 'video' ? downloadBtn : downloadAudioBtn;
        //     const btnText = currentBtn.querySelector('.btn-text');
        //     const loading = currentBtn.querySelector('.loading');

        //     if (!url) {
        //         alert('Please enter a valid URL');
        //         return;
        //     }
        //     if (!isValidUrl(url)) {
        //         alert('Please enter a valid URL');
        //         return;
        //     }
        //     btnText.style.display = 'none';
        //     loading.classList.add('active');
        //     currentBtn.disabled = true;

        //     try {
        //         const response = await fetch('/download', {
        //             method: 'POST',
        //             headers: { 'Content-Type': 'application/json' },
        //             body: JSON.stringify({ url, type })
        //         });
        //         const result = await response.json();
        //         if (result.status === 'success') {
        //             alert(type === 'video' 
        //                 ? 'Video download completed! Check your downloads folder.' 
        //                 : 'Audio download completed! Check your downloads folder.');
        //         } else {
        //             alert('Download failed: ' + (result.message || 'Unknown error'));
        //         }
        //     } catch (error) {
        //         alert('Download failed. Please try again.');
        //     } finally {
        //         btnText.style.display = 'block';
        //         loading.classList.remove('active');
        //         currentBtn.disabled = false;
        //     }
        // }

        async function handleDownload(type) {
    const url = urlInput.value.trim();
    const currentBtn = type === 'video' ? downloadBtn : downloadAudioBtn;
    const btnText = currentBtn.querySelector('.btn-text');
    const loading = currentBtn.querySelector('.loading');

    if (!url) {
        alert('Please enter a valid URL');
        return;
    }
    if (!isValidUrl(url)) {
        alert('Please enter a valid URL');
        return;
    }
    btnText.style.display = 'none';
    loading.classList.add('active');
    currentBtn.disabled = true;

    try {
        const endpoint = type === 'video' ? '/download_video' : '/download_audio';
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url }) // Remove type from payload since it's determined by the endpoint
        });

        if (response.ok) {
            // Handle file download
            const blob = await response.blob();
            const disposition = response.headers.get('Content-Disposition');
            let filename = 'downloaded_file';
            if (disposition && disposition.includes('filename=')) {
                filename = disposition.split('filename=')[1].replace(/"/g, '');
            }
            const downloadUrl = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(downloadUrl);
            a.remove();

            alert(type === 'video' 
                ? 'Video download completed! Check your downloads folder.' 
                : 'Audio download completed! Check your downloads folder.');
        } else {
            const error = await response.text();
            alert('Download failed: ' + error);
        }
    } catch (error) {
        alert('Download failed: ' + error.message);
    } finally {
        btnText.style.display = 'block';
        loading.classList.remove('active');
        currentBtn.disabled = false;
    }
}

        // Platform click handlers
        platformItems.forEach(item => {
            item.addEventListener('click', () => {
                const platform = item.dataset.platform;
                let placeholder = '';
                
                switch(platform) {
                    case 'youtube':
                        placeholder = 'Paste your YouTube video URL here...';
                        break;
                    case 'instagram':
                        placeholder = 'Paste your Instagram video/reel URL here...';
                        break;
                    case 'threads':
                        placeholder = 'Paste your Threads video URL here...';
                        break;
                    case 'pinterest':
                        placeholder = 'Paste your Pinterest video URL here...';
                        break;
                    case 'facebook':
                        placeholder = 'Paste your Facebook video URL here...';
                        break;
                }
                
                urlInput.placeholder = placeholder;
                urlInput.focus();
                
                // Add a subtle highlight effect
                item.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    item.style.transform = '';
                }, 200);
            });
        });

        // Enter key handler
        urlInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                downloadBtn.click();
            }
        });

        // URL validation
        function isValidUrl(string) {
            try {
                new URL(string);
                return true;
            } catch (_) {
                return false;
            }
        }

        // Simulate download process
        function simulateDownload(url) {
            return new Promise((resolve) => {
                // Simulate processing time
                setTimeout(() => {
                    resolve();
                }, 2000 + Math.random() * 2000);
            });
        }

        // Auto-focus on input
        window.addEventListener('load', () => {
            urlInput.focus();
        });

        // Animate platform icons on load
        window.addEventListener('load', () => {
            platformItems.forEach((item, index) => {
                setTimeout(() => {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px)';
                    item.style.transition = 'all 0.5s ease';
                    
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    }, 100);
                }, index * 100);
            });
        });
    