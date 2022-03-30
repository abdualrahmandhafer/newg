#عبدالرحمن طه ظافر

import numpy as np
import cv2
import matplotlib.pyplot as plt
# دعنا ps
sanpang = cv2.imread('ضع الصورة هنا')
plt.imshow(sanpang)

# استيراد وجه ليتم استبداله
dog = cv2.imread('قم بوضع الوجه الجديد الذي سيتم التبديل بة')
plt.imshow(dog[:,:,::-1])
# التعرف على منطقة الوجه ، تحتاج إلى خوارزمية
#تم #توفير # خوارزمية
# احسب نطاق الوجه باستخدام خوارزمية
face_zone = face_det.detectMultiScale(sanpang)
# احصل على ndarray ، وهي منطقة الوجه
face_zone
# ناتج من face_zone
array(
    [[182,  62,  61,  61]], dtype=int32)
# قطع وجه
dog_face = dog[40:180,70:240]
# ضغط وجه
dog_face2 = cv2.resize(dog_face,(61,61))

for x,y,w,h in face_zone:
    sanpang[y:y+w,x:x+h] = dog_face2
plt.imshow(sanpang[:,:,::-1])