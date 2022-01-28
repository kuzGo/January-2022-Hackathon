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