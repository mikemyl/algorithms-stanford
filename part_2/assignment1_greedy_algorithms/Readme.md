# Programming Assignment 1 - Greedy algorithms
                             

This programming assignment consist of two tasks. In the first task, we are given [this](app/assignment_1.1.txt) 
list of tasks, where each task has a weight (the first number) and a time (the second number). Our goal is to
schedule these tasks so that the sum of the completion times of the tasks (weight * time_that_was_completed) is 
minimized. We are going to evaluate two greedy algorithms: the first one takes the difference (weight - time),
as the greedy choice, while the second one tasks the ratio (weight / time)


##### Challenges
* Special care needs to be taken in order to handle ties (we need to choose the job with the bigger weight first)


##### Solver:

* [job_scheduler.py](app/job_scheduler.py)

##### Unittests:

* [test_job_scheduler.py](test/test_job_scheduler.py)