# Programming Assignment 2 - Clustering, Kruskal's MST
                             
In this programming assignment we are asked to compute the max-spacing k-clustering
of two given cluster [this small one](https://d3c33hcgiwev3.cloudfront.net/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt?Expires=1479600000&Signature=DSaztEEpucrEEz4j6r5~tBwv5WOmcEsuByLG-FiugoElcuqgBM8kfl5YdkgjMrWDJSk3v~eYV7JpKev1t4yMuXgWuozv6A0QwePfmnLDH3uDfAUAbFVIXLciOeYhvYX~UsipjvH8rPL~bx1FxpupFlnHKDrbiSnXsYtkmglePI4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
and [this larger](https://d3c33hcgiwev3.cloudfront.net/_fe8d0202cd20a808db6a4d5d06be62f4_clustering_big.txt?Expires=1479600000&Signature=cJz7loN1Q3TpWk-YOQDkW7sAJQul2YiFbF6kbQarjwMaP-Iy-bPxFOxfZRNcWY1LBPggZrspZNfpzHS-IU5lV02LGm9SmcPM79JLg-mswfEd8yEN~2J1tQijm62IZtZ5KOGgdth2f0Oe3FbInF5UR84emsBOdLv8ivD4mYr8hUE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

The clustering algorithm that was described in the lecture, uses the Kruskal's
MST algorithm (sort the edges from min to max, add if no cycle - detect cycles with
the union-find data structure).



##### Challenges

* Model the large cluster efficiently, as we can't store each distance explicitly.

##### Solver:

* [cluster_small.py](app/cluster_small.py)
* [cluster_big.py](app/cluster_big.py)

##### Unittests:

* [test_cluster_small.py](test/test_cluster_small.py)
* [test_cluster_big.py](test/test_cluster_big.py)
