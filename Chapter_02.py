routes = []
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    for i in range(len(ports)):
        tmp_route = route + [ports[i]]
        permutations(tmp_route, ports[:i] + ports[i + 1:])
    # Print the port names in route when the recursion terminates
    if not ports:
        routes.append(route)


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))


def main():
    # https://sea-distances.org/
    # nautical miles converted to km

    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)

    co2 = 0.020

    for i in routes:
        distance = 0
        for j in range(1, len(i)):
            distance += D[i[j - 1]][i[j]]
        emissions = distance * co2
        print(' '.join([portnames[r] for r in i]) + " %.1f kg" % emissions)


main()
