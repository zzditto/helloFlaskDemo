# author:LWZ
# datetime:2021/2/21 15:18

"""
文件说明：

"""
import os
import uuid


class serverUtils:

    def random_filename(self, filename):
        """
        上传文件重命名
        :return: uuid名称
        """
        ext = os.path.splitext(filename)[1]  # 获取文件名后缀
        return uuid.uuid4().hex + ext
