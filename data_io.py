# importing data from the input filed
import numpy as np

genre_labels = ['Unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

def read_movies(filename):
    '''
    Gets movies and their genres from the given file.
    '''
    movie_names = {} # movie ID to name
    movie_genres = {} # indexed by movie ID
    genres = {}

    # create the genre fields
    for g in genre_labels:
        genres[g] = set([])

    with open(filename, 'rU') as f:
        for line in f:
            # see what we're working with
            #print "line:", line
            d = line.strip('\n').split('\t')
            #print d

            # extract stuff
            num = d[0]
            title = d[1]
            genre = [genre_labels[i] for i in range(19) if d[i + 2] == '1']
            # print num, title, genre

            # add the info to the relevant db
            movie_names[num] = title
            movie_genres[num] = genre
            for g in genre:
                genres[g].add(num)

    # return it
    return movie_names, movie_genres, genres

if __name__ == '__main__':
    movie_names, movie_genres, genres  = read_movies('movies.txt')
    #print "movies:", [movies[d] for d in movies.keys()[:10]]
    # print "genres:", genres[:10]