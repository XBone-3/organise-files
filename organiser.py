import os
import shutil
import sys
import argparse
import time

# creating destinations
def destination_create(index):
	if not os.path.exists(destinations[keys[index]]):
		try:
			os.mkdir(destinations[keys[index]])
			print(f'destination {destinations[keys[index]]} created successfully')
			log.write(f'destination {destinations[keys[index]]} created successfully at {time.asctime()} \n')
		except PermissionError:
			print('permission denied to create path: ', destinations[keys[index]])
			print(f'try creating {destinations[keys[index]]} on your own and rerun the file')
			sys.exit()
	else:
		print(f'destination {destinations[keys[index]]} already exists. Trying to use existing directory...')
		log.write(f'using already existing directory {destinations[keys[index]]} at {time.asctime()} \n')

# function to move or copy the files to destinations
def function(path, formats, choice):
	if not os.path.isdir(path):
		path_split_index = path.split('.')
		file_extension_index = len(path_split_index) - 1
		file_extension_name = path_split_index[file_extension_index]
		for extension in formats:
			if extension == file_extension_name.lower():
				try:
					drctry_split_list = path.split('\\')
					file_name_index = len(drctry_split_list) - 1
					file_name = drctry_split_list[file_name_index]
					if choice.lower() == 'm':
						shutil.move(path, os.path.join(destinations[keys[i]], file_name))
						print(f'moved {file_name} successfully from {path} to {destinations[keys[i]]}')
						log.write(
							f'moved {file_name} successfully from {path} to {destinations[keys[i]]} during {time.asctime()} \n')
						break
					elif choice.lower() == 'c':
						shutil.copyfile(path, os.path.join(destinations[keys[i]], file_name))
						print(f'copied {file_name} successfully from {path} to {destinations[keys[i]]}')
						log.write(f'copied {file_name} successfully from {path} to {destinations[keys[i]]} during {time.asctime()} \n')
						break
				except OSError:
					print(f'error occurred while moving {file_name} from {path}')
					log.write(f'error occurred while moving {file_name} from {path} during {time.asctime()} \n')
					break
	elif os.path.isdir(path):
		operable_list = os.listdir(path)
		for index in range(len(operable_list)):
			item = os.path.join(path, operable_list[index])
			if not os.path.isdir(item):
				item_split_list = item.split('.')
				item_extension_index = len(item_split_list) - 1
				item_extension_name = item_split_list[item_extension_index]
				for extension in formats:
					if extension == item_extension_name:
						try:
							if choice.lower() == 'm':
								shutil.move(item, os.path.join(destinations[keys[i]], operable_list[index]))
								print(f'moved {operable_list[index]} successfully from {item} to {destinations[keys[i]]}')
								log.write(
									f'moved {operable_list[index]} successfully from {item} to {destinations[keys[i]]} during {time.asctime()}\n')
								break
							elif choice.lower() == 'c':
								shutil.copyfile(item, os.path.join(destinations[keys[i]], operable_list[index]))
								print(f'copied {operable_list[index]} successfully from {item} to {destinations[keys[i]]}')
								log.write(
									f'copied {operable_list[index]} successfully from {item} to {destinations[keys[i]]} during {time.asctime()}\n')
						except OSError:
							print(f'error occurred while moving {operable_list[index]} from {item}')
							log.write(
								f'error occurred while moving {operable_list[index]} from {item} during {time.asctime()} \n')
							break
			elif os.path.isdir(item):
				print(f'performing operation on {item} with {format_names[i]}')
				log.write(f'performing operation on{item} with {format_names[i]} at {time.asctime()} \n')
				function(item, formats, user_decision)

