# importing data from the input files
import numpy as np

genre_labels = ['Unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'FilmNoir', 'Horror', 'Musical', 'Mystery', 'Romance', 'SciFi', 'Thriller', 'War', 'Western']

def read_movies(filename):
    '''
    Gets movies and their genres from the given file.
    '''
    movie_names = {} # movie ID to name
    movie_genres = {} # indexed by movie ID
    genres = {} # genre name to set of IDs

    # create the genre fields
    for g in genre_labels:
        genres[g] = set([])

    with open(filename, 'rU') as f:
        for line in f:
            d = line.strip('\n').split('\t')

            # extract stuff
            movie_id = d[0]
            title = d[1]
            genre = [genre_labels[i] for i in range(19) if d[i + 2] == '1']

            # add the info to the relevant db
            movie_names[movie_id] = title
            movie_genres[movie_id] = genre
            for g in genre:
                genres[g].add(movie_id)

    # return it
    return movie_names, movie_genres, genres

def read_ratings(filename, movie_names):
    '''
    Gets users and their ratings for movies from the given file
    '''
    Y = [] # the input data

    movie_ratings = {}

    # aggregate ratings by movie
    for m in movie_names.keys():
        movie_ratings[m] = []

    with open(filename, 'rU') as f:
        for line in f:
            d = line.strip('\n').split('\t')

            # extract stuff
            user_id = int(d[0])
            movie_id = d[1]
            rating = int(d[2])

            # add the info to the relevant db
            Y.append([user_id, int(movie_id), rating])
            movie_ratings[movie_id].append(rating)

    # return it
    return np.asarray(Y), movie_ratings

def save_matrix(V, filename):
    '''Dump trained matrix into a file'''
    np.savetxt(filename, V, fmt='%f')

def load_matrix(filename):
    '''Load dumped matrix from file'''
    return np.loadtxt(filename, dtype=float)



if __name__ == '__main__':
    movie_names, movie_genres, genres  = read_movies('movies.txt')
    Y, movie_ratings = read_ratings('data.txt', movie_names)
    #print "movies:", [movies[d] for d in movies.keys()[:10]]
    # print "genres:", genres[:10]