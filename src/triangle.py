# Sample from triang dist if already in service
import scipy
import matplotlib.pyplot as plt
import yaml
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True, help='Path to the YAML config file.')
    return parser.parse_args()

def load_config(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def main():
    # parse cli arguments
    args = parse_args()
    config = load_config(args.config)

    X = []
    service_dist = config['service_dist']
    c = (service_dist['mid'] - service_dist['low']) / (service_dist['high'] - service_dist['low'])
    loc = service_dist['low']
    scale = service_dist['high'] - service_dist['low']
    x_0 = config['x0']
    for i in range(config['N']):
        generating = True
        while generating:
            x = scipy.stats.triang.rvs(c,loc,scale)
            if x >= x_0:
                time_in_accomm = x-x_0
                generating = False
        X.append(time_in_accomm)

    fig, ax = plt.subplots(1, 1)    
    ax.hist(X, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
    fig.suptitle("Remaining service time | t="+str(x_0))
    plt.savefig('triangle_dist.pdf', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()
