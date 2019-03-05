#coding=utf-8
import re
import sys

class Item:
    def __init__(self):
        self.iter = 0
        self.train_loss = 0

log_file = r"demo.log"

F_r = open(log_file,'rt')

## save iteration, loss
F_w = open('write_ouput.txt','wt')

## set condition
regex_iteration = re.compile('Iteration (\d+)')
regex_train_output = re.compile('Train net output #(\d+): (\S+) = ([\.\deE+-]+)')
regex_train_output_cls = re.compile('Train net output #1: loss-net1 = ([\.\deE+-]+)')
regex_train_output_box = re.compile('Train net output #0: loss-net2 = ([\.\deE+-]+)')
regex_train_output_alignment = re.compile('Train net output #2: loss-net3 = ([\.\deE+-]+)')

regex_test_output = re.compile('Test net output #(\d+): (\S+) = ([\.\deE+-]+)')
regex_learning_rate = re.compile('lr = ([-+]?[0-9]*\.?[0-9]+([eE]?[-+]?[0-9]+)?)')

iteration = -1

## save result
SaveIter =[]
SaveTrainLoss = []
SaveBoxLoss = []
SaveAlignmentLoss = []

while 1:
    line = F_r.readline()
    if not line:
        break
    # ret = line.find(beginStr)
    infoTemp = Item()
    iteration_match = regex_iteration.search(line)
    if iteration_match: ##否则便是None
        iteration = int(iteration_match.group(1))
        # iteration = iteration -1000
        if len(SaveIter)==0:
            SaveIter.append(iteration)
        if SaveIter[-1]!= iteration:
            SaveIter.append(iteration)
    if iteration == -1:
        continue
    # cls loss
    train_loss_match = regex_train_output_cls.search(line)
    if train_loss_match:
        SaveTrainLoss.append(float(train_loss_match.group(1)))
    # box loss
    box_match = regex_train_output_box.search(line)
    if box_match:
        SaveBoxLoss.append(float(box_match.group(1)))
    # alignment loss
    alignment_match = regex_train_output_alignment.search(line)
    if alignment_match:
        SaveAlignmentLoss.append(float(alignment_match.group(1)))

saveNum = min(len(SaveIter),len(SaveTrainLoss),len(SaveBoxLoss)) ## len(SaveAlignmentLoss)
for i in range(0,saveNum):
    F_w.write(str(SaveIter[i])+' '+str(SaveTrainLoss[i])+' '+str(SaveBoxLoss[i])+' '+str(SaveAlignmentLoss[i])+'\n')
    # F_w.write(str(SaveIter[i])+' '+str(SaveTrainLoss[i])+' '+str(SaveBoxLoss[i])+' '+'\n')
print 'write over!'