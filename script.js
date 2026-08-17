// ================================
// BIRTHDAY MUSIC
// ================================

const youtubeVideoId = "32YzafO9Bmo";

let musicPlaying = false;

const musicButton = document.getElementById("musicButton");
const youtubePlayer = document.getElementById("youtubePlayer");

musicButton.addEventListener("click", function () {

    if (!musicPlaying) {

        youtubePlayer.src =
            "https://www.youtube.com/embed/" +
            youtubeVideoId +
            "?autoplay=1&loop=1&playlist=" +
            youtubeVideoId +
            "&controls=0&rel=0";

        musicPlaying = true;

        musicButton.innerHTML = "🔇 Pause Birthday Song";

    } else {

        youtubePlayer.src = "";

        musicPlaying = false;

        musicButton.innerHTML = "🎵 Play Birthday Song";
    }

});


// ================================
// OPEN LOVE LETTER
// ================================

function openLetter() {

    const letter = document.getElementById("letter");

    if (letter) {

        letter.scrollIntoView({
            behavior: "smooth"
        });

    }

}