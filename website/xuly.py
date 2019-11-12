# -*- coding: utf-8 -*-
import re


def taoslug(ketqua):
    mautimkiem = {
            '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
            '[đ]': 'd',
            '[èéẻẽẹêềếểễệ]': 'e',
            '[ìíỉĩị]': 'i',
            '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
            '[ùúủũụưừứửữự]': 'u',
            '[ỳýỷỹỵ]': 'y',
            ' ': '-',
            }
    ketqua = re.sub('^\s+', '', ketqua)
    ketqua = re.sub('\s+$', '', ketqua)
    for mau, thaythe in mautimkiem.items():
        ketqua = re.sub(mau, thaythe, ketqua)
        ketqua = re.sub(mau.upper(), thaythe.upper(), ketqua)
    return ketqua

def kiemtraslug(dsslug, slug):
    if slug not in dsslug:
        return slug
    if slug in dsslug:
        danhsach = slug.split(',')
        if len(danhsach) == 1:
            return ','.join([slug, str(1)])
        else:
            stt = int(danhsach[1])
            return ','.join([slug, str(stt+1)])

