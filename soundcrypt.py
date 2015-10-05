import wave
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input", help="Path to the file")
parser.add_argument("output", help="File to save as")
parser.add_argument("-r", "--reverse", action="store_true", help="Reverse the output")
parser.add_argument("-s", "--speed", type=float, help="Change frame rate by n times")
args = parser.parse_args()


def get_frames(wf):
    full_data = []
    for i in range(wf.getnframes()):
        full_data.append(wf.readframes(1))
    return full_data


def reverse(data):
    return data[::-1]


def save(wf, data):
    wf.writeframes(''.join(data))


def main():
    win = wave.open(args.input, 'rb')
    wout = wave.open(args.output, 'wb')
    wout.setparams(win.getparams())

    data = get_frames(win)
    if(args.reverse is True):
        data = reverse(data)
    if(args.speed is not None):
        wout.setframerate(wout.getframerate() * args.speed)
    save(wout, data)
    wout.close()
    win.close()


if __name__ == '__main__':
    main()
