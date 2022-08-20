def get_dest(result_path):
    """
    result_path: Should contain the FULL path of directory & object
    """
    tmp_list = result_path.split("/")
    return "/".join(tmp_list[:len(tmp_list)-1])