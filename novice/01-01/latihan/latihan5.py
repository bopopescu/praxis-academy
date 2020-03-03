list(range(3, 6)) 
def concat(*args, sep="/"):
    return sep.join(args)
concat("earth", "mars", "venus", sep=".")