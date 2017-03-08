import os
import numpy as np
import shutil
import argparse

parser = argparse.ArgumentParser(description='Simple random split on training data.')
parser.add_argument('--train_dir', type=str)
parser.add_argument('--work_dir', type=str)

np.random.seed(2016)

train_split_dir = os.path.join(work_dir, "train")
if not os.path.exists(train_split_dir):
    os.makedirs(train_split_dir)
val_split_dir = os.path.join(work_dir, "test")
if not os.path.exists(val_split_dir):
    os.makedirs(val_split_dir)

FishNames = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']

nbr_train_samples = 0
nbr_val_samples = 0

# Training proportion
split_proportion = 0.8

for fish in FishNames:
    if fish not in os.listdir(train_split_dir):
        os.mkdir(os.path.join(train_split_dir, fish))

    total_images = os.listdir(os.path.join(train_dir, fish))

    nbr_train = int(len(total_images) * split_proportion)

    np.random.shuffle(total_images)

    train_images = total_images[:nbr_train]

    val_images = total_images[nbr_train:]

    for img in train_images:
        source = os.path.join(train_dir, fish, img)
        target = os.path.join(train_split_dir, fish, img)
        shutil.copy(source, target)
        nbr_train_samples += 1

    if fish not in os.listdir(val_split_dir):
        os.mkdir(os.path.join(val_split_dir, fish))

    for img in val_images:
        source = os.path.join(train_dir, fish, img)
        target = os.path.join(val_split_dir, fish, img)
        shutil.copy(source, target)
        nbr_val_samples += 1

print('Finish splitting train and val images!')
print('# training samples: {}, # val samples: {}'.format(nbr_train_samples, nbr_val_samples))
