$(document).ready(function () {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            const movies = data.films;
            movies.forEach(movie => function() {
                $.ajax({
                    url: movie,
                    method: 'GET',
                    sucess: function(mv) {
                        const mv = da.title;
                        $('#list_movies').append(mv);
                    }
                })
            });
            }
        }
    });
});