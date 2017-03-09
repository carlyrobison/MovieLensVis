# importing data from the input filed
import numpy as np

def read_movies(filename):
    '''
    Gets movies and their genres from the given file.
    '''
    movies = dict({})
    genres = dict({})

    # data = [d.split('\t') for d in np.genfromtxt(filename, delimiter = '\r')]
    # for d in data[:10]:
    #     print str(d)

    with open(filename, 'rU') as f:
        count = 0
        for line in f:
            count += 1
            # see what we're working with
            print "line:", line
            
            d = line.split('\t')
            print d
            movies

        print count
    return movies, genres

if __name__ == '__main__':
    movies, genres = read_movies('movies.txt')
    print "movies:", [movies[d] for d in movies.keys()[:10]]
    # print "genres:", genres[:10]