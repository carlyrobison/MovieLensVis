import numpy as np
import matplotlib.pyplot as plt

import data_io
import prob2utils



def top_ten_popular(movie_ratings):
    '''Finds the ten movies which had the most ratings.'''
    ret = [0 for i in range(10)]    # popular movies
    rat = [0 for i in range(10)]    # number of ratings
    curr_min = min(rat)

    for movie in movie_ratings:
        num_ratings = len(movie_ratings[movie])

        # if we find a more popular movie, add it in
        if num_ratings > curr_min:
            for i in range(len(rat)):
                if rat[i] == curr_min:
                    ret[i] = movie
                    rat[i] = num_ratings
                    curr_min = min(rat)
                    break

    # sort return movie list
    ret = [movie for (rating, movie) in sorted(zip(rat, ret))]
    ret.reverse()
    return ret

def top_ten_rated(movie_ratings):
    '''Finds the ten movies which had the best average ratings.'''
    ret = [0 for i in range(10)]    # best rated movies
    rat = [0.0 for i in range(10)]    # average ratings
    curr_min = min(rat)

    for movie in movie_ratings:
        avg_ratings = np.mean(movie_ratings[movie])

        # if we find a more popular movie, add it in
        if avg_ratings > curr_min:
            for i in range(len(rat)):
                if rat[i] == curr_min:
                    ret[i] = movie
                    rat[i] = avg_ratings
                    curr_min = min(rat)
                    break
            print rat

    # sort return movie list
    ret = [movie for (rating, movie) in sorted(zip(rat, ret))]
    ret.reverse()
    return ret

def plot_histogram(labels, ratings, title):
    r = 5   # (Ratings range from 1 to 5)
    colors = ['0.1', '0.9'] * 5
    n, bins, patches = plt.hist(ratings, r,
                        facecolor=colors)

    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.title(title)

    max_ratings = 0
    for rating in ratings:
        num_ratings = [0 for i in range(6)]
        for rate in rating:
            num_ratings[rate] += 1
        if max(num_ratings) > max_ratings:
            max_ratings = max(num_ratings)
    plt.axis([1, r, 0, max_ratings])
    plt.grid(True)

    plt.show()

def plot_histogram_stack(labels, ratings, title):
    r = 5   # (Ratings range from 1 to 5)

    plot_ratings = [0 for i in range(r)]
    for rating in ratings:
        for item in rating:
            plot_ratings[item-1] += 1
    print plot_ratings
    n, bins, patches = plt.hist(ratings, r, 
        facecolor='green', histtype='barstacked')

    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.title(title)

    plt.axis([1, r, 0, max(plot_ratings)])

    plt.show()

'''Makes a ccdf given data'''
def plot_ccdf(x, name):
    plt.figure()
    # the cumulative reverse hist
    plt.hist(x, 1000, normed=1, histtype='step', cumulative=-1)

    plt.xlabel(name)
    plt.ylabel('Probability')
    plt.axis([0, max(x), 0, 1])
    plt.grid(True)



if __name__ == '__main__':
    movie_names, movie_genres, genres = data_io.read_movies('movies.txt')
    Y, movie_ratings = data_io.read_ratings('data.txt', movie_names)

    popular = top_ten_popular(movie_ratings)
    print popular
    print [movie_names[movie] for movie in popular]
    print [len(movie_ratings[movie]) for movie in popular]
    print movie_ratings[popular[0]]

    '''
    print "-"*50

    popular = top_ten_rated(movie_ratings)
    print popular
    print [movie_names[movie] for movie in popular]
    print [np.mean(movie_ratings[movie]) for movie in popular]

    print movie_ratings['814']
    '''

    plot_histogram_stack([movie_names[movie] for movie in popular], 
        [movie_ratings[movie] for movie in popular],
        "Most rated movies")


