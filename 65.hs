import Data.Char (digitToInt)
import Data.Ratio

eRepr :: Int -> Ratio Integer
eRepr n = foldr (\x y-> x + 1 / y) (last repr) (init repr)
          where repr = 2:take n (concatMap (\x -> [1, 2 * x, 1]) [1 % 1..])

answer = sum $ map digitToInt (show $ numerator $ eRepr 99)
