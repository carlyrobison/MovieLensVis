# matrix factorization!

import data_io
import prob2utils as svd
import numpy as np

k = 20 # size of matrix


def get_internal_matrices(Y, K):
    '''Returns U and V from factorizing Y.'''
    M = max([d[0] for d in Y]) + 1 # number of users
    N = max([d[1] for d in Y]) + 1 # number of movies

    reg = 10**-3
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
    print proj[movie_id]
    return proj[movie_id]

if __name__ == '__main__':
    movie_names, movie_genres, genres  = data_io.read_movies('movies.txt')
    Y, movie_ratings = data_io.read_ratings('data.txt', movie_names)
    
    # if we're calculating U and V again. Otherwise just read from the file.
    # U, V = get_internal_matrices(Y, k)
    # data_io.save_matrix(U, 'savedU.txt')
    # data_io.save_matrix(V, 'savedV.txt')

    # if we're calculating the projection again.
    # Vnew = data_io.load_matrix('savedV.txt')
    # Vproj = get_projection(Vnew)
    # data_io.save_matrix(Vproj, 'savedProj.txt')

    X = data_io.load_matrix('savedProj.txt')
    print X.shape

    for i in movie_names.keys()[:10]:
        print i
        print movie_names[i], get_movie_point(X, int(i))

