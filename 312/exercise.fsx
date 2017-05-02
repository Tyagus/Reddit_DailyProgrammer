(*
    # /r/dailyprogrammer -> Challange #312
    # Description:
    # Given an integer, 
    # find the next largest integer using ONLY the digits 
    # from the given integer.
    # https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/
    Code by: TIago Ribeiro
*)

let rec distribute e = function
  | [] -> [[e]]
  | x::xs' as xs -> (e::xs)::[for xs in distribute e xs' -> x::xs]

let rec permute = function
  | [] -> [[]]
  | e::xs -> List.collect (distribute e) (permute xs)

let rec ConvertToString list =
   match list with
   | head :: tail -> head.ToString() + ConvertToString tail
   | [] -> ""

let getString list = List.fold (fun acc x -> (ConvertToString x)::acc) [] list

let rec listIntToInt list =
    match list with
    | [] -> 0
    | n :: rest -> n * (pown 10 (list.Length-1)) + listIntToInt rest

let main input = 
    let inputInt = listIntToInt input

    let allPerm = permute input

    let allPermSort = List.sort (List.fold (fun acc x -> (int x)::acc ) [] (getString allPerm))

    let solution = List.tryFind (fun x -> x > inputInt) allPermSort

    solution;

#time;;

let input = [1;2;5;6;9;7;8;9]

main input
