# matrix factorization!

import data_io
import prob2utils as svd
import numpy as np
import basic_histograms as stats
import diagrams as diag
import random

k = 20 # size of matrix


def get_internal_matrices(Y, K):
    '''Returns U and V from factorizing Y.'''
    M = max([d[0] for d in Y]) + 1 # number of users
    N = max([d[1] for d in Y]) + 1 # number of movies

    reg = .1 # used data set from last week
    eta = 0.01 # initially .03
    U, V, err = svd.train_model(M, N, K, eta, reg, Y)
    print err
    print V
    return U, V

def get_projection(V):
    '''Gets the projection of V into the two dimensions with the most variation in the data.'''
    A, E, B = np.linalg.svd(V)
    Vproj = np.dot(A.transpose()[:2], V)
    return Vproj.transpose()

def get_movie_point(proj, movie_id):
    # print proj[movie_id]
    pt = proj[movie_id]
    return pt[0], pt[1]

def plot_movie_ids(title, ids, X):
    movie_data = []
    for m in ids:
        x, y = get_movie_point(X, int(m))
        movie_data.append((ensure_unicode(movie_names[m]), x, y))

    diag.plot_movies(movie_data, title)

def plot_popular(X, movie_names, movie_ratings):
    mvs = stats.top_ten_popular(movie_ratings)
    print "most popular movies:", [movie_names[m] for m in mvs]

    plot_movie_ids("Most Popular Movies", mvs, X)

def plot_highest_rated(X, movie_names, movie_ratings):
    mvs = stats.top_ten_rated(movie_ratings)
    print "highest rated movies:", [movie_names[m] for m in mvs]

    plot_movie_ids("Highest Rated Movies", mvs, X)

def plot_genres(X, movie_names, movie_ratings, genres):
    for k in genres.keys():
        v = list(genres[k])
        num_samples = min(20, len(v))
        plot_movie_ids("Genre: " + str(k), random.sample(list(v), num_samples), X)

def ensure_unicode(v): # needed bc weird errors
    if isinstance(v, str):
        v = v.decode('latin-1')
    return unicode(v)  # convert anything not a string to unicode too

if __name__ == '__main__':
    movie_names, movie_genres, genres  = data_io.read_movies('movies.txt')
    Y, movie_ratings = data_io.read_ratings('data.txt', movie_names)
    
    # #if we're calculating U and V again. Otherwise just read from the file.
    # U, V = get_internal_matrices(Y, k)
    # data_io.save_matrix(U, 'savedU.txt')
    # data_io.save_matrix(V, 'savedV.txt')

    # #if we're calculating the projection again.
    # Vnew = data_io.load_matrix('savedV.txt')
    # Vproj = get_projection(Vnew)
    # data_io.save_matrix(Vproj, 'savedProj.txt')

    X = data_io.load_matrix('savedProj.txt')
    # print X.shape

    plot_popular(X, movie_names, movie_ratings)
    plot_highest_rated(X, movie_names, movie_ratings)
    plot_genres(X, movie_names, movie_ratings, genres)

    try:
        diag.show_plots()
    except:
        pass
