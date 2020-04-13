---
title: "Data Structure"
excerpt: "mind the data structure"
date: 2018-03-20
toc: true
category:
- 'Algorithms'
tag:
- 'Data Structure'
- 'Basics'
weight: 10
---

Dealing with data structure is like dealing with your cloth. Some people simply randomly drop their cloth somewhere without thinking. But it takes time to retrieve a specific T-shirt. Some poeple spend some time folding and arranging their cloth. However this process makes it easy to find a specific T-shirt. There is always a balance between the computation time and the coding time.

## Keywords

This is meant for some kind of flash card keywords. I am using this to remind myself some of the important concepts.

### Binary Tree

0. Tree; Binary tree
1. Traverse a tree:
   a. Pre-order traversal: parent->left->right
   b. In-orer traversal: left->parent->right
   c. Post-order traversal: left->right->parent
   d. Level-order traversal: top->bottom, by each level from left to right of the whole tree

## Some Useful Data Structures

### Array

Array is accessed with indices.

### Linked List

The first element is **head** while the last element is **tail**.


Elements can be linked through two different ways, Signly Linked List or Doubly Linked List.

Each node of the singly linked list is assigned two fields, the first field is the value of the node, which stores the information we need, the second field is the link to the next node.

<figure markdown="1">
![](../assets/data-structure/Singly-linked-list.svg)
<figcaption markdown="1">
Singly linked list illustration from [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
</figcaption>
</figure>

Suppose we are solving the [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem). Linked list is good for deletion, however it is computation expensive when it comes to the counting. On the other hand, array structure is good for determining which one to delete, but the deletion involves rearrangement of index the array which requires some computation power.

### Stack

Stack is good for adding new items and removing the most recent-added item. ([Card on Enki](https://enkipro.com//insight/58f77be3d2d15f373906a905))

Stack data structure is Last in First out, aka LIFO. There are only two ways to change the stack, which are adding item to the stack and removing the item at the top.

<figure markdown="1">
![](../assets/data-structure/Lifo_stack.png)
<figcaption markdown="1">
Stack from Wikipedia
</figcaption>
</figure>

### Queue

Queue is First in First out, aka FIFO. The name Queue explains itself quite well. In a line of queue, the first one in the line would be the first one served and removed from the queue. To add into the queue, we have the put the new guy at the end of the queue.

<figure markdown="1">
![](../assets/data-structure/Data_Queue.svg)
<figcaption markdown="1">
Queue from Wikipedia
</figcaption>
</figure>

