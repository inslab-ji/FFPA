from models.DataSet import Trajectory, SeqDataSet
import pickle


def loadMsnbc(minLength=3,maxLength=None):
    msnbc_path = 'data/msnbc/msnbc990928.seq'
    with open(msnbc_path) as fp:
        lines = fp.readlines()
        line_num = len(lines)
    dataset = SeqDataSet(list(range(17)))
    for i in range(7,line_num):
        line = lines[i]
        line_split = line.split()

        for i in range(len(line_split)):
            line_split[i] = int(line_split[i]) - 1 # locations starts form 0
        
        if minLength is not None and len(line_split) < minLength:
            continue

        if maxLength is not None and len(line_split) > maxLength:
            continue

        traj = Trajectory(line_split)
        dataset.add_line(traj)
    
    return dataset


if __name__ == '__main__':
    ds = loadMsnbc()
    with open("./data/msnbc.pickle",'wb') as fp:
        pickle.dump(ds,fp)