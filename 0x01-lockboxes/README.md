### Lockboxes
### Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

#### Concepts Needed

- **Lists and List Manipulation:** Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically. ([Python Lists - Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists))
- **Graph Theory Basics:** Knowledge of graph theory, especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search. ([Graph Theory - Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms))
- **Algorithmic Complexity:** Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms. ([Big O Notation - GeeksforGeeks](https://www.geeksforgeeks.org/big-o-notation/))
- **Recursion:** Some solutions might require a recursive approach to traverse through the boxes and keys. ([Recursion in Python - Real Python](https://realpython.com/python-recursion/))
- **Queue and Stack:** Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes. ([Python Queue and Stack - GeeksforGeeks](https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/))
- **Set Operations:** Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process. ([Python Sets - Python Official Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets))

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

### Additional Resources

- **Mock Technical Interview**

## Requirements

- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should be documented
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

- **Tasks**
  - **Lockboxes**
    - **Score:** 0.0% (Checks completed: 0.0%)
    - **Prototype:** `def canUnlockAll(boxes)`
    - **Return:** `True` if all boxes can be opened, else return `False`

## Example

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
