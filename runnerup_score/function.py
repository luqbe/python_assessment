def runner_up(score):
    sc=list(set(score))
    sc.sort(reverse=True)

    if len(sc)<2:
        return "no runnerUP_score"
    else:
        return sc[1]