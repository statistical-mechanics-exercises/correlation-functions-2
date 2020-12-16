def variance_spin( spins ) :
  # Your code goes here
  s2, sav = 0, sum(spins) / len(spins)
  for s in spins : s2 = s2 + s*s 
  return s2 /len(spins) - sav*sav

spins1 = [1,-1,1,1,-1,1,1,1,-1,-1]
print( variance_spin( spins1 ) )
spins2 = [-1,1,1,1,-1,-1,1,1,1,-1]
print( variance_spin( spins2 ) )
