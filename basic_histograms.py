import numpy as np
import matplotlib.patches as mpatches
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
        if avg_ratings > curr_min and len(movie_ratings[movie]) > 20:
            for i in range(len(rat)):
                if rat[i] == curr_min:
                    ret[i] = movie
                    rat[i] = avg_ratings
                    curr_min = min(rat)
                    break
            #print rat

    # sort return movie list
    ret = [movie for (rating, movie) in sorted(zip(rat, ret))]
    ret.reverse()
    return ret

def plot_histogram(labels, ratings, title, filename=None):
    r = 5   # (Ratings range from 1 to 5)
    # Note: this_colors is only rainbow for ten colors.
    if len(labels) == 10:
        this_colors = ['r', 'orange', 'gold', 'lawngreen', 'g', 
                   'turquoise', 'b', 'purple', 'm', 'brown']
    else:
        this_colors = ['r'] * len(labels)
    n, bins, patches = plt.hist(ratings, r,
                        color=this_colors)

    plt.xticks(range(r+1), range(r+1))
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

    handle_list = []
    for i in range(len(labels)):
        handle_list += [mpatches.Patch(color=this_colors[i], label=labels[i])]

    plt.legend(handles=handle_list)

    if filename != None:
        plt.savefig(filename)
    plt.show()

def plot_histogram_stack(labels, ratings, title, filename=None):
    '''Doesn't look as nice, don't use'''
    r = 5   # (Ratings range from 1 to 5)

    plot_ratings = [0 for i in range(r)]
    for rating in ratings:
        for item in rating:
            plot_ratings[item-1] += 1
    print plot_ratings
    n, bins, patches = plt.hist(ratings, r, 
        facecolor='green', histtype='barstacked')

    plt.xticks(range(r+1), range(r+1))
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.title(title)

    plt.axis([1, r, 0, max(plot_ratings)])

    if filename != None:
        plt.savefig(filename)
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

    popular = genres['Film-Noir']

    plot_histogram_stack([movie_names[movie] for movie in popular], 
        [movie_ratings[movie] for movie in popular],
        "Film Noir movies", "pictures/basic_genres_filmnoir.png")


