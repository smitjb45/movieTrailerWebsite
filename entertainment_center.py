import media
import fresh_tomatoes

# Four instances of the Movies Class are created here
shrek = media.Movie("Shrek (2001)", 
                    "After his swamp is filled with magical creatures, Shrek agrees to" + 
                    "rescue Princess Fiona for a villainous lord in order to get his land back.", 
                    "http://www.movieposter.com/posters/archive/main/97/MPW-48589", 
                    "https://www.youtube.com/watch?v=ooJJX3R42WM"
                    )
                    
endless_summer = media.Movie("The Endless Summer (1968)",
                    "Filmmaker/narrator Bruce Brown follows two surfers, Mike Hynson and Robert August, on a surfing trip around the world", 
                    "http://mrdoveton.com/wp-content/uploads/2013/12/1-ENDLESS_SUMMER_45TH.jpg", 
                    "https://www.youtube.com/watch?v=yZsuQXKkPdw"
                    )
                    
degrees_south = media.Movie("180 South (2010)", 
                    "Conquerors of the Useless follows Jeff Johnson as he retraces the epic 1968" +
                    " journey of his heroes Yvon Chouinard and Doug Tompkins to Patagonia", 
                    "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/180_South.jpg/220px-180_South.jpg", 
                    "https://www.youtube.com/watch?v=NK3TOHLFL50"
                    )
                    
star_wars = media.Movie("Star Wars (1977)", 
                    " The Rebel Alliance, led by Princess Leia (Fisher), and its attempt to destroy" + 
                    " the Galactic Empire's space station, the Death Star.", 
                    "http://www.followingthenerd.com/site/wp-content/uploads/Star_Wars_A_New_Hope_OGN_Cover.jpg", 
                    "https://www.youtube.com/watch?v=nywPf1p-BBY"
                    )

# Created a list to put instances in and pass into the open movies function
movies = [shrek, endless_summer, degrees_south, star_wars]

fresh_tomatoes.open_movies_page(movies)