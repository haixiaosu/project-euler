import numpy

# (i,j) entry represents probability of finishing on i when starting at j.
P = numpy.zeros((40,40))

# Special squares.
GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5
R2 = 15
R3 = 25
U1 = 12
U2 = 28
T1 = 4
D3 = 19
GO_TO_JAIL = 30
CC3 = 33
CC = [2, 17, 33]
CH1 = 7
CH2 = 22
CH3 = 36

# Dice
n = 4

# We break the solution into two independent Markov chains:
# One for moving between squares and one for keeping track of doubles.
# Note that this isn't quite accurate because the doubles counter resets
# if one is sent to jail.

# Calculate probability of having rolled two doubles in a row.
dice_prob_mat = numpy.array([[(n-1)/n, (n-1)/n, 1], [1/n, 0, 0], [0, 1/n, 0]])
w, v = numpy.linalg.eig(dice_prob_mat)
doubles_prob = v[:,0]/numpy.sum(v[:,0])
doubles_prob = numpy.real(doubles_prob).astype(float)

# Dice roll probabilities.
prob_roll = numpy.array([1,2,3,4,5,6,5,4,3,2,1], dtype=float)
prob_roll = numpy.array([1,2,3,4,3,2,1], dtype=float)
prob_roll[::2] -= doubles_prob[2]
prob_roll /= n**2

for i in range(40):
    vec = numpy.zeros(40)
    if i+2+len(prob_roll) <= 40:
        vec[i+2:i+2+len(prob_roll)] = prob_roll
    elif i+2 <= 40:
        leftover = (i+2+len(prob_roll)) % 40
        vec[i+2:] = prob_roll[:-leftover]
        vec[:leftover] = prob_roll[-leftover:]
    else:
        # We're on H2.
        vec[1:len(prob_roll)+1] = prob_roll
    
    end_vec = vec.copy()
    end_vec[JAIL] += 1 - numpy.sum(prob_roll)
    for k in range(i+2, i+2+len(prob_roll)):
        j = k % 40
        if j == GO_TO_JAIL:
            end_vec[JAIL] += vec[j]
            end_vec[j] = 0
        elif j in CC:
            end_vec[JAIL] += vec[j]*1/16
            end_vec[GO] += vec[j]*1/16
            end_vec[j] *= 14/16
        elif j in [CH1, CH2, CH3]:
            transfer_sq = [GO, JAIL, C1, E3, H2, R1]
            if j == CH1:
                transfer_sq += [R2, R2, U1, T1]
            elif j == CH2:
                transfer_sq += [R3, R3, U2, D3]
            elif j == CH3:
                transfer_sq += [R1, R1, U1]
            for sq in transfer_sq:
                end_vec[sq] += vec[j]*1/16   
            if j == CH3:
                # Deal with possibility of second CC.
                end_vec[GO] += vec[j]*1/16*1/16
                end_vec[JAIL] += vec[j]*1/16*1/16
                end_vec[CC3] += vec[j]*1/16*14/16
            end_vec[j] *= 6/16
    P[:,i] = end_vec
eigvals, eigvecs = numpy.linalg.eig(P)
probs = eigvecs[:,0]/numpy.sum(eigvecs[:,0])

top_n = 3
top_inds = probs.argsort()[-top_n:][::-1]
for i in range(top_n):
    print(top_inds[i], probs[top_inds[i]])