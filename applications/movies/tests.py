from rest_framework.test import APITestCase

class MoviesTestCase(APITestCase):
    
    def test_create_movie(self):
        expectedResponse = {
            "id": 1,
            "title": "Spotlight",
            "release_date": "2017-06-14",
            "genre": "Thriller",
            "plot": "unos periodistas etc",
            "average_rating": 0,
            "ratings": []
        }
        data = {
        "title": "Spotlight",
        "release_date": "2017-06-14",
        "genre": "Thriller",
        "plot": "unos periodistas etc"
        }
        response = self.client.post("/movies/movies/", data, format="json")
        assert response.data == expectedResponse

    def test_order_by_avg_rating(self):

        data1 = {
                "title": "Spotlight",
                "release_date": "2017-06-14",
                "genre": "Thriller",
                "plot": "unos periodistas etc",
                "ratings": [
                    {
                        "rating": 5,
                        "comment": "bueno",
                    },
                    {
                        "rating": 5,
                        "comment": "good"
                    }
                ]
            }   
        data2 = {
                "title": "interstellar",
                "release_date": "2014-06-14",
                "genre": "sci-fi",
                "plot": "matiu va al espacio",
                "ratings": [
                    {
                        "rating": 3,
                        "comment": "great",
                    },
                    {
                        "rating": 5,
                        "comment": "excelent"
                    }
                ]
            }         
        self.client.post("/movies/movies/", data1, format="json")
        self.client.post("/movies/movies/", data2, format="json")
        
        response = self.client.get("http://127.0.0.1:8000/movies/movies/", None, **{'HTTP_SEARCHSORT': 'ascRating'})
        assert response.data[0]['title'] == 'interstellar'
        assert response.data[1]['title'] == 'Spotlight'

 


