package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil || q == nil {
		return p == q
	}

	if p.Val != q.Val {
		return false
	}

	if (p.Left == nil) != (q.Left == nil) {
		return false
	}

	if p.Left != nil {
		if !(isSameTree(p.Left, q.Left)) {
			return false
		}
	}

	if (p.Right == nil) != (q.Right == nil) {
		return false
	}

	if p.Right != nil {
		if !(isSameTree(p.Right, q.Right)) {
			return false
		}
	}

	return true
}

func main() {
	// [1,2,3]
	// [1,2,3]
	testCaseA := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
		Right: &TreeNode{
			Val: 3,
		},
	}
	testCaseB := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
		Right: &TreeNode{
			Val: 3,
		},
	}

	fmt.Println(isSameTree(&testCaseA, &testCaseB))
}
