import os

from shutil import copyfile


if __name__ == '__main__':
	few = 500
	data_dir = 'mnist_png'
	training_dir = os.path.join(data_dir, 'training') # mnist_png/training
	few_training_dir = os.path.join(data_dir, f'training-{few}') # mnist_png/training-500

	if not os.path.exists(few_training_dir):
		os.mkdir(few_training_dir)

	for i in range(10):
		print(f'Working on digit {i}')

		if not os.path.exists(os.path.join(few_training_dir, str(i))): # mnist_png/training-500/2
			os.mkdir(os.path.join(few_training_dir, str(i)))

		filenames = os.listdir(os.path.join(training_dir, str(i)))
		filenames = sorted(filenames)
		few_filenames = filenames[:few]
		for filename in few_filenames:
			copyfile(
				os.path.join(training_dir, str(i), filename),
				os.path.join(few_training_dir, str(i), filename),
			)
