Deep Learning Music Recommendation Engine
Thinkful Data Science Final Capstone
Data Wrangling
Get our song data from Spotify.
* Use spotiPy wrapper for Spotify API and song IDs from two user-generated playlists (liked/disliked songs).
* Playlists simulate user preference data Spotify collects for all users.
* Assign target values to each song based on preference:
* Song "likes" will be assigned target value of 0.
* Song "dislikes" will have a target value of 1.
With song IDs, pass to spotiPy and get Spotify's audio features for each song.
* Features include numeric measures: "acousticness", "energy", "dancability"
* musical qualities: "mode" and "tempo"
* spotiPy can get additional information: "popularity" score (numeric), "explicit" boolean, artist and track names.
With artist and track info the Lyrics Genius API can get lyric strings for each song.
Perform supervised modeling on audio features and NLP on lyrics.


Lyric NLP
Clean and parse lyrics with spaCy.
* Remove music terminology (radio edit, remix, featuring, recorded live at... etc.)
* Multiple versions of songs (covers, live recordings, etc)
* LyricsGenius API sometimes returns very long text files instead of lyrics:( text of Angela's Ashes and Venus in Furs, script of Pulp Fiction)
Generate features for NLP model.
* Bag of Words method with the 1024 most common words.


As a Supervised Problem
Model audio features
Model selection (L1/L2 Regularization,  Decision Tree, K-Nearest Neighbors, Random Forest, Multilayer Perceptron, Gradient Boosting)
Hyperparameter tuning of final model
As an Unsupervised Problem
Cluster feature sets (Spotify audio features, lyric bag of words) to generate labels
Create new supervised model with cluster labels and target value
Compare performance to previous supervised model


As a Deep Learning Problem
Generate contextual embedding vectors with ELMo
Model embeddings with a neural network using Keras and compared to previous models.


Recommendation Engine
Compute similarity (cosine similarity) of songs using contextual embeddings and audio features
Generate song recommendations based on cosine similarity of embeddings and audio features, compare results.