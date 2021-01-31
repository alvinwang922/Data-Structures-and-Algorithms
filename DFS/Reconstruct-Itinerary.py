"""
Given a list of airline tickets represented by pairs of 
departure and arrival airports [from, to], reconstruct the 
itinerary in order. All of the tickets belong to a man who 
departs from JFK. Thus, the itinerary must begin with JFK.
Note:
If there are multiple valid itineraries, you should return 
the itinerary that has the smallest lexical order when read 
as a single string. For example, the itinerary ["JFK", "LGA"] 
has a smaller lexical order than ["JFK", "LGB"]. All airports 
are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
"""

import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

    print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], \
        ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], \
        ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print("The arrays above should be [\"JFK\", \"MUC\", \
        \"LHR\", \"SFO\", \"SJC\"] and [\"JFK\", \"ATL\", \
        \"JFK\", \"SFO\", \"ATL\", \"SFO\"].")
