# Programming Assignment 4 - Dynamic Programming - Multiple shortest paths
                             
In this programming assignment we are asked to solve multiple shortest paths problem.

We are given 3 graph sets, and an optional 4th one that is very large:

* [first](https://d3c33hcgiwev3.cloudfront.net/_6ff856efca965e8774eb18584754fd65_g2.txt?Expires=1479686400&Signature=NhavLwnUrC37Vqla7yNDL5pXfC8RVhbRrChBEOi5QxmitRm0gJYSk14AHiqotinVR~4MphJgL35z7O5yrPhs6lPp-3m67TeoWEvL6jNWs6p5nt5ImkJVtoH8rrF9UG1AXDFPpiNZV5JEds2zqtwhCbzWG0FrjCZ2v7cdlOWNSoM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
* [second](https://d3c33hcgiwev3.cloudfront.net/_6ff856efca965e8774eb18584754fd65_g2.txt?Expires=1479686400&Signature=NhavLwnUrC37Vqla7yNDL5pXfC8RVhbRrChBEOi5QxmitRm0gJYSk14AHiqotinVR~4MphJgL35z7O5yrPhs6lPp-3m67TeoWEvL6jNWs6p5nt5ImkJVtoH8rrF9UG1AXDFPpiNZV5JEds2zqtwhCbzWG0FrjCZ2v7cdlOWNSoM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
* [third](https://d3c33hcgiwev3.cloudfront.net/_6ff856efca965e8774eb18584754fd65_g3.txt?Expires=1479686400&Signature=HQ6WubFvZ-N2hd9RjxUd2Nmdw1PDxUqfZAEtIkb81KDXc6W63CTTE8ICJSozMOO4qAC1WyXTkF5OG3XSpDlBMQ5WHwEwxX3pFLi1zAIbJunoqMDRL7O1gaNGhe9-aGeZhP7Nh7teEKunWUg86CKfRA5uYY0ZW4XH4aaGHZ6Orko_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
* [fourth-optional](https://d3c33hcgiwev3.cloudfront.net/_919f8ed0c52d8b5926aa7e3fdecc2d32_large.txt?Expires=1479686400&Signature=Zuc8YQkjHESl3S6c9voFX-gEIH0a0jyeYFaqFPupWY9pk1mpebjZTeAPWX~B8j~VMr6BcKYW74XuUGZ4xFQDAyf90WPwM7VF9PcibFL5O9JXmoaGIDthJhIj3bf1i7x8-CDHcTHsyjJoTJzXhrQliHx8UGM8LqJ9CfwZXBdZhvA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

These graphs may contain negative length cycles. We are asked to identify those that don't have any
negative cycles, and for those graphs, to compute the minimum of the shortest paths for each pair
of vertices.

##### Challenges

* Benchmark Bellman-Ford and Floyd-Warshall algorithm, and pick the fastest for the relative test sets.
(Dijkstra algorithm is not applicable, as we have negative-cost edges).

##### Solver:

* [multiple_shortest_path_finder.py](app/multiple_shortest_path_finder.py)

##### Unittests:

* [test_multiple_shortest_path_finder.py](test/multiple_shortest_path_finder.py)
