# Programming Assignment 3 - Dynamic Programming - Knapsack
                             
In this programming assignment we are asked to solve the famous knapsack problem.

We are given two knapsack instances, [a small](https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt?Expires=1479600000&Signature=gvpA1fmhxMiNc4xPS-IeuE8nVf2diqHzt7VdWgSs2YEhhTVfWdEEAiJoLy2N-nUsct4YYzAcIxmLBFTVHnwTBT9V8AplVqO1WdSBiXdm3UooEOm~ry1Femw~mB4aEtsvPJbX0dLSM-npObSAULbaao~DFIkvwnV-JDp4gkZPhm0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
and [a larger](https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt?Expires=1479600000&Signature=anj4BHDa62BmTYXBenI3puaW~LzizYjFrumSwC3PNKJyDbzlO0fMH-9mjwUWNIr8JU~2hpMBoyg2tylFvdd2bpwW-nWj5NYLdMuCq0LE201EPn4K6HnKSaHST62j3ckPznUbo8Ph9GQNie8HOIqawd1CVxAv-~jNyc4hyYZKhBY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

##### Challenges

* Employ some optimization to solve the large knapsack instance.

The classical approach (bottom-up, 2D array) won't work on the large instance as we are computing redundant
subproblems. We don't need to compute every single combination of item - weight. That's why the recursive 
solution was employed, along with memoization (to avoid computing the same problems again and again)

##### Solver:

* [knapsack.py](app/knapsack.py)

##### Unittests:

* [test_knapsack.py](test/test_knapsack.py)
