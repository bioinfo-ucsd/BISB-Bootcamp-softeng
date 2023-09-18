def gc_content(string):
    string = string.upper()
    gs=string.count("G")
    cs=string.count("C")
    tot=len(string)
    return (gs+cs)/tot
