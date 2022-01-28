const app = document.querySelector(".app");
const inactiveTime = 3000; // 3sec
let mouseLastMoveTime = new Date();

document.addEventListener("mousemove", () => {
    mouseLastMoveTime = new Date();
    app.classList.remove("inactive");
    document.body.style.cursor = "auto";
});

function deactivateApp() {
    // Check if the user was inactive for a certain amount of time
    let now = new Date();
    let deltaTime = now - mouseLastMoveTime;

    if (deltaTime >= inactiveTime) {
        app.classList.add("inactive");
        document.body.style.cursor = "none";
    }
    requestAnimationFrame(deactivateApp);
}
deactivateApp();