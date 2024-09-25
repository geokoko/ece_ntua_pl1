datatype 'a tree = node of 'a * 'a tree * 'a tree | empty

(* Helper function to calculate the size of the subtree *)
fun size empty = 0
  | size (node (_, left, right)) = 1 + size left + size right

(* Main function to count unbalanced nodes *)
fun countUnbalanced empty = 0
  | countUnbalanced (node (_, left, right)) =
    let
      val leftSize = size left
      val rightSize = size right
      val currentUnbalanced = if leftSize = rightSize then 0 else 1
    in
      currentUnbalanced + countUnbalanced left + countUnbalanced right
    end
