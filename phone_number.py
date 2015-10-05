import argparse
import wave

parser = argparse.ArgumentParser()
parser.add_argument("output", help="File to save as")
parser.add_argument("number", help="Phone number to read out")
parser.add_argument("-s", "--speed", type=float, help="Change frame rate by n times")
args = parser.parse_args()


def read_phonenumber(number):
    filelist = []
    total_data = []
    for i in list(number):
        filelist.append("numbers/{}.wav".format(i))
    for infile in filelist:
        w = wave.open(infile, 'rb')
        total_data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    return total_data


def main():
    wout = wave.open(args.output, 'wb')
    data = read_phonenumber(args.number)
    wout.setparams(data[0][0])
    for numbers in data:
        wout.writeframes(numbers[1])
    wout.close()

if __name__ == '__main__':
    main()
