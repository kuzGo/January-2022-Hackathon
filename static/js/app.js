// Play and pause buttons
const play = document.querySelector(".play"),
    pause = document.querySelector(".pause");
// Audio element
const audio = document.querySelector(".audio audio");
// Video and season 
const seasons = document.querySelectorAll(".season"),
    video = document.querySelector(".video video");
// Duration
const durations = document.querySelectorAll(".duration");
// 
const path = document.querySelector(".rect"),
    remainingTimeEl = document.querySelector(".audio-remaining-time");
const pathLength = path.getTotalLength();
path.style.strokeDasharray = pathLength;
// Default auddio duration
let audioDuration = 120; // 2min

// Play audio
play.addEventListener("click", () => {
    audio.play();
    update();
});
// Pause audio
pause.addEventListener("click", () => {
    audio.pause();
});

// Toggling videos
seasons.forEach((season) => {
    season.addEventListener("click", () => {
        video.src = season.getAttribute("video-src");
    });
});
// Audio duration changing
durations.forEach((duration) => {
    duration.addEventListener("click", () => {
        audioDuration = duration.getAttribute("audio-duration");
        update();
    });
});

function update() {
    if (audio.currentTime >= audioDuration) {
        audio.pause(); // pause audio
        audio.currentTime = 0; // stop audio
    }

    // PORTION PLAYED FROM THE AUDIO
    let portionPlayed = audio.currentTime / audioDuration;

    // STROKE DASHOFFSET IS PROPOTIONAL TO the portionPlayed
    path.style.strokeDashoffset = -portionPlayed * pathLength;

    // CALCULATE REMAINING TIME IN SEC
    let remainingTimeInSec = audioDuration - audio.currentTime;
    renderRemainingTime(remainingTimeInSec);

    if (!audio.paused) {
        requestAnimationFrame(update);
        console.log("update");
    }
}
update();

// RENDER REMAINING TIME
function renderRemainingTime(timeInSec) {
    let min = Math.floor(timeInSec / 60);
    let sec = Math.floor(timeInSec % 60);

    // IF min/sec is a single digit(ex:9) we add a zero before the digit. (ex: 9 becomes 09)
    min = min < 10 ? `0${min}` : min;
    sec = sec < 10 ? `0${sec}` : sec;

    remainingTimeEl.innerHTML = `${min}:${sec}`;
}