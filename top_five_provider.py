import networkx
import csv


def get_five_provider(relation_file, hostname_file):
    g = networkx.Graph()
    with open(relation_file, 'r') as relations, open(hostname_file, 'r') as hostname_asn:
        providers = csv.reader(relations, delimiter='\n')
        hostnames = csv.reader(hostname_asn)

        for asn in providers:
            g.add_edge(asn[0].split(',')[0], asn[0].split(',')[1])

        asn_degree_dict = {n: d for n, d in g.degree()}

        for host in hostnames:
            if host[2] in asn_degree_dict:
                asn_degree_dict[host[2]] += 1

        sorted_asn = sorted(asn_degree_dict, key=asn_degree_dict.__getitem__, reverse=True)

        return sorted_asn[:5]


if __name__ == '__main__':
    relations = 'relations.csv'
    hostnames = 'top-10k-with-asn.csv'
    top_five = get_five_provider(relations, hostnames)
    print('Top five providers:')
    print(top_five)
