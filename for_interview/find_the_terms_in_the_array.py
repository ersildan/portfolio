def get_summands_indexes(nums, target):

    for ind, el in enumerate(nums):
        for ind_2, el_2 in enumerate(nums):
            if el + el_2 == target and ind != ind_2:
                return [ind,ind_2]
    return None

    