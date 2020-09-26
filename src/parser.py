import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Run JTCN.")

    parser.add_argument('--embed_type', default="Transformer",
                        help="JTCN, Ave, Dence, Transformer")
    parser.add_argument('--pretrain', default=False,
                        help='use the pretain model')

    parser.add_argument('--max_L', type=int, default=64,
                        help="atteneion layer's max len")
    parser.add_argument('--Tran_head', type=int, default=1)
    parser.add_argument('--Tran_layer', type=int, default=1)
    parser.add_argument('--Tran_hid_size', type=int, default=128)

    parser.add_argument('--split', default=0,
                        help='Move test samples to train')
    parser.add_argument('--mv_self', default=False,
                        help='when fit data,move self one-hot')

    parser.add_argument('--weights_path', nargs='?', default='',
                        help='Store model path.')
    parser.add_argument('--data_path', nargs='?', default='../data/',
                        help='Input data path.')
    parser.add_argument('--proj_path', nargs='?', default='',
                        help='Project path.')
    parser.add_argument('--dataset', nargs='?', default='CiteU',
                        help='Choose a dataset from {CiteU, Amazon}')
    parser.add_argument('--verbose', type=int, default=1,
                        help='Interval of evaluation.')
    parser.add_argument('--epoch', type=int, default=100,
                        help='Number of epoch.')
    parser.add_argument('--embed_size', type=int, default=256,
                        help='Embedding size.')
    parser.add_argument('--batch_size', type=int, default=128,
                        help='Batch size.')
    parser.add_argument('--regs', nargs='?', default='[1e-3,1e-5,1e-2]',
                        help='Regularizations.')
    parser.add_argument('--lr', type=float, default=0.0005,
                        help='Learning rate.')
    parser.add_argument('--Ks', nargs='?', default='[100, 50, 30, 20, 10]',
                        help='Output sizes of every layer')
    parser.add_argument('--save_flag', type=int, default=0,
                        help='0: Disable model saver, 1: Activate model saver')
    parser.add_argument('--test_flag', nargs='?', default='part',
                        help='Specify the test type from {part, full}, indicating whether the reference is done in mini-batch')
    return parser.parse_args()
