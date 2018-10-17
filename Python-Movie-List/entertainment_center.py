import fresh_tomatoes
import media

christopher_robin = media.Movie("Christoper Robin",
                        "A working-class family man, Christopher Robin, encounters his childhood friend Winnie-the-Pooh, who helps him to rediscover the joys of life.",
                        "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.playpartyplan.com%2Fwp-content%2Fuploads%2F2018%2F05%2FChristopher-Robin-movie-trailer-3.jpg&f=1",
                        "https://www.youtube.com/watch?v=0URpDxIjZrQ&t=1s")

black_panther = media.Movie("Black Panther",
                     "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.",
                     "https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU&t=5s")


breakfast_club = media.Movie("Breakfast Club",
                                  "Five high school students meet in Saturday detention and discover how they have a lot more in common than they thought.",
                                  "https://m.media-amazon.com/images/M/MV5BOTM5N2ZmZTMtNjlmOS00YzlkLTk3YjEtNTU1ZmQ5OTdhODZhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                  "https://www.youtube.com/watch?v=BSXBvor47Zs")

avengers_infinite_war = media.Movie("Avengers Infinite War",
                      "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                      "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=6ZfuNTqbHE8&t=7s")

toy_story = media.Movie("Toy Story",
                           "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                           "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

cool_beans = media.Movie("",
                            "",
                             "",
                             "")

movies =[christopher_robin, black_panther, breakfast_club, avengers_infinite_war, toy_story, cool_beans]
fresh_tomatoes.open_movies_page(movies)
