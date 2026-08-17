let player = null;
let youtubeReady = false;


// ==========================================
// YOUTUBE PLAYER
// ==========================================

function onYouTubeIframeAPIReady() {

    player = new YT.Player("youtube-player", {

        height: "1",
        width: "1",

        // CHANGE THIS TO YOUR YOUTUBE VIDEO ID
        videoId: "7gXmq3WScTYM_W-v",

        playerVars: {
            autoplay: 0,
            controls: 0,
            loop: 1,
            playlist: "7gXmq3WScTYM_W-v",
            playsinline: 1,
            rel: 0
        },

        events: {
            onReady: function () {

                youtubeReady = true;

                console.log("YouTube player is ready.");

            },

            onStateChange: function (event) {

                // If the song finishes, play it again
                if (event.data === YT.PlayerState.ENDED) {

                    player.playVideo();

                }

            }

        }

    });

}


// ==========================================
// OPEN LETTER BUTTON
// ==========================================

function openLetter() {

    // Start music
    if (youtubeReady && player) {

        player.unMute();

        player.setVolume(100);

        player.playVideo();

    } else {

        console.log("YouTube player is not ready yet.");

    }


    // Scroll to letter
    const letter = document.getElementById("letter");

    if (letter) {

        letter.scrollIntoView({
            behavior: "smooth"
        });

    }

}