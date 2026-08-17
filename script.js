let player;
let musicPlaying = false;

const YOUTUBE_VIDEO_ID = "32YzafO9Bmo";

function onYouTubeIframeAPIReady() {
    player = new YT.Player("youtubePlayer", {
        height: "0",
        width: "0",

        videoId: YOUTUBE_VIDEO_ID,

        playerVars: {
            autoplay: 0,
            controls: 0,
            loop: 1,
            playlist: YOUTUBE_VIDEO_ID
        },

        events: {
            onReady: function () {
                console.log("YouTube music player is ready ❤️");
            }
        }
    });
}


document.getElementById("musicButton").addEventListener("click", function () {

    if (!player) {
        alert("Please wait a few seconds and try again ❤️");
        return;
    }

    if (musicPlaying) {

        player.pauseVideo();

        musicPlaying = false;

        this.innerHTML = "🎵 Play Birthday Song";

    } else {

        player.playVideo();

        musicPlaying = true;

        this.innerHTML = "🔇 Pause Birthday Song";
    }

});


function openLetter() {

    const letter = document.getElementById("letter");

    if (letter) {
        letter.scrollIntoView({
            behavior: "smooth"
        });
    }

}