import Data.List

main = putStrLn $ show answer

digits :: Int -> [Int]
digits 0 = []
digits x = (mod x 10):(digits $ div x 10)

sortedDigits :: Int -> [Int]
sortedDigits x = sort (digits x)

sameDigits :: Int -> Bool
sameDigits x = allSame $ map sortedDigits nums
    where nums = (*) <$> [1..6] <*> [x]
          allSame xs = and $ map (== head xs) (tail xs)

answer :: Int
answer = head $ filter sameDigits [1..]
