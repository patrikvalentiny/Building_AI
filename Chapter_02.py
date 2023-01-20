portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    for i in range(len(ports)):
        tmp_route = route + [ports[i]]
        permutations(tmp_route, ports[:i]+ports[i+1:])
    # Print the port names in route when the recursion terminates
    if not ports:
        print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
