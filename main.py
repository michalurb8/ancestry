import argparse
import ancestry

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--points', default=300, type=int, help="How many points are to be generated")
parser.add_argument('-g', '--generations', default=400, type=int, help="How many generations are to be generated")
parser.add_argument('-s', '--sigma', default=5, type=int, help="Integer, mutation rate, can be 0")
parser.add_argument('-r', '--radius', default=2, type=int, help="How large square of pixels per point")
parser.add_argument('-c', '--color', default="111", type=lambda x: x if x=='0' or len(x)==3 else False, help="Starting color, if 0, will be randomized")

if __name__=="__main__":
    args = parser.parse_args()
    ancestry.generate(args.points, args.generations, args.sigma, args.radius, args.color)