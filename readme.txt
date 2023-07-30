My pc specs:
Intel i7-7700 at ~60% utilization during the trials
16 gb DDR4 Ram

testing:
my birthdate is 07/05/1997 so we will use that as example input
I'll log the input, number of attempts, and time before target is reached

results:
0          took 39 tries in 0.023998260498046875 seconds
07         took 329 tries in 0.1695878505706787 seconds
070        took 4,989 tries in 2.499730110168457 seconds
0705       took 119,679 tries in 59.04464817047119 seconds
07051      took 3,873,334 in 1906.8827686309814 seconds (31 minutes, 26 seconds)
070519     untested, I speculate 16-64 million tries or ~2-8 hours
0705199    untested, I speculate 268 million - 1 billion tries or ~32-128 hours
07051997   untested, I speculate 4-16 billion tries or 20-80 days

I've found that the number of attempts roughly correspond to this series:
16^1 = 16
16^2 = 16 * 16 = 256
16^3 = 16 * 16 * 16 = 4,096
16^4 = 16 * 16 * 16 * 16 = 65,536
16^5 = 16 * 16 * 16 * 16 * 16 = 1,048,576
16^6 = 16 * 16 * 16 * 16 * 16 * 16 = 16,777,216
16^7 = 16 * 16 * 16 * 16 * 16 * 16 * 16 = 268,435,456
16^8 = 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 = 4,294,967,296
16^9 = 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 = 68,719,476,736
16^10 = 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 * 16 = 1,099,511,627,776

For each hexidecimal character of the SHA-256 output, there's approx. a
1/16 chance that you would receive any one specific output. This compounds to 
16^2 for two specific chars in succession and so on. There's no guarantee that 
the pseudorandom SHA-256 output would follow any particular pattern in generating
our vanity address, so I think it's fair to say that on average it would take a 
number of tries roughly corresponding to this series or greater for each character 
of a given target vanity address. 

If we were using ECC to generate a BTC vanity address, we'd be dealing with Base58 
which has 58 so we'd have 58 different options for each number instead of 16, so 
while we would gain many more words we could express(caps and lowercase) in Base58,
it would be significantly more computationally challenging to generate actual 
vanity BTC addresse