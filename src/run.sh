# python -W ignore main.py  --regs [1e-3] --embed_size 256  --lr 0.0005 --save_flag 0 \
#				--batch_size 128 --epoch 100 --verbose 1 --dataset 'CiteU'

_lr=(1e-5 5e-5 1e-4 5e-4)
_batch_size=(16 32 64 128)
_Tran_head=(1 2 4 8)
_Tran_layer=(1 2 4 8)
_Tran_hid_size=(128 256 512 1024)
_max_L=(64 128)

for ((i=0; i<4; ++i))
do
  python main.py  --lr ${_lr[i]}
done