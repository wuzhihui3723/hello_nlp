import torch
import torch.nn as nn
import jieba
import numpy as np


"""
基于pytorch的网络编写一个分词模型
使用jieba分词的结果作为训练数据
看看是否可以得到一个效果接近的神经网络模型
"""

class TorchModel(nn.Module):
    def __init__(self,input_dim,hidden_size,num_rnn_layer,vocab):
        super(TorchModel,self).__init__()
        self.embedding = nn.Embedding(len(vocab) + 1,input_dim)
        self.rnn_layer = nn.RNN(input_size=input_dim,
                                hidden_size=hidden_size,
                                batch_first=True,
                                num_layers=num_rnn_layer,
                                nonlinearity="relu",
                                dropout=0.1)
        self.classify = nn.Linear(hidden_size,2)
        self.loss_func = nn.CrossEntropyLoss(ignore_index=-100)

    # 当输入真实标签，返回loss值；无真实标签，返回预测值
    def forward(self,x,y = None):
        x = self.embedding(x)
        x,_ = self.rnn_layer(x)
        y_pred = self.classify(x)
        if y is not None:
            return self.loss_func(y_pred.view(-1,2),y.view(-1))
        else:
            return y_pred


def build_vocab(vocab_path):
    vocab = {}
    with open(vocab_path,"r",encoding="utf8") as f:
        for index,line in enumerate(f):
            char = line.strip()
            vocab[char] = index + 1
    vocab["unk"] = len(vocab) + 1
    return vocab


def sentence2sentence(sentence, vocab):
    sentence = [vocab.get(char,vocab['unk']) for char in sentence]
    return sentence


def sentence2label(sentence):
    words = jieba.lcut(sentence)
    label = [0] * len(sentence)
    pointer = 0
    for word in words:
        pointer += len(word)
        label[pointer - 1] = 1
    return label


class Dataset(object):
    def __init__(self,corpus_path,vocab,max_length):
        self.vocab = vocab
        self.corpus_path = corpus_path
        self.maxlength = max_length
        self.load()

    def load(self):
        self.data = []
        with open(self.corpus_path,encoding="utf8") as f:
            for line in f:
                sequence = sentence2sentence(line,self.vocab)
                label = sentence2label(line)

def build_dataset(corpus_path, vocab, max_length, batch_size):
    dataset = Dataset(corpus_path,vocab,max_length)



def main():
    epoch_num = 10 #训练轮数
    batch_size = 20
    char_dim = 50
    hidden_size = 100
    num_rnn_layer = 3
    max_length = 20
    learning_rate = 1e-3
    vocab_path = "data/chars.txt"
    corpus_path = "data/corpus.txt"
    vocab = build_vocab(vocab_path)
    data_loader = build_dataset(corpus_path, vocab, max_length, batch_size)

    return

if __name__ == '__main__':
    main()