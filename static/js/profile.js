document.addEventListener('DOMContentLoaded', () => {
    const profileContainer = document.querySelector('.trainer-profile');
    const trainerID = profileContainer.getAttribute('data-trainer-id');
    const USER_ID = profileContainer.getAttribute('data-user-id');

    const favoriteButton = document.querySelector('.favorite-btn');

    if (favoriteButton) {
        favoriteButton.addEventListener('click', () => {
            const trainerId = favoriteButton.getAttribute('data-trainer-id');
            toggleFavorite(trainerId, favoriteButton);
        });
    }

    async function toggleFavorite(trainerId, button) {
        try {
            const response = await fetch(`/api/favorite-trainer/${trainerId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                }
            });

            if (response.ok) {
                const data = await response.json();
                if (data.message === 'Trainer added to favorites!') {
                    button.textContent = 'Already in Favorites';
                } else if (data.message === 'Trainer removed from favorites!') {
                    button.textContent = 'Add to Favorites';
                }
            } else {
                const errorData = await response.json();
                alert(errorData.error || 'An error occurred.');
            }
        } catch (error) {
            console.error('Error:', error);
            window.location.href = '/accounts/login/';
            alert('Failed to toggle favorite. Please try again later.');
        }
    }

    document.querySelectorAll('.fa-star').forEach(star => {
        star.addEventListener('click', async function() {
            const ratingValue = this.getAttribute('data-value');
            try {
                const response = await submitRating(ratingValue, trainerID);
                const data = await response.json();

                if (response.ok) {
                    updateStars(trainerID);
                    alert('Rating submitted');
                }
            } catch (error) {
                alert('Error: You may have already rated this trainer or have not logged in yet');
                window.location.href = '/accounts/login/';
                console.error('Error posting rating:', error);
            }
        });
    });

    async function submitRating(ratingValue, trainerId) {
        const response = await fetch(`/api/ratings/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({
                user: USER_ID,
                trainer: trainerId,
                rating: ratingValue,
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to submit rating');
        }

        return response;
    }

    async function getUserRating(trainerId) {
        try {
            const response = await fetch(`/api/ratings/${trainerId}/user-rating/`);
            const data = await response.json();

            if (response.ok && data.rating !== null) {
                return data.rating;
            } else {
                return 0;
            }
        } catch (error) {
            console.error('Error fetching rating:', error);
            return 0;
        }
    }

    async function updateStars(trainerId) {
        const rating = await getUserRating(trainerId);

        document.querySelectorAll('.fa-star').forEach(star => {
            star.classList.remove('selected');
            star.classList.remove('hover');
            star.classList.remove('no-hover');
        });

        for (let i = 0; i < rating; i++) {
            document.querySelectorAll('.fa-star')[i].classList.add('selected');
        }

        if (rating > 0) {
            document.querySelectorAll('.fa-star').forEach(star => {
                star.classList.add('no-hover');
            });
        }
    }

    updateStars(trainerID);
});
