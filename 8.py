"""This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all
 nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1 """

class Node {
	int value
	Node left
	Node right
}

def is_unival(root) :
	if root == null:
		return True
	if root.left != null and root.left.value != root.value :
		return False
	if root.right != null and root.right.value != root.value :
		return False
	if is_unival(root.left) and is_unival(root.right) :
		return True
	return False

#count func

def count_univals(root) :
	return 0

	total_count = count_univals(root.left) + count_univals(root.right)
	if is_unival(root):
		total_count += 1
	return total_count