# the main
if __name__ == '__main__':
	print(
		'"organise" is used when your folder is like trash and you want to organise them according to the file type....')
	print('Note: organise mode will copy or move files in the same folder.')
	print('"bulk-paste" is used when there are a lot to move or copy from one folder to another...')
	while True:
		user_input = input('want to (o)rganise or (b)ulk-paste: ')
		if user_input.lower() == 'o' or user_input.lower() == 'b':
			break
		else:
			print('enter either "o" or "b"')

	# defining formats to filter the files
	image_formats = ['jpg', 'png', 'JPEG', 'PNG', 'GIF', 'gif']
	video_formats = ['mp4', 'mkv', 'avi']
	zip_formats = ['zip', '7z']
	pdf_formats = ['pdf']
	format_list = [image_formats, video_formats, zip_formats, pdf_formats]
	format_names = ['images', 'videos', 'zip', 'pdf']
	keys = ['images', 'videos', 'zip', 'pdf']
	if user_input.lower() == 'o':
		# ap = argparse.ArgumentParser()
		# ap.add_argument('-s', '--source', required=True, help='path of the folder to be organised')
		# args = vars(ap.parse_args())
		# path to begin the operation
		source = input('provide the path of the folder or drive for me to operate upon: ')
		# creating a log.txt file
		log = open(os.path.join(source, 'log.txt'), 'w')
		log.write(f'log was created in {source} during {time.asctime()} \n')
		# destinations to be created
		destinations = {'images': os.path.join(source, 'Images'), 'videos': os.path.join(source, 'Videos'),
						'zip': os.path.join(source, 'Zip'), 'pdf': os.path.join(source, 'PDFs')}
		# creating destination paths
		for i in range(len(keys)):
			destination_create(i)
		directory_list = os.listdir(source)  # creating list of items in the path
		directory_list_new = []
		# loop to filter the items
		for directory in directory_list:
			if directory == '$RECYCLE.BIN' or directory == 'games' or directory == 'educational' or directory == 'msdownld.tmp' \
					or directory == 'System Volume Information' or directory == 'Images' or directory == 'Videos' or directory == 'Zip':
				continue
			else:
				directory_list_new.append(directory)
		paths_to_operate = []
		# creating a list of paths to check for our files
		print('creating paths to operate upon')
		log.write(f'creating paths to operate upon started at {time.asctime()} \n')
		for iterable in directory_list_new:
			paths_to_operate.append(os.path.join(source, iterable))
		log.write(f'operable paths created at {time.asctime()} \n')
		log.write(f'operable paths are \n {paths_to_operate} \n')
		print('operable paths are created')
		print(paths_to_operate)
		# starting our main task of filtering
		while True:
			user_decision = input('want to (c)opy or (m)ove: ')
			if user_decision.lower() == 'c' or user_decision.lower() == 'm':
				break
			else:
				print('enter either "c" or "m"')
		log.write('c = copy, m = move')
		log.write(f'chose to {user_decision} ')
		log.write(f'starting task on {time.asctime()} \n')
		for i in range(len(format_names)):
			for route in paths_to_operate:
				print(f'operating task on {route}')
				log.write(f'operating on {route} with images on {time.asctime()} \n')
				function(route, format_list[i], user_decision)
		log.write(f'process completed on {time.asctime()} \n')
		log.close()
	elif user_input.lower() == 'b':
		# ap = argparse.ArgumentParser()
		# ap.add_argument('-s', '--source', required=True, help='source folder path')
		# ap.add_argument('-d', '--destination', required=True, help='destination folder path')
		# args = vars(ap.parse_args())
		print('provide "source" and "destination" for me to operate upon')
		source, destination = map(str, input('provide the paths with "," separation: ').split(','))
		log = open(os.path.join(destination, 'log.txt'), 'w')
		log.write('log is updating...')
		destinations = {'images': os.path.join(destination, 'Images'), 'videos': os.path.join(destination, 'Videos'),
		                'zip': os.path.join(destination, 'Zip'), 'pdf': os.path.join(destination, 'PDFs')}
		for i in range(len(keys)):
			destination_create(i)
		source_list = os.listdir(source)
		source_paths_list = []
		for iterable in source_list:
			source_paths_list.append(os.path.join(source, iterable))
		while True:
			user_inpt = input('how to operate, (c)opy or (m)ove: ')
			if user_inpt.lower() == 'c' or user_inpt.lower() == 'm':
				break
			else:
				print('provide either "c" or "m"')
		for i in range(len(format_names)):
			for path in source_paths_list:
				function(path, format_list[i], user_inpt)
		log.write('process completed....')
		log.write('log is created....')
		log.close()
