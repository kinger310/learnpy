from mxnet import nd
from mxnet.gluon import nn

# 实现“注意力机制”一节中定义的函数a
def attention_model(attention_size):
  model = nn.Sequential()
  model.add(
    nn.Dense(attention_size, activation='tanh', use_bias=False, flatten=False),
    nn.Dense(1, use_bias=False, flatten=False)
  )
  return model


# 注意力机制的输入包括查询项、键项和值项

def attention_forward(model, enc_states, dec_state):
  # 将解码器隐藏状态广播到和编码器隐藏状态形状相同后进行连结
  dec_states = nd.broadcast_axis(
      dec_state.expand_dims(0), axis=0, size=enc_states.shape[0]
  )
  enc_and_dec_states = nd.concat(enc_states, dec_states, dim=2)
  e = model(enc_and_dec_states)  # 形状为（时间步数，批量大小，1）
  alpha = nd.softmax(e, axis=0)  # 在时间步维度做softmax运算
  return (alpha * enc_states).sum(axis=0)


seq_len, batch_size, num_hiddens = 10, 4, 8
model = attention_model(seq_len)
model.initialize()
enc_states = nd.zeros((seq_len, batch_size, num_hiddens))
dec_state = nd.zeros((batch_size, num_hiddens))
print(attention_forward(model, enc_states, dec_state).shape)


from mxnet.gluon import data as gdata
# gdata.vision.ImageFolderDataset
X = gdata.vision.CIFAR10(train=True)