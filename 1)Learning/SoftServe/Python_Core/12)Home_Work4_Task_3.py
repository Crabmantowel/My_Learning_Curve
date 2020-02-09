def areYouPlayingBanjo(name):
    return(str(name) + ' plays banjo' if name.startswith('R') or name.startswith('r') else str(name) + ' does not play banjo')
# Can two .startswith be replaced by one?
