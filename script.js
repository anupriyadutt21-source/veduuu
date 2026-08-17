let player = null;
let youtubeReady = false;

function onYouTubeIframeAPIReady() {

    player = new YT.Player("youtube-player", {

        height: "1",
        width: "1",

        videoId: "32YzafO9Bmo",

        playerVars: {
            autoplay: 0,
            controls: 0,
            loop: 1,
            playlist: "32YzafO9Bmo",
            playsinline: 1,
            rel: 0
        },

        events: {
            onReady: function () {
                youtubeReady = true;
                console.log("Music player ready");
            }
        }

    });
}


function openLetter() {

    if (youtubeReady && player) {
        player.unMute();
        player.setVolume(100);
        player.playVideo();
    }

    const letter = document.getElementById("letter");

    if (letter) {
        letter.scrollIntoView({
            behavior: "smooth"
        });
    }

}