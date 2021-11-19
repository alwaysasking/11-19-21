def repeats(string):

  # can't be repeating if 1 character or less, so:
  if len(string) <= 1:
    return False
    
  # if is more than 1 character, split the string in two:
  else:
    x = int(len(s) / 2)
    
    # go to the character in the pos after the split
    split = string[:x+1]
    
    reps = ""
    
    # check the repetition:  
    for s in split:
      reps+=1
      if string.replace(reps, "") == "":
        return True
      else:
        return False
