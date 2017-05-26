"""
@author: Maneesh D
@date: 5/11/2017
"""
import string


def remove_all_w(url):
    return url.lstrip("w").rstrip("w")


def remove_all_lower(url):
    return url.lstrip(string.ascii_lowercase).rstrip(string.ascii_lowercase)


def remove_all_printable(url):
    return url.strip(string.printable)

if __name__ == '__main__':
    print("www.edureka.in")
    print("-" * len("www.edureka.in"))
    print("All 'w' removed before and after .edureka. = %s" % remove_all_w("www.edureka.in"))
    print("All all lowercase letters removed before and after .edureka. = %s" %
          remove_all_lower("www.edureka.in"))
    print("All printable characters removed = %s" % remove_all_printable("www.edureka.in"))
