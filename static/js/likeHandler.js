document.addEventListener("DOMContentLoaded", () => {
    const likeButtons = document.querySelectorAll(".btn-like-workout");

    likeButtons.forEach((button) => {
        button.addEventListener("click", async (event) => {
            event.preventDefault(); // Prevent default anchor behavior
            const workoutId = button.getAttribute("data-workout-id");
            const isLiked = button.getAttribute("data-liked") === "true";

            try {
                // Send the request to the server
                const response = await fetch(`/api/like-workout/${workoutId}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                    },
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data.message === "Workout liked!") {
                        button.setAttribute("data-liked", "true");
                        updateHeartIcon(button, true); // Update the heart icon to red
                    } else if (data.message === "Workout unliked!") {
                        button.setAttribute("data-liked", "false");
                        updateHeartIcon(button, false); // Update the heart icon to unfilled
                    }
                } else {
                    console.error("Failed to toggle like status");
                }
            } catch (error) {
                console.error("Error toggling like:", error);
            }
        });
    });


    function updateHeartIcon(button, liked) {
        const svgIcon = button.querySelector("svg");
        if (liked) {
            svgIcon.setAttribute("fill", "red");
        } else {
            svgIcon.setAttribute("fill", "none");
        }
    }
});
