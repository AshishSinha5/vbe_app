def vbe_gen(x):
    ls = []
    while x:
        q = x % (2 ** 7)
        ls.append(q)
        x = x // (2 ** 7)
    ls.reverse()
    return ls


def vbe_util(l):
    l = l.split(",")
    l = list(map(int, l))
    l.sort()
    gap_list = [0] * len(l)
    gap_list[0] = l[0]
    for i in range(1, len(l)):
        gap_list[i] = l[i] - l[i - 1]
    final_list = []
    final_bin_list = []
    for i in gap_list:
        final_list.append(vbe_gen(i))
        for j in final_list[-1]:
            final_bin_list.append('{0:08b}'.format(j))
        final_bin_list[-1] = '1' + final_bin_list[-1][1:]
    # final_bin_list = list(map(int, final_bin_list))
    final_bin_list = " ".join(str(x) for x in final_bin_list)
    # print(final_bin_list)
    return final_bin_list


if __name__ == "__main__":
    print(vbe_util('824,829,215406'))

