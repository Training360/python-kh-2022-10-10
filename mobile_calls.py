calls = [
("1111","2222","10:10","start"),
("1112","2223","10:15","start"),
("1113","2224","10:20","start"),
("1111","2222","10:25","end"),
("1113","2224","10:30","end"),
("1112","2223","10:35","end")]

active_calls = {}
closed_calls = []
for call in calls:
    caller, called, time, type = call
    if type == "start":
        active_calls[caller] = {"caller": caller, "called": called, "start": time}
    else:
        active_calls[caller]["end"] = time
        closed_calls.append(active_calls[caller])
        del(active_calls[caller])


print(closed_calls)