"""
 define pyric exceptions
  all exceptions are tuples t=(error code,error message)
  we use error codes defined in errno, using EUNDEF = -1 to define an undefined
  error I don't like importing all from errno but it provides conformity in
  error handling i.e modules using pyric.error do not need to call pyric.EUNDEF
  and errno.EINVAL but can call pyric.EUNDEF and pyric.EINVAL
"""
EUNDEF = -1  # undefined error
from errno import *  # make all errno errors pyric errors

errorcode[EUNDEF] = "EUNDEF"  # add ours to errorcode dicts


class error(EnvironmentError):
    def __init__(self, errno, errmsg=None):
        if not errmsg:
            errmsg = strerror(errno)
        EnvironmentError.__init__(self, errno, errmsg)


def strerror(errno):
    """
    :param errno: error code
    :returns: error message
    """
    import os

    if errno < 0:
        return "Undefined error"
    elif errno == EPERM:
        return "Superuser privileges required"
    elif errno == EINVAL:
        return "Invalid parameter"
    elif errno == EBUSY:
        msg = "{0}. Make sure Card is up and no other devices share the same phy"
        return msg.format(os.strerror(EBUSY))
    elif errno == ENFILE:
        return "There are no available netlink sockets"
    else:
        return os.strerror(errno)
