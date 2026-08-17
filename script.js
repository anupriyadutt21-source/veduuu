let player;

function onYouTubeIframeAPIReady() {

    player = new YT.Player("youtube-player", {

        height: "1",

        width: "1",

        videoId: "7gXmq3WScTYM_W-v",

        playerVars: {

            autoplay: 0,

            controls: 0,

            loop: 1,

            playlist: "7gXmq3WScTYM_W-v"

        },

        events: {

            onReady: function () {

                console.log("Music player ready");

            }

        }

    });

}


function openLetter() {

    if (player) {

        player.playVideo();

    }

    document
        .getElementById("letter")
        .scrollIntoView({
            behavior: "smooth"
        });

}