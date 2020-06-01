def powerset(array):
    main_set = []
	main_set.append([])
	# print(f"main set initially = {main_set}")
	for ele in array:
		for i in range(len(main_set)):
			current_set = main_set[i]
            # main_set.append(current_set.extend([ele])) does not work
			main_set.append(current_set + [ele])
			# main_set.append(new_set)
			# print(f'current_set = {current_set},  main_set = {main_set}')
	return main_set
