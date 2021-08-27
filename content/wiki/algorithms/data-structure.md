---
title: "Data Structure"
description: "mind the data structure"
date: 2018-03-20
categories:
- 'Algorithms'
tags:
- 'Data Structure'
- 'Basics'
weight: 2
---

Dealing with data structure is like dealing with your clothes. Some people randomly drop their clothes somewhere without thinking. But it takes time to retrieve a specific T-shirt. Some people spend more time folding and arranging their clothes. This process makes it easy to find a specific T-shirt. Similar to retrieving clothes, there is always a balance between the computation time (retrieving clothes) and the coding time (folding clothes).

## Keywords

This section serves as some kind of flashcard keywords. I am using this section to remind myself of the important concepts.

### Binary Tree

1. Tree; Binary tree
2. Traverse a tree:
   1. Pre-order traversal: parent->left->right
   2. In-orer traversal: left->parent->right
   3. Post-order traversal: left->right->parent
   4. Level-order traversal: top->bottom, by each level from left to right of the whole tree


## Some Useful Data Structures

### Array

Suppose I bought 5 movie tickets for the movie [Tenet](https://www.imdb.com/title/tt6723592/). Usually, the theater would give out contiguous seats, 0, 1, 2, 3, 4. Your friends are seated as shown in the following table.

| seat | 0 | 1 | 2 | 3 | 4 |
|:----:|:----:|:----:|:----:|:----:|:----:|
| people | A | B | C | D | E |

{{< figure src="../assets/data-structure/theater-seats-contiguous.svg" caption="Your friends are seated in the red seats." >}}

Now it is easy to locate a friend. When you find your friend A, just find the third seat next to A to find your friend D.

The seats are like spots in computer memory. Your friends are the values assigned to the spots.

```
array = [A, B, C, D, E]
```

becomes an array. This array is accessed with indices, i.e., `array[3]` is your friend D.


### Linked List

What if the theater doesn't have contiguous seats? You can create a linked list. Friend A only know the spot of friend B, friend B only knows the location of friend C, etc. If you would like to find the seat of friend D, consult A first to find the seat of friend B. Find the seat of friend B then find the seat of friend C. Finally, find friend C to get the seat of friend D.

{{< figure src="../assets/data-structure/theater-seats-non-contiguous.svg" caption="Your friends are seated in the red seats." >}}


In a linked list, the first element is **head** and the last element is **tail**.

Elements can be linked in two different ways, Signly Linked List or Doubly Linked List.

Each node of the singly linked list is assigned two fields, the first field is the value of the node, which stores the information we need, the second field is the link to the next node.

{{< figure src="../assets/data-structure/Singly-linked-list.svg" caption="Singly linked list illustration from [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)" >}}

Suppose we are solving the [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem). Linked list is good for deletion, however it is computation expensive when it comes to the counting. On the other hand, array structure is good for determining which one to delete, but the deletion involves rearrangement of index the array which requires some computation power.

### Stack

Stack is good for adding new items and removing the most recent-added item. ([Card on Enki](https://enkipro.com//insight/58f77be3d2d15f373906a905))

Stack data structure is Last in First out, aka LIFO. There are only two ways to change the stack, which are adding an item to the stack and removing the item at the top.


{{< figure src="../assets/data-structure/Lifo_stack.png" caption="Stack from Wikipedia" >}}

### Queue

Queue is First in First out, aka FIFO. The name Queue explains itself quite well. In a line of queue, the first one in the line would be the first one served and removed from the queue. To add into the queue, we have to put the new guy at the end of the queue.


{{< figure src="../assets/data-structure/Data_Queue.svg" caption="Queue from Wikipedia" >}}
