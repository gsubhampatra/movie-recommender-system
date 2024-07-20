
# Movie Recommender System

This is a Movie Recommender System web application built using Streamlit. The application recommends movies based on a selected movie and also displays their posters using data fetched from The Movie Database (TMDb) API.

## Features

- **Movie Recommendations:** Get top 5 similar movies based on the selected movie.
- **Movie Posters:** View posters of the recommended movies.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommender-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd movie-recommender-system
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the web application in your browser. It will be available at `http://localhost:8501`.
2. Select a movie from the dropdown menu.
3. Click the "Recommend" button to get a list of recommended movies along with their posters.

## Files

- `app.py`: The main application file.
- `movies.pkl`: Pickle file containing movie data.
- `similarity.pkl`: Pickle file containing similarity matrix.
- `requirements.txt`: File containing the list of required Python packages.

## Dependencies

- `streamlit`
- `pandas`
- `requests`
- `pickle`

You can install the dependencies using the command:
```bash
pip install -r requirements.txt
```

## API Key

This project uses The Movie Database (TMDb) API to fetch movie posters. You need to have an API key from TMDb. Replace `YOUR_API_KEY` in the `fetch_poster` function with your actual API key.

```python
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [The Movie Database (TMDb)](https://www.themoviedb.org/)

Feel free to contribute to the project by submitting issues or pull requests. Happy coding!
```

Replace `YOUR_API_KEY` with your actual TMDb API key. If you have a `requirements.txt` file, ensure it lists all the necessary dependencies. If not, you can create it by running:

```bash
pip freeze > requirements.txt
```

