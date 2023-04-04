package arrayOps

import (
	"testing"
	"reflect"
)

func TestRotateRightThree(t *testing.T) {
	input := []string{"a", "b", "c", "d"}
	expected := []string{"b", "c", "d", "a"}
	output := Rotate(input, 3, 1)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", input, expected)
	}
}

func TestRotateLeftTwo(t *testing.T) {
	input := []string{"a", "b", "c", "d", "e"}
	expected := []string{"c", "d", "e", "a", "b"}
	output := Rotate(input, 2, -1)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", input, expected)
	}
}

func TestReverseFromPosOneToPosThree(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "c", "b", "d", "e"}
	ReverseFrom(output, 1, 3)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFromZeroToFour(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"d", "c", "b", "a", "e"}
	ReverseFrom(output, 0, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFrom(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "d", "c", "b", "e"}
	ReverseFrom(output, 1, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndLengthFour(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "e", "c", "d", "b"}
	ReverseFrom(output, 4, 2)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndLengthThree(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "b", "c", "e", "d"}
	ReverseFrom(output, 3, 0)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndTwo(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "b", "c", "d", "e"}
	ReverseFrom(output, 4, 0)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndFive(t *testing.T) {
	output := []int{1, 2, 3, 4, 5}
	expected := []int{5, 4, 3, 2, 1}
	ReverseFrom(output, 3, 2)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartSecondEndFirst(t *testing.T) {
	output := []int{1, 2, 3, 4, 5}
	expected := []int{1, 5, 4, 3, 2}
	ReverseFrom(output, 1, 0)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularEvenNumList(t *testing.T) {
	output := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	expected := []int{8, 7, 3, 4, 5, 6, 2, 1, 10, 9}
	ReverseFrom(output, 6, 2)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}