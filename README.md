<h1>Movie Recommender Using Machine Learning - Content-Based Approach</h1>

<p>This project is a Movie Recommender System that utilizes machine learning and a content-based approach to suggest movies to users based on their preferences. The system employs vectorized text data to understand the content of movies and provide recommendations. The recommendations are presented through a user-friendly interface created using Streamlit.</p>

https://github.com/AyushKumarBar/movie-recommender-using-ml/assets/95698835/6d0435e6-15d0-4298-b262-8c0686dd99ef





<h2>Table of Contents</h2>
<ul>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#model">Model</a></li>
    <li><a href="#streamlit-interface">Streamlit Interface</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
</ul>

<h2 id="installation">Installation</h2>

<ol>
    <li>Clone this repository to your local machine.</li>
    <pre><code>git clone https://github.com/AyushKumarBar/movie-recommender-using-ml.git</code></pre>
    <li>Navigate to the project directory.</li>
    <pre><code>cd movie-recommender</code></pre>
    <li>Create a virtual environment. (Optional but recommended)</li>
    <pre><code>python3 -m venv venv<br>source venv/bin/activate</code></pre>
    <li>Install the required packages.</li>
    <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h2 id="usage">Usage</h2>

<ol>
    <li>After installing the necessary packages, run the Streamlit app.</li>
    <pre><code>streamlit run app.py</code></pre>
    <li>The web interface will open in your default web browser.</li>
    <li>Enter the title of a movie you like in the search bar.</li>
    <li>Click on the "Get Recommendations" button.</li>
    <li>The system will display a list of recommended movies similar to your input.</li>
</ol>

<h2 id="data">Data</h2>

<p>The movie data used for this project contains information about various movies, including their titles, genres, and textual descriptions. The descriptions have been preprocessed and vectorized for content analysis.</p>

<h2 id="model">Model</h2>

<p>The recommender system employs a content-based approach. It analyzes the vectorized text data from movie descriptions to identify similarities between movies. Based on the input movie, the system suggests movies with similar content, aiming to provide recommendations that align with the user's preferences.</p>

<h2 id="streamlit-interface">Streamlit Interface</h2>

<p>The Streamlit interface provides a straightforward way for users to interact with the recommender system. Users can input a movie title, and the system will generate a list of recommended movies based on content similarity.</p>


<h2 id="conclusion">Conclusion</h2>

<p>This Movie Recommender System demonstrates the use of machine learning and content-based techniques to offer personalized movie recommendations. By analyzing the textual content of movies, the system suggests similar movies, providing users with a convenient way to discover new films aligned with their interests.</p>

<p>Feel free to contribute to this project by adding more features, improving the recommendation algorithm, or enhancing the user interface. Happy coding!</p>

<hr>



![Screenshot 2023-08-26 163637](https://github.com/AyushKumarBar/movie-recommender-using-ml/assets/95698835/63225cce-68d9-415f-b747-8cb13ba0d2dc)
