import Data.List
import Data.Maybe (fromJust)
import Data.Ord
import Data.Ratio
import qualified Data.Set as Set

data Op = Add | Sub | Mul | Div
data Tree a = Leaf a | Node Op (Tree a) (Tree a)

getAllTrees :: Fractional a => [a] -> [Tree a]
getAllTrees [x] = [Leaf x]
getAllTrees xs = do
                    splitInd <- [1..((length xs) - 1)]
                    let left = take splitInd xs
                        right = drop splitInd xs
                    leftTree <- getAllTrees left
                    rightTree <- getAllTrees right
                    op <- [Add, Sub, Mul, Div]
                    return (Node op leftTree rightTree)

evalTree :: (Fractional a, Eq a) => Tree a -> Maybe a
evalTree (Leaf x) = Just x
evalTree (Node Add x y) = (+) <$> (evalTree x) <*> (evalTree y)
evalTree (Node Sub x y) = (-) <$> (evalTree x) <*> (evalTree y)
evalTree (Node Mul x y) = (*) <$> (evalTree x) <*> (evalTree y)
evalTree (Node Div x y) = case denom of
                              Just 0 -> Nothing
                              Nothing -> Nothing
                              _ -> (/) <$> num <*> denom
                          where denom = evalTree y
                                num = evalTree x

evalAllTrees :: (Fractional a, Eq a) => [a] -> [a]
evalAllTrees xs = map fromJust filtered
        where maybeList = map evalTree (getAllTrees xs)
              filtered = filter dropMaybe maybeList
              dropMaybe Nothing = False
              dropMaybe _ = True


maxInSet :: Set.Set Int -> Int
maxInSet xs = works 1
              where works n
                      | isElem = works (n + 1)
                      | otherwise = n - 1
                      where isElem = n `elem` xs

countDistinctValues :: [Ratio Int] -> Int
countDistinctValues xs = maxInSet (Set.fromList filtered)
        where allTrees = concatMap evalAllTrees (permutations xs)
              filtered = map numerator (filter validResult allTrees)
              validResult x = (x > 0) && ((denominator x) == 1)


combinations :: Int -> [a] -> [[a]]
combinations 0 _ = [[]]
combinations n xs = [ (xs!!i):xr | i <- [0..(length xs) - 1],
                                   xr <- combinations (n - 1) (drop (i + 1) xs)]


answer = maximumBy (comparing snd) (zip combs res)
         where res = map countDistinctValues combs
               combs = combinations 4 [0 % 1..9]

main = print answer
