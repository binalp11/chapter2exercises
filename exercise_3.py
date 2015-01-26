from __future__ import division

#this is exercise 3 <- Restriction fragment lengths

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

strand1 = sequence.find("GAATTC") + 1

strand2 = len(sequence) - strand1
