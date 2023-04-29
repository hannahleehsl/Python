# Name: Hannah Lee
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")

    # (Your code for Problem 1a goes here.)

    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("C", "D")
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("D", "F")
    practice_graph.add_edge("D", "E")
    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    # (Your code for Problem 1b goes here.)
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edge("Juliet", "Capulet")
    rj.add_edge("Capulet", "Tybalt")
    rj.add_edge("Juliet", "Nurse")
    rj.add_edge("Juliet", "Friar Laurence")
    rj.add_edge("Juliet", "Romeo")
    rj.add_edge("Romeo", "Friar Laurence")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Montague")
    rj.add_edge("Montague", "Benvolio")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Capulet", "Escalus")
    rj.add_edge("Capulet", "Paris")
    rj.add_edge("Escalus", "Paris")
    rj.add_edge("Escalus", "Montague")
    rj.add_edge("Escalus", "Mercutio")
    rj.add_edge("Paris", "Mercutio")

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    immediate_friends = friends(graph, user)
    mutuals_set = set()
    for immediate_friend in immediate_friends:
        friends_of_friends = friends(graph, immediate_friend)
        for mutual in friends_of_friends:
            if mutual != user and mutual not in immediate_friends:
                mutuals_set.add(mutual)
    return mutuals_set


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends that user1 and user2
        have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    friends_of_user1 = friends(graph, user1)
    friends_of_user2 = friends(graph, user2)
    mutual_friends = friends_of_user1 & friends_of_user2

    return mutual_friends


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    friends_in_common = {}
    user_friends = friends(graph, user)
    for friend in graph.nodes():
        if friend != user:
            if friend not in user_friends:
                mutuals_set = common_friends(graph, user, friend)
                mutuals_count = len(mutuals_set)
                if mutuals_count > 0:
                    friends_in_common[friend] = mutuals_count
    return friends_in_common


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    sorted_by_key = sorted(map_with_number_vals.items(), key=itemgetter(0))
    sorted_by_value = sorted(sorted_by_key, key=itemgetter(1), reverse=True)
    return_list = list()
    for key, _ in sorted_by_value:
        return_list.append(key)
    return return_list


def rec_number_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    new_list = number_map_to_sorted_list(
        number_of_common_friends_map(graph, user))
    return new_list

###
#  Problem 3
###


def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    ret_dict = {}
    friend_common = rec_number_common_friends(graph, user)
    for friend in friend_common:
        common_between_the_two = common_friends(graph, user, friend)
        total = 0
        for com_friend in common_between_the_two:
            total = total + 1 / (len(set(graph.neighbors(com_friend))))
            ret_dict[friend] = total
    return ret_dict


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence = influence_map(graph, user)
    rec_based_on_influence = number_map_to_sorted_list(influence)
    return rec_based_on_influence


###
#  Problem 5
###

def get_facebook_graph():
    """Builds and returns the facebook graph
    """
    facebook = nx.Graph()
    file_name = 'facebook-links-small.txt'
    my_file = open(file_name)
    for line in my_file:
        a, b, _ = line.strip().split('\t')
        a = int(a)
        b = int(b)
        facebook.add_edge(a, b)
    my_file.close()
    return facebook


def main():
    practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    unchanged_rec = []
    changed_rec = []
    for user in rj.nodes():
        rec_by_common_friends = rec_number_common_friends(rj, user)
        rec_by_influence = recommend_by_influence(rj, user)
        if rec_by_common_friends == rec_by_influence:
            unchanged_rec.append(user)
        else:
            changed_rec.append(user)
    sorted_unchanged = sorted(unchanged_rec)
    sorted_changed = sorted(changed_rec)
    print("Unchanged Recommendations: ", sorted_unchanged)
    print("Changed Recommendations: ", sorted_changed)

    ###
    #  Problem 5
    ###

    # (Your Problem 5 code goes here. Make sure to call get_facebook_graph.)
    facebook = get_facebook_graph()
    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090

    facebook_list = []
    for num in facebook.nodes():
        facebook_list.append(num)
    facebook_list.sort()
    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    for user in facebook_list:
        if user % 1000 == 0:
            facebook_rec_cm = rec_number_common_friends(facebook, user)
            top_ten = []
            if len(facebook_rec_cm) > 10:
                top_ten = facebook_rec_cm[0:10]
            else:
                top_ten.extend(facebook_rec_cm)
            print(str(user) + " (by num_common_friends): " + str(top_ten))

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    for user in facebook_list:
        if user % 1000 == 0:
            facebook_rec_inf = recommend_by_influence(facebook, user)
            top_ten = []
            if len(facebook_rec_cm) > 10:
                top_ten = facebook_rec_inf[0:10]
            else:
                top_ten.extend(facebook_rec_inf)
            print(str(user) + " (by influence): " + str(top_ten))

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    same_count = []
    diff_count = []
    for user in facebook.nodes():
        if user % 1000 == 0:
            facebook_rec_inf = recommend_by_influence(facebook, user)
            facebook_rec_cm = rec_number_common_friends(facebook, user)
            if facebook_rec_cm == facebook_rec_inf:
                same_count.append(user)
            else:
                diff_count.append(user)
    print("Same: ", len(same_count))
    print("Different: ", len(diff_count))


if __name__ == "__main__":
    main()
