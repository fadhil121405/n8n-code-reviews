def append_to_list(element, target_list=None):
    """
    Menambahkan elemen ke dalam list.
    Menggunakan None sebagai default value untuk menghindari bug mutable default argument.
    """
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list