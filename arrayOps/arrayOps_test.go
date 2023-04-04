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
	expected := []string{"a", "d", "c", "b", "e"}
	ReverseFrom(output, 1, 3)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFromFullArray(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"e", "d", "c", "b", "a"}
	ReverseFrom(output, 0, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFrom(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "e", "d", "c", "b"}
	ReverseFrom(output, 1, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndLengthFour(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"b", "a", "e", "d", "c"}
	ReverseFrom(output, 4, 2)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndLengthThree(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"d", "b", "c", "a", "e"}
	ReverseFrom(output, 3, 0)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndTwo(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"e", "b", "c", "d", "a"}
	ReverseFrom(output, 4, 0)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseCircularStartEndFive(t *testing.T) {
	output := []int{1, 2, 3, 4, 5}
	expected := []int{1, 5, 4, 3, 2}
	ReverseFrom(output, 3, 2)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}