import Data.Ratio

numDigits :: Integer -> Int
numDigits = length . show

nextSqrtApprox :: Ratio Integer -> Ratio Integer
nextSqrtApprox x = 1 + 1 / (1 + x)

answer :: Int
answer = length $ filter works (take 1000 (iterate nextSqrtApprox 1))
         where works x = numDigits (numerator x) > numDigits (denominator x)